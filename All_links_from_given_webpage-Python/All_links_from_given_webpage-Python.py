import requests as rq
from bs4 import BeautifulSoup

url=input("Enter Link: ")
if("https" or "http") in url:
    data=rq.get(url)
else:
    data=rq.get("https://" + url)

soup=BeautifulSoup(data.text,"html.parser")             #Creează un obiect care contine tot HTML-ul paginii
                                                        #"html.parser" → spune să folosească parser-ul HTML intern al lui Python.
links=[]

for link in soup.find_all("a"):                         #soup.find_all("a") → caută toate etichetele <a> (link-uri) din pagină.
    links.append(link.get("href"))                      #link.get("href") → ia atributul href din fiecare <a>.
                                                        #<a href="https://google.com">Click aici</a>
                                                        #href="https://google.com" = atributul href (hyperlink reference).
    
with open("MyLinks.txt",'a') as saved:                  #Deschide fișierul myLinks.txt în modul append ('a' = adaugă la final, nu suprascrie).
    print(links[:10],file=saved)                        #Scrie primele 10 link-uri (links[:10]) în fișier.
    
    



"""
rq.get(...) returnează un obiect de tip Response.
De exemplu:
data = rq.get("https://openai.com")
Acum data are:
data.status_code → codul răspunsului (ex. 200 = ok, 404 = pagina nu există).
data.text → conținutul paginii ca text (HTML).
data.content → același conținut, dar în bytes.
data.headers → informații despre răspuns (tip de fișier, server, etc.).                         
"""                         
                            
"""                       
Rezumat pe scurt:
1.Primește un link de la utilizator.
2.Face un GET la adresa respectivă (adaugă https:// dacă lipsește).
3.Parsează HTML-ul cu BeautifulSoup.
4.Extrage toate linkurile (href) din <a>.
5.Salvează primele 10 linkuri într-un fișier text myLinks.txt.
"""