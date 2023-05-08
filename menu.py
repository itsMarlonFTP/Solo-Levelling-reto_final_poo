import sys
from os import system
from time import sleep
import random
from random import choice, choices
from inicio import Character, Stats, Damage

system('cls')
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
print("3.- Exit \n")
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

        
            print("Welcome Player, select you class")
            print(f"\nWarrior | {(Stats(**Character.default_stats['warrior']['stats']))} \nMage  |  {(Stats(**Character.default_stats['mage']['stats']))} \nHunter | {(Stats(**Character.default_stats['hunter']['stats']))} \n")
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
                
                for i in range(1, 4):
                    phase = i
                    if player.is_alive or i > 3:
                        enemy = random.choice(['goblin','skinwalker'])
                        if enemy in Character.default_stats:
                            enemystats=Character(enemy)
                            print('..................................................................................')
                            print(*(enemy),' has appeared')
                            while (enemystats.stats.hp>0):
                            #while enemy.stats.hp < 0:
                                print('PHASE', phase)
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
                                        herodamagedifference = (player.stats.strength * player.default_stats[answer]['weaponattack'])
                                        enemystats.stats.hp = enemystats.stats.hp - herodamagedifference

                                        if enemystats.stats.hp < 0:
                                            break

                                        damagedifference = (enemystats.stats.strength * enemystats.default_stats[enemy]['weaponattack'])
                                        player.stats.hp = player.stats.hp - damagedifference
                                        
                                        if player.stats.hp < 0:
                                            break
                                    case '2':
                                        print('Defensa')
                                                            
                                    case '3':
                                        print()
                                        if Damage.escape is False:
                                            print('¡¡You failed to escape!!')
                                        else:
                                            print("¡¡You managed to escape safely!!")
                                            break
                                                    
                                print("\nYou have done", herodamagedifference, 'damage to', enemy)
                                print(enemy, 'has done', damagedifference, 'damage to you\n')

                            if enemystats.is_alive():
                                print('YOU DIED, ¿try again?')
                            if player.is_alive():
                                print('¡¡', enemy, 'has been slain, keep going!!')

                
                print('BOSS PHASE \n Prepare for the fight -------------------')
                input()


            

            else:
                print('Please select a valid class')
            
    case'2':
        sleep(delay)
        print("Aqui en un futuro implementaremos la opcion de agregar buffs desde un inicio")
        
    case'3':
        sleep(delay)
        print("Thanks for playing, see you later")
        sys.exit()

