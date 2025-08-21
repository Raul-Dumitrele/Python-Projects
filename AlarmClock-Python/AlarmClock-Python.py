# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
root=Tk()                                                               #creeaza fereastra principala si stabileste marimea acesteia
root.geometry("400x200")
                                                                        #Thinker=Interfata

def Threading():                                                       #aceasta functie porneste functia alarm(),daca nu am avea aceasta functie, interfara s-ar bloca pana cand s-ar declansa alarma
    t1=Thread(target=alarm)
    t1.start()
    
def alarm():
    while True:
        set_alarm_time=f"{hour.get()}:{minute.get()}:{second.get()}"    #seteaza timpul la care sa sune alarma
        time.sleep(1)                                                   #asteapta o secunda
        current_time=datetime.datetime.now().strftime("%H:%M:%S")         #seteaza timpul actual
        print(current_time,set_alarm_time)
        
        if current_time==set_alarm_time:                                #verifica daca timpul actual este egal cu ora setata si porneste fisierul audio sound.wav
            print("Time to wake up!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)        #linia asta pune text "Alarm Clock" roșu, bold, de 20, centrat în fereastră, cu spațiu de 10 față de alte elemente sus jos.
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()


frame=Frame(root)
frame.pack()



hour=StringVar(root)                                                    #se creaza io variabila care tine minte un text(string) si este conectata la elementele grafice din meniu
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)                                                               #se creeaza un tuplu cuu orele,aceste valori vor aparea in meniul derulat
hour.set(hours[0])                                                      #seteaza valoarea initiala a variabilei hour ca fiind hours[0]

#aici vom face butonul care va aparea pe fereastra unde vom selecta ora pentru a seta alarma
hrs=OptionMenu(frame,hour,*hours)                                       #creeaza un meniu DROPDOWN in care poti alege o valoare
                                                                        # frame = locul unde punem meniul 
                                                                        # hour = variabila legată de meniu → când alegi o valoare, hour.get() îți dă ce ai selectat.
                                                                        # *hours = pune toate valorile din tuplu în meniul derulant. 
                                                                        
hrs.pack(side=LEFT)                                                     #afiseaza meniul in interfata si il aliniaza in partea stanga a frameului


minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins=OptionMenu(frame,minute,*minutes)
mins.pack(side=LEFT)

second=StringVar(root)
seconds=('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs=OptionMenu(frame,second,*seconds)
secs.pack(side=LEFT)

#Creeaza un buton "Set Alarm" si atunci cand este apasat porneste functia Threading() → care la randul ei porneste alarma
Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

root.mainloop()