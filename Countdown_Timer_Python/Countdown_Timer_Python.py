import time

def Countdown(t):
    while t:
        mins,secs=divmod(t,60)                                  #Splits t into minutes(t//60) and seconds(t%60)     divmod(125, 60) → (2, 5)
        timer='{:02d}:{:02d}'.format(mins,secs)                 #Creates a string showing the countdown in MM:SS format. :02d means “2 digits, pad with 0 if needed”.   if mins=0, secs=7 → "00:07".
        print(timer,end="\r")                                   #We use end="\r" to display the timer on the same line, meaning to reset the same line and not appear one below another
        time.sleep(1)
        t-=1
        
    print('Timer Completed!')
    
t=input('Enter the time in seconds:')

Countdown(int(t))