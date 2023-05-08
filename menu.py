import sys
from os import system
from time import sleep
import random
from random import choice, choices
from inicio import Character, Stats, Damage,Items

system('cls')
print("----------Solo Leveling Game----------")
delay = 1
sleep(delay)

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
                    round = 1
                    if player.is_alive or i > 3:
                        enemy = random.choice(['goblin','skinwalker'])
                        if enemy in Character.default_stats:
                            enemystats = Character(enemy)
                            print('..................................................................................')
                            print(*(enemy),' has appeared')
                            while (enemystats.stats.hp>0):
                            
                                print('|| PHASE', phase, '|| ROUND', round)
                                print('Select an action!!!\n\n1. Attack()')
                                print("2. Defense\n3. Items\n4. Escape")
                                print("\n\n\t" + enemy.upper())
                                print(enemystats.stats)
                                print("\n\n      YOUR STATS")
                                print(player.stats)
                                battleanswer=input()
                                        
                                        
                                match(battleanswer):
                                    case '1':
                                        critic = player.default_stats[answer]['weaponattack']
                                        # if critic.crit is False:
                                        #     critic_attack = player.default_stats[answer]['weaponattack']
                                        # else: 
                                        #     critic_attack = player.default_stats[answer]['weaponattack'] + 0.2
                                        #player.default_stats[str(answer)]['weaponattack'] -= len(Character.default_stats)
                                        herodamagedifference = (player.stats.strength * critic)
                                        enemystats.stats.hp = enemystats.stats.hp - herodamagedifference

                                        damagedifference = (enemystats.stats.strength * enemystats.default_stats[enemy]['weaponattack'])
                                        player.stats.hp = player.stats.hp - damagedifference
                                        
                                        if player.stats.hp < 0:
                                            break

                                        if enemystats.stats.hp < 0:
                                            break

                                        print("\nYou have done", herodamagedifference, 'damage to', enemy)
                                        print(enemy, 'has done', damagedifference, 'damage to you\n')
                                        round = round + 1


                                    case '2':
                                         if answer == 'warrior':
                                             damagedifference = (enemystats.stats.strength * enemystats.default_stats[enemy]['weaponattack'])* player.default_stats['warrior']['shield']
                                             player.stats.hp = player.stats.hp - damagedifference
                                             print(enemy, 'has done', damagedifference, 'damage to you\n')
                                         else:
                                             print('Oh sorry, only class warrior can use defense')
                                             damagedifference = (enemystats.stats.strength * enemystats.default_stats[enemy]['weaponattack'])
                                             player.stats.hp = player.stats.hp - damagedifference
                                             print(enemy, 'has done', damagedifference, 'damage to you\n')
                                    
                                    case '3':
                                        if  Items.items == 0:
                                            print('You do not have items')
                                        else:
                                            print()
                                    case '4':
                                        print()
                                        if Damage.escape == 0:
                                            print('¡¡You failed to escape!!')
                                        else:
                                            print("¡¡You managed to escape safely!!")
                                            sys.exit()
                                
                        if enemystats.is_alive():
                            print('YOU DIED')
                            sys.exit() 
                        elif player.is_alive():
                            print('¡¡', enemy, 'has been slain, keep going!!')   
                        if player.stats.hp > 50:
                            print("Congratulations, you just earn a heatlh potion")
                            Items.items + 1
                            
                

                print('BOSS PHASE \n Prepare for the fight -------------------')
                input()
                boss = random.choice(['beru','igris'])
                if boss in Character.default_stats:
                    bossstats = Character(boss)
                    print('..................................................................................')
                    print(*(boss),' has emerged')
                    while (bossstats.stats.hp>0):
                    
                        print('|| FINAL PHASE || ROUND', round)
                        print('Select an action!!!\n\n1. Attack()')
                        print("2. Defense\n3. Items\n4. Escape")
                        print("\n\n\t" + boss.upper())
                        print(bossstats.stats)
                        print("\n\n      YOUR STATS")
                        print(player.stats)
                        battleanswer=input()
                                
                                
                        match(battleanswer):
                            case '1':
                                critic = player.default_stats[answer]['weaponattack']
                                # if critic.crit is False:
                                #     critic_attack = player.default_stats[answer]['weaponattack']
                                # else: 
                                #     critic_attack = player.default_stats[answer]['weaponattack'] + 0.2
                                #player.default_stats[str(answer)]['weaponattack'] -= len(Character.default_stats)
                                herodamagedifference = (player.stats.strength * critic)
                                bossstats.stats.hp = bossstats.stats.hp - herodamagedifference

                                damagedifference = (bossstats.stats.strength * bossstats.default_stats[enemy]['weaponattack'])
                                player.stats.hp = player.stats.hp - damagedifference
                                
                                if player.stats.hp < 0:
                                    break

                                if bossstats.stats.hp < 0:
                                    break

                                print("\nYou have done", herodamagedifference, 'damage to', boss)
                                print(boss, 'has done', damagedifference, 'damage to you\n')
                                round = round + 1

                            case '2':
                                break
                            case '3':
                                if  Items.items == 0:
                                    print('You do not have items')
                                else:
                                    print()
                            case '4':
                                print()
                                if Damage.escape == 0:
                                    print('¡¡You failed to escape!!')
                                else:
                                    print("¡¡You managed to escape safely!!")
                                    sys.exit()
                if enemystats.is_alive():
                            print('YOU DIED')
                            sys.exit() 
                elif player.is_alive():
                    print('¡¡', boss, 'has been defeated, you gain respect!!')   
                if player.stats.hp > 50:
                    print("Congratulations, you just earn a heatlh potion")
                    Items.items + 1
            

            else:
                print('Please select a valid class')
            
    case'2':
        sleep(delay)
        print("Aqui en un futuro implementaremos la opcion de agregar buffs desde un inicio")
        
    case'3':
        sleep(delay)
        print("Thanks for playing, see you later")
        sys.exit()

