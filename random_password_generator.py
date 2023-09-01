# this is a password generater and checker
# if you enter your own pass word it will check if it is valid or not
# if you dont want to create yor pssword it generate password for you under a very specific condition
import random
import string
import re
import pyfiglet


character = list(string.ascii_letters + string.digits + "~!@#$%^&*")
def generate (x):
    password = ""
    for i in range (0,x) :
        k = random.choice(character)
        password += k
    return password

def cheacker (y):
    c = 0
    if (len(y)<6):
        c+=1
    elif not (re.search("[a-z]",y)):
        c+=1
    elif not (re.search("[A-Z]",y)):
        c+=1
    elif not (re.search("[0-9]",y)):
        c+=1
    elif not (re.search("[~!@#$%^&*]", y)):
        c+=1
    return c

print(pyfiglet.figlet_format("Password Generator Cheaker" , font="ogre"))

a = input("Do you want to generate a password? :- ")
if a == "yes" or a == "YES" or a == "Yes" :
    while True:
        b = int(input("Enter a length of password :- "))
        if (b <= 6):
            print("length must be greater than or equal to 6")
            continue
        else :
            break
    password = generate(b)
    while True :
       if(cheacker(password) == 0):
             break
       else:
           password = generate(b)
    print("\n\n" ,password, " <-- this is your password \n")
else :
    print("create your own password")
    while True :
        q = input("enter your password :- ")
        if cheacker(q) > 0:
            print("password is in valid ")
        else :
            print("password is valid ")
            break