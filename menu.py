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
        print("Test 1")
        
    case'2':
        sleep(delay)
        print("Test 2")