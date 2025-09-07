# ✅ Flask To-Do App  

This project is a simple **To-Do list web application** built with [Flask](https://flask.palletsprojects.com/) and [SQLAlchemy](https://www.sqlalchemy.org/).  
It lets you add, update, and delete tasks, all stored in a **SQLite database**.  

It’s a clean example of how to build a CRUD (Create, Read, Update, Delete) app with Python and Flask.  

---

## 📋 Overview  
This app demonstrates how you can:  
- Create a **web app** using Flask.  
- Connect to a **database** using SQLAlchemy ORM.  
- Build routes for **adding, deleting, and updating** tasks.  
- Use **Jinja2 templates** to dynamically render data into HTML pages.  

---

## ⚙️ How it Works  
1. **Start the app**: Flask runs a local web server on `http://127.0.0.1:5000/`.  
2. **Home page (`/`)**:  
   - Shows all tasks from the database.  
   - Lets you add a new task via a form.  
3. **Delete (`/delete/<id>`)**: Removes the selected task.  
4. **Update (`/update/<id>`)**: Opens a form to modify a task, then saves the change.  
5. **Database**: All tasks are stored in `test.db` (SQLite).  

---

## 📦 Requirements  
- Python 3.8+  
- Libraries:  
  - `Flask`  
  - `Flask-SQLAlchemy`  

Install them with:  
```bash
pip install flask flask_sqlalchemy
```  

---

## ⚠️ Important  
- Run the app with:  
  ```bash
  python app.py
  ```  
- By default, it uses `test.db` in the project folder.  
- If the DB doesn’t exist, create it in a Python shell:  
  ```python
  from app import db
  db.create_all()
  ```  

---

## 🔧 Installation  
Clone the repository and navigate into it:  
```bash
git clone https://github.com/username/flask-todo-app.git
cd flask-todo-app
```  

Run the app:  
```bash
python app.py
```  

Then open in your browser:  
```
http://127.0.0.1:5000/
```  

---

## ✨ Features  
- Add new tasks  
- Delete tasks  
- Update tasks  
- Tasks ordered by creation date  

---

## 👤 Author  
[Raul Dumitrele](https://github.com/Raul-Dumitrele)  
