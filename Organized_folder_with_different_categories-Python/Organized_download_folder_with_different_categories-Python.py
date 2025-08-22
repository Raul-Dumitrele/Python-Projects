import os
import shutil

os.chdir(r"C:\Users\Dumitrele George\Desktop\New folder")
#os.chdir() schimbă directorul curent de lucru.
#Deci scriptul va lucra în folderul C:\Users\Dumitrele George\Desktop

files=os.listdir()
#os.listdir() returnează o listă cu toate fișierele și folderele din directorul curent.



extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif"],
    "videos": [".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"],
    "design": [".xd", ".psd"]
}


def sorting(file):
    keys=list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            #print(ext)
            if file.endswith(ext):
                return key
#Primește un fișier și caută ce categorie i se potrivește după extensie.
#Returnează cheia (ex. "images", "documents", etc.). sau None daca nu gaseste


for file in files:
    dist = sorting(file)
    if dist:
        dest_folder = "C:/Users/Dumitrele George/Desktop/Organized_download_folder_with_different_categories-Python/sorted/" + dist
    else:
        dest_folder = "C:/Users/Dumitrele George/Desktop/Organized_download_folder_with_different_categories-Python/sorted/others"

    # Creează folderul dacă nu există
    os.makedirs(dest_folder, exist_ok=True)

    # Mută fișierul în folderul corespunzător
    try:
        shutil.move(file, os.path.join(dest_folder, file))
    except:
        print(file + " is already exist")


#shutil.move muta fisierul in folderul nou
#os.makedirs(dest_folder, exist_ok=True) ceeaza folderul in calea data de dest_foder daca nu exista
#os.path.join(dest_folder, file) = calea completă a fișierului în folderul de sortare ,iar shutil.move il muta efectiv in folder






#dest_folder = "C:/Users/Dumitrele George/Desktop/sorted/images"
#file = "poza1.jpg"

#os.path.join(dest_folder, file)
# Rezultatul: "C:/Users/Dumitrele George/Desktop/sorted/images/poza1.jpg"













