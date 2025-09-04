import csv

import requests


status_dict = {"Website": "Status"}                                                         #Creaza un dictionar cu un singurr element cheie "Website" si valoarea "Status"


def main():
    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()                                                          #șterge spațiile și newline-ul (\n).
            status = requests.get(website).status_code                                      #face o cerere GET către site și îți dă codul HTTP.
            status_dict[website] = "working" if status == 200 else "not working"            #daca este 200 site-ul merge, ceva e în neregulă (404, 500)
             

    # print(status_dict)
    with open("website_status.csv", "w", newline="") as fw:                                 #creeam un fisier .csv si scriem perechi cheie-valoare din dictionar pe rand
        csv_writers = csv.writer(fw)                                                        #ia listele Python si le scrie ca randuri CSV in fisier
        for key in status_dict.keys():
            csv_writers.writerow([key, status_dict[key]])                                   #ia cheia(key) si valoarea asociata(Status_dict[key]) si le scrie ca o lista in fisierul CSV


if __name__ == "__main__":                                                                  #Verifică dacă scriptul este rulat direct (nu importat).
    main()    
                                                                                            #Dacă e rulat direct, atunci apelează funcția main().
                                                                                            #Dacă e importat într-un alt fișier, codul din main() nu se execută automat, dar poți să o chemi manual.
    
    
    
    
    