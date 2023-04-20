import sys
from os import system
from time import sleep
import random
from random import choice
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
                player=Character(answer)
                weapons = Character.default_stats[answer]['weapons']
                system('cls')
                print(f"YOU SELECTED {answer.upper()}\n")
                print("Your weapons are: ")
                print(*(weapon for weapon in weapons), sep='\n')
                input('\n\nPulsa cualquier tecla para empezar tu aventura')
                system('cls')
                
                enemy = random.choice(['goblin','skinwalker'])
                if enemy in Character.default_stats:
                    enemystats=Character(enemy)
                    while (enemystats.stats.hp>0):
                        system('cls')
                        #while enemy.stats.hp < 0:
                        print(*(enemy),' has appeared, select an option!\n\n1. Attack()')
                        print("2. Defense\n3. Escape")
                        print("\t\n"+enemy)
                        print(enemystats.stats)
                        print("\n\n\tYour stats")
                        print(player.stats)
                        battleanswer=input()
                        match(battleanswer):
                            case '1':
                                enemystats.stats.hp -= 10
                                print('--------------------------------------------------------------------------')
                            case '2':
                                print()
                        print('--------------------------------------------------------------------------')
                            
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