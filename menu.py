import sys
from time import sleep
from os import system

print("----------Solo Leveling Game----------")
delay = 1
sleep(delay)

print("\nSelect the options")
print("1.- New Game")
print("2.- Options")
print("3.- Exit")
answer = input()
system('cls')

match(answer):
    case '1':
        sleep(delay)
        print("Welcome to Solo Levelling Game, select you class")
        sleep(delay)
        print("\nWarrior \nMage \nHunter\n")
        answer= input()
        
        if answer != "warrior" "Warrior":
            print("This class does not exist, please select a class existed")
        else:
            print()
        if answer != "mage" "Mage":
            print("This class does not exist, please select a class existed")
        else:
            print()
        if answer != "Hunter" "hunter":
            print("This class does not exist, please select a class existed")
        else:
            print()
    case'2':
        sleep(delay)
        print("I don't know what to put here c:")
        
    case'3':
        sleep(delay)
        print("Vuelva pronto")
        sys.exit()