import os

text = input("Input text: ")
path = input("Path: ")

def getfiles(path, text):
    found = False
    for root, dirs, files in os.walk(path):
        for file_name in files: 
            abs_path = os.path.join(root, file_name)                                #construieste calea absoluta a fisierului
            try:
                with open(abs_path, "r", errors="ignore") as f:
                    if text in f.read():                                            #citeste continutul fisierului si verifica daca apare textul pe care il cautam
                        print(f"{text} found in {abs_path}")                        #daca a gasit afiseaza calea completa a fisierului
                        found = True
            except:
                # dacă e fișier binar sau nu poate fi deschis
                continue
    if not found:
        print(f"{text} not found!")

getfiles(path, text)

                        
                        
                        
          
#for root, dirs, files in os.walk(path):
#        for file_name in files:
#            abs_path = os.path.join(root, file_name)
#Loop-ul mare (for root, dirs, files) merge prin fiecare director și subdirector.
#Loop-ul mic (for file_name in files) ia fiecare fișier din directorul curent.
#os.path.join(root, file_name) → îți face calea completă până la fișier, ca să-l poți deschide.