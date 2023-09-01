import random
from playsound import playsound
import time
import pyfiglet

game = pyfiglet.figlet_format("Dice Game",font="doom")
print(game)
# creating a die function which will give us output from 1 to 6
def dice (y) :
    dice_drawing = {
        1: (
            ''' 
                -----
                |   |
                | o |
                |   |
                ----- '''
        ),
        2: (
            '''
               -----
               |o  |
               |   |
               |  o|
               -----'''
        ),
        3: (
            '''
               -----
               |o  |
               | o |
               |  o|
               -----'''
        ),
        4: (
            '''
               -----
               |o o|
               |   |
               |o o|
               -----'''
        ),
        5: (
            '''
               -----
               |o o|
               | o |
               |o o|
               -----'''
        ),
        6: (
            '''
               -----
               |o o|
               |o o|
               |o o|
               -----'''
        ),
    }
    return dice_drawing.get(y,"something went wrong")

#rowling 2 die

a = int(input("press 1 to roll die :- "))
if a == 1:
    output1 = random.randint(1,6)
    output2 = random.randint(1,6)
    playsound("_YOUR_PATH_") # Copy past path of die.mp3 _YOUR_PATH_ --> Copied_path
    print (f'{dice(output1)} \t {dice(output2)}')
    time.sleep(3)
    print("\n its now computers turn \n \n ")
    comp1 = random.randint(1,6)
    comp2 = random.randint(1,6)
    playsound("_YOUR_PATH_") # Copy past path of die.mp3 _YOUR_PATH_ --> Copied_path
    print(f"{dice(comp1)} \t {dice(comp2)}")
    player = output1 + output2
    computer = comp1 + comp2
    print("\n\n")
    if player > computer :
        print("\t HURRAY!!! you won the game")
    else:
        print("\t BAD :-< You lose")
else :
    print("something went wrong try again ")

