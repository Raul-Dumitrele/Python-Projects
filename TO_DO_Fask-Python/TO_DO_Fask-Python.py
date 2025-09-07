from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from markupsafe import escape




app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"              #Create the database test.db in the project directory.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False                      #Turn off unnecessary notifications with SQLALCHEMY_TRACK_MODIFICATIONS.
db=SQLAlchemy(app)
with app.app_context():
    db.create_all()


class Todo(db.Model):                                                           #– Each task has:
    id=db.Column(db.Integer,primary_key=True)                                   #id → unique identifier
    content=db.Column(db.String(200),nullable=False)                            #content → task text
    complete=db.Column(db.Integer,default=0)                                    #completed → 0/1 (uncompleted/completed)
    pub_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)      #pub_date → when it was created

    def __repr__(self):
       return f"<Task {self.id} - {self.content}>"
   
   
@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        task_content=request.form["task"]
        new_task=Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There is an issue"
    else:
        tasks = Todo.query.order_by(Todo.pub_date).all()
        return render_template("index.html", tasks=tasks)
        
"""
POST → când trimiți formularul (scrii un task nou), ia valoarea din request.form["task"], creează un obiect Todo, îl bagă în DB și salvează.
După ce a terminat, face redirect("/") → reîncarcă pagina cu lista actualizată
GET → când deschizi site-ul, extrage toate taskurile din DB, le sortează după pub_date și le dă la index.html.(else)
"""
        
@app.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.get_or_404(id)                          #Caut task-ul,daca nu exista imi da eroare 404
    try:    
        db.session.delete(task)
        db.session.commit()
        return redirect("/")
    except:
        return "This is an Problem while deleting"
        
"""
Primește un id din URL.
Caută taskul cu get_or_404 → dacă nu există, îți dă direct 404.
Dacă există, îl șterge din DB și face commit.
Redirect iar către /.
"""
        
@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    task = Todo.query.get_or_404(id)                            
    if request.method == "POST":
        task.content = request.form["task"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There is an issue"
    else:
        tasks = Todo.query.order_by(Todo.pub_date).all()
        return render_template("index.html", update_task=task, tasks=tasks)
        
"""
Găsește taskul după id.
GET → practic deschizi pagina de update. Tot index.html e folosit, dar pe lângă lista de tasks mai trimite și update_task=task. În template probabil ai un formular special pentru editare.
POST → când trimiți formularul, actualizează task.content cu noul text, dă commit și redirect la /.
"""


if __name__ == "__main__":
    app.run(debug=True)

