import sys
from os import system
from time import sleep
import random
from random import choice
from random import choices
from inicio import Character, Stats, Damage

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
                        print(*(enemy),' has appeared')
                        #while enemy.stats.hp < 0:
                        print('Select an option!\n\n1. Attack()')
                        print("2. Defense\n3. Escape")
                        print("\n\n\t" + enemy.upper())
                        print(enemystats.stats)
                        print("\n\n      YOUR STATS")
                        print(player.stats)
                        battleanswer=input()
                        
                        
                        match(battleanswer):
                            case '1':
                                #player.default_stats[str(answer)]['weaponattack'] -= len(Character.default_stats)
                                print("hola")
                                print(player.default_stats[answer]['weaponattack'])
                                weaponsattack = int(player.default_stats[answer]['weaponattack'])
                                
                                damagedifference = (player.stats.strength*weaponsattack)
                                enemystats.stats.hp = enemystats.stats.hp - damagedifference
                                #enemystats.stats.hp = enemystats.stats.hp - (player.stats.strength * player.default_stats[answer]['weaponattack'])
                                
                            case '2':
                                print()
                            case '3':
                                print()
                                if Damage.escape is False:
                                    print('¡¡You failed to escape!!')
                                else:
                                    print("¡¡You managed to escape safely!!")
                                    break
                        
                        print('el enemigo te ha atacado, has perdido: ', damagedifference)
                        player.stats.hp= player.stats.hp - enemystats.stats.strength
                        print('Pulsa cualquier tecla para continuar')
                        input()
                        print('..................................................................................')
                                

                            
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