import tkinter as tk
import random

#creeaza fereastra principala
fereastra=tk.Tk()
fereastra.title("Sudoku")

#creeam un frame layout
frame_stanga=tk.Frame(fereastra)
frame_dreapta=tk.Frame(fereastra)

frame_stanga.pack(side="left",padx=10,pady=10)
frame_dreapta.pack(side="right",padx=10,pady=10)



#creeaza functia pentru actiunea butonului
def apasa_buton():
    label.config(text="Ai apasat butonul!")
    
#creeaaza un buton
buton = tk.Button(frame_stanga,text="Generate Sudoku", command=apasa_buton)
buton.pack(pady=10)         
buton = tk.Button(frame_stanga,text="Solve Sudoku", command=apasa_buton)
buton.pack(pady=10) 
buton = tk.Button(frame_stanga,text="Clear Table", command=apasa_buton)
buton.pack(pady=10 )        

#creeaza un label pt feedback
label=tk.Label(frame_stanga,text="Apasa butonul pentru actiune")
label.pack(pady=10)

# Dimensiunile grilei Sudoku
Celula=40
Latime=Celula*9
Inaltile=Celula*9

# Creează un Canvas pentru tabel
canvas=tk.Canvas(frame_dreapta,width=Latime,height=Inaltile,bg="white")
canvas.pack()

# Grilă globală pentru Sudoku
grila = [[0] * 9 for _ in range(9)]
entries = []  # Lista pentru Entry-uri

# Funcție pentru desenarea grilei
def deseneaza_grila():
    for i in range(10):
        grosime = 3 if i % 3 == 0 else 1            # Linii mai groase pentru blocurile 3x3
        # Linii orizontale
        canvas.create_line(0, i*Celula , Latime , i*Celula , width=grosime)
        # Linii verticale
        canvas.create_line(i * Celula, 0, i * Celula, Inaltile, width=grosime)

# Funcție pentru adăugarea celulelor
def adauga_celule():
    global entries
    entries=[]            #resetam lista
    for i in range(9):
        rand=[]
        for j in range(9):
            # Creează o celulă Entry
            entry=tk.Entry(fereastra,width=2,justify="center",font=("Arial",16),bd=0)
            # Adaugă un event pentru a detecta modificarea valorii
            entry.bind("<KeyRelease>", lambda event, r=i, c=j: valideaza_input(r, c))
            # Plasează celula în Canvas
            canvas.create_window(j * Celula + Celula // 2, i * Celula + Celula // 2, window=entry, width=Celula-5, height=Celula-5)
            rand.append(entry)
        entries.append(rand)
    return entries



def valideaza_input(rand,col):
    """Verifica daca valoarea introdusa intr-o coloana este valida"""
    valoare = entries[rand][col].get()
    if valoare=="":     # Dacă celula este goală, resetează culoarea la alb (sau transparent)
        entries[rand][col].config(bg="white")
        return True
    
    try:
        numar=int(valoare)
    except ValueError:
        numar = 0
        
    if numar < 1 or numar > 9:
        entries[rand][col].config(bg="red")  # Culoare roșie pentru invalid
        return False
    elif este_valid(grila, rand, col, numar):
        entries[rand][col].config(bg="green")  # Culoare verde pentru valid
        return True
    else:
        entries[rand][col].config(bg="yellow")  # Culoare galbenă pentru valid dar incorect
        return False
    
    
    
    
"""# Creează o funcție pentru tabelul Sudoku(creaza doar tabelul)
def creeaza_tabel(parent):
    for i in range(9):      # 9 rânduri
        for j in range(9):      # 9 coloane
            celula=tk.Entry(parent,width=2,justify="center",font=("Arial",16))
            celula.grid(row=i,column= j,padx=2,pady=2)

# Adaugă tabelul în frame-ul din dreapta
creeaza_tabel(frame_dreapta)
"""

def este_valid(grila,rand,col,numar):
    """Verifica daca numarul este valid si este in grila"""
    '''Verificam Randul si Coloana'''
    for i in range(9):
        if grila[rand][i]==numar or grila[i][col]==numar:
            return False
        
    """Verifica subrila 3x3"""
    start_rand , start_col = 3*(rand//3) , 3*(col//3)
    for i in range(3):
        for j in range(3):
            if grila[start_rand+i][start_col+j]== numar:
                return False
    return True


def genereaza_sudoku_complet(grila):
    """Genereaza un Sudoku complet rezolvat"""
    for rand in range(9):
        for col in range(9):
            if grila[rand][col]==0:
                numere=list(range(1,10))
                random.shuffle(numere)
                for numar in numere:
                    if este_valid(grila,rand,col,numar):
                        grila[rand][col]=numar
                        if genereaza_sudoku_complet(grila):
                            return True
                    grila[rand][col]=0
                return False
    return True


def elimina_valori(grila,dificultate=40):
    """Elimina valori din Sudoku pentru a crea puzzle-ul"""
    numere_de_eliminat=dificultate
    while numere_de_eliminat>0:
        rand = random.randint(0,8)
        col=random.randint(0,8)
        if grila[rand][col]!=0:
            grila[rand][col]=0
            numere_de_eliminat-=1
            
            
            
def afiseaza_sudoku():
    """Afiseaza Sudoku-ul generat in Entryuri"""
    for i in range(9):
        for j in range(9):
            val=grila[i][j]
            entries[i][j].delete(0,tk.END)
            if val !=0:
                entries[i][j].insert(0,str(val))
                entries[i][j].config(state="disabled",bg="lightgray")
            else:
                entries[i][j].config(state="normal",bg="white")

                
            
def rezolva_sodoku():
    """Rezolva sudoku-il si il afiseaza"""           
    global grila
    """Folosim functia pentru a genera un sudoku complet"""
    genereaza_sudoku_complet(grila)
    afiseaza_sudoku()
            
def curata_sudoku():
    """Sterge toate valorile si goleste tabelul"""
    global grila
    grila = [[0] * 9 for _ in range(9)]           #"""Reseteaza grila"""
    for i in range(9):
        for j in range(9):
            entries[i][j].config(state="normal",bg="white")   
            entries[i][j].delete(0,tk.END)      #"""Stergem fiecare celula"""
            
            

            
def genereaza_sudoku():
    global grila
    grila = [[0]*9 for _ in range (9)]          #"""Reseteaza grila"""
    genereaza_sudoku_complet(grila)
    elimina_valori(grila)
    afiseaza_sudoku()
    
    
    
    
buton_genereaza = tk.Button(frame_stanga,text="Generate Sudoku", command=genereaza_sudoku)
buton_genereaza.pack(pady=10)         
buton_solve = tk.Button(frame_stanga,text="Solve Sudoku", command=rezolva_sodoku)
buton_solve.pack(pady=10) 
buton_clear = tk.Button(frame_stanga,text="Clear Table", command=curata_sudoku)
buton_clear.pack(pady=10 ) 
    
label = tk.Label(frame_stanga, text="Apasă butonul pentru acțiune")
label.pack(pady=10)
    

#deseneaza grila si adauga celulele
deseneaza_grila()
tabel=adauga_celule()

#Ruleaza fereastra
fereastra.mainloop()












