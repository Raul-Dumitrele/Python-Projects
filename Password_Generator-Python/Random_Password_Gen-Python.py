import random
import math



alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"


#pass_len=random.randint(8,13)  #without User Input
pass_len=int(input("Enter Password Lenght:"))


# length of password by 50-30-20 formula
alpha_len=pass_len//2
num_len=math.ceil(pass_len*30/100)                  # 30% num (rounded up)
special_len=pass_len-(alpha_len+num_len)

password=[]

def generate_pass(lenght,array,is_alpha=False):
    for i in range(lenght):
        index=random.randint(0,len(array)-1)        #choose a random index
        character=array[index]                      #take the character            
        if is_alpha:                                #if it's a letter, we can randomly capitalize it
            case=random.randint(0,1)
            if case==1:                             #if the case after randomization is 1 ,we write it with a capital letter
                character=character.upper()
                
        password.append(character)                  #add the caracter to the password


# alpha password
generate_pass(alpha_len, alpha, True)   # litere (cu opțiunea de majusculă)
# numeric password
generate_pass(num_len, num)             # cifre
# special Character password
generate_pass(special_len, special)     # simboluri



# suffle the generated password list
random.shuffle(password)

# convert List To string
gen_password=""
for i in password:                      
    gen_password=gen_password+str(i)
print(gen_password)
