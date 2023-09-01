import random
import pyfiglet

print(pyfiglet.figlet_format("Game" , font="small"))
print("Stone Paper Scissor Game \n")

a = ['stone','paper','scissor']
player = input('select your move stone paper or scissor :- ')
if (player == 'stone' or player == 'scissor' or player == 'paper') :
    computer = random.choice(a)
    print("computer choes",computer , "\n")
    if(player == computer):
        print("its a tie")
    elif(player == 'scissor' and computer == 'paper'):
        print("congratulation you won")
    elif(player == 'stone' and computer == 'paper'):
        print("bad you lost")
    elif(player == 'paper' and computer == 'stone'):
        print("congratulation you won")
    elif(player == 'scissor' and computer == 'stone'):
        print("bad you lost")
    elif(player == 'stone' and computer == 'scissor'):
        print("congratulation you won")
    elif(player == 'paper' and computer == 'scissor'):
        print("bad you lost")
else :
    print("selected option is not correct ")
