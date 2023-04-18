import sys
from os import system
from time import sleep

from inicio import Character, Stats

print("----------Solo Leveling Game----------")
delay = 1
sleep(delay)

# Esto es una prueba para el ataque critico
# class Attack:

#   critrate = [1, 2, 3, 4, 5] 

#   def __init__(self) -> None:    
#        self.critrate: int = choice(self.critrate)
   
#critic = Attack()
#print(critic.critrate)
print("\nSelect the options")
print("1.- New Game")
print("2.- Options")
print("3.- Exit")
answer = input()
system('cls')

match(answer):
    case '1':
        # effect_sentences = {
        #     'warrior': "Your weapons: \n "+{Character.default_stats["warrior"]},
        #     'mage': "perfecto, ya sabia que te gustaban los palos",
        #     'hunter': "okey wey ta chido hunter",
        # }

        #print(Stats(**Character.default_stats['warrior']))

        while True:
            print("Welcome Player, select you class")
            print(f"\nWarrior | {(Stats(**Character.default_stats['warrior']))} \nMage  |  {(Stats(**Character.default_stats['mage']))} \nHunter | {(Stats(**Character.default_stats['hunter']))} \n")
            answer = input().lower()
            if answer in Character.default_stats:
                weapons = Character.default_stats[answer]['weapons']
                system('cls')
                print(f"YOU SELECTED {answer.upper()}\n")
                print("Your weapons are: ")
                print(*(weapon for weapon in weapons), sep='\n')
                input('\n\nPulsa cualquier tecla para empezar tu aventura')
                system('cls')
                print("An Enemy has appeared, select an option!\n\n1. Attack()")
                print("2. Defense\n3. Escape")
                battleanswer=input()
                break
            else:
                print('Please select a valid class')
        
    case'2':
        sleep(delay)
        print("Aqui en un futuro implementaremos la opcion de agregar buffs desde un inicio")
        
    case'3':
        sleep(delay)
        print("Thanks for playing, see you later")
        sys.exit()