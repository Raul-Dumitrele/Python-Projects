links = {
     "www.chatgpt.ro",
     "www.facebook.com",
     "www.youtube.com",
     "www.wikipedia.com",
}

for link in links:
    print(link.lstrip("www."))
    """ daca folosesc lstrip o atunci cand afiseaza la wikipedia o sa imi afiseze idipedia deoarece el sterge toate caracterele w si . pana cand gaseste alt caracter diferit"""
    print(link.removeprefix("www."))
    """daca folosesc removeprefix atunci o sa imi stearga doar ce i am spus eu sa stearga"""