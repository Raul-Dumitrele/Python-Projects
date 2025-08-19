''' Un joc de zaruri simplu în care jucătorii încearcă să atingă cel putin un anumit scor (50 în acest caz) prin rularea unui zar.
    Regulile sunt astfel:
    Daca dai cu zarul de si obtii un scor(ex:10) si te opresti,scorul se salveaza.
    Daca dai cu zarul si primesti 1 atunci scorul se reseteaza la scorul salvat inainte si trece la urmatorul jucator.
'''
import random

def roll():
    minim=1
    maxim=6
    roll=random.randint(minim,maxim)
    return roll


while True:
    players=input("Introduceti numarul de jucatori:")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("Trebuie sa fie intre 2 - 4 jucatori")
    else:
        print("Invalid,incercati un numar intre 2 - 4")
        
max_score = 50
players_score=[0 for _ in range(players)]

while max(players_score) < max_score:
    
    for numarul_jucatorului in range(players):
    
        print("\nJucatorul",numarul_jucatorului +1,"este randul tau!\n")
        print("Scorul tau este: ",players_score[numarul_jucatorului])
        curent_score=0
        winner = 0
        while winner!=1:
            should_roll=input("Ai vrea sa dai ca zarul (y) ?")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("Ai primit: 1 ! Trecem la urmatorul jucator!\n")
                curent_score=0
                break
            else:
                curent_score+=value
                print("Ai primit: ",value,"!")
                
            print("\nScorul tau este: ",curent_score) 
            print("\nScorul total daca te-ai opri acum este: ",players_score[numarul_jucatorului]+curent_score)
            print("\nScorul daca primesti 1 este: ",players_score[numarul_jucatorului])
            if players_score[numarul_jucatorului]+curent_score>=max_score:
                winner=1
      
        players_score[numarul_jucatorului] += curent_score    
        print("\nScorul total al jucatorului",numarul_jucatorului+1 ,"este: ",players_score[numarul_jucatorului])
        if winner == 1:
            break   
max_score=max(players_score)
winning_index=players_score.index(max_score)
print("\nCastigatorul este jucatorul ",winning_index+1,"cu un scor de: ",max_score)            
