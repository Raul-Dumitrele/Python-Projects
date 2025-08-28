import sys
import img2pdf
import os

filepath=r"C:\Users\Dumitrele George\Desktop\Convert_image_to_pdf"
#filepath=sys.argv[1]


if os.path.isabs(filepath):                                             #verifica daca este cale absoluta
    with open("output.pdf","wb") as f:                                  #deschide fisierul output.pdf
        imgs=[]                                                         #initializeaza lista imgs goala
        for fname in os.listdir(filepath):                              #parcurge toate fisierele din folder-ul pe care l-am dat
            if not fname.endswith(".jpg"):                              #sare peste fisierele care nu se termina in .jpg
                continue
            path=os.path.join(filepath,fname)                           #construieste calea completa catre fisier
            if os.path.isdir(path):                                     #daca elementul e un director (nu fisier), il sare peste.
                continue
            imgs.append(path)                                           #adauga calea imaginii in lista imgs
        f.write(img2pdf.convert(imgs))                                  #transforma toate imaginile din imgs intr-un singur fisier PDF output.pdf
elif os.path.isfile(filepath):
    if filepath.endswith(".jpg"):                                       #daca calea e un fisier jpg,il transforma direct in output.pdf
        with open("output.pdf","wb") as f:
            f.write(img2pdf.convert(filepath))
else:
    print("Please input file or dir")                                   #daca nu e nici un fisier afiseaza eroare