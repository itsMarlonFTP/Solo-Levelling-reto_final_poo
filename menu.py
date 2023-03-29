from time import sleep
from os import system
from random import choice

print("----------Solo Leveling Game----------")
delay = 1
sleep(delay)

class Attack:

    critrate = [1, 2, 3, 4, 5]

    def __init__(self) -> None:    
        self.critrate: int = choice(self.critrate)
   
critic = Attack()
print(critic.critrate)
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