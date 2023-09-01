import random
import pyfiglet

def fun1(b):
    a = random.choice(range(0,len(s1)))
    add_to_b = random.choice("~!@#$%^&*")
    b = s1[:a] + add_to_b + s1[a:]
    return b
def fun2(a):
    a = random.choice("/*-+") + a + random.choice("<>?=")
    return a
def fun3(c):
    x = ["{}","[]","()"]
    a = random.choice(x)
    b = random.choice(range(10,99))
    if b > c :
        tem = b - c 
        c = a[0] + f"{b}" + "-" + f"{tem}" + "=" + f"{c}" + a[1]
        return c
    elif b == c :
        tem = 0
        c = a[0] + f"{b}" + "+" + f"{tem}" + "=" + f"{c}" + a[1]
        return c
    else :
        tem = c - b 
        c = a[0] + f"{b}" + "+" + f"{tem}" + "=" + f"{c}" + a[1]
        return c 
    

print(pyfiglet.figlet_format("Personalised Password Generator", font="drpepper"))

print("\n You Need to give me 2 string and one 2 digit number \n in total 3 things and I will generate a password \n the generated password is based on that and easy to remember \n")

s1 = input(" > Enter your first word :- ")
s2 = input(" > Enter your second word :- ")
n = int(input(" > Enter your 2 digit number :- "))


if s1 != "" and s2 != "" and 10<n<99 : 
    pwd = fun1(s1) + fun2(s2) + fun3(n)
    print(f" > Your personalised is \n > {pwd} " )

else :
    print(" > You forgot to provide required info run it again")