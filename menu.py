import sys
from os import system
from time import sleep
import random
from inicio import Character, Stats, Items, Player


system('cls')
print("----------Solo Leveling Game----------")
delay = 1
sleep(delay)

print("\nSelect the options")
print("1.- New Game")
print("2.- Options")
print("3.- Exit \n")
answer = 'default'
answer = input()
system('cls')


def choose_character_class():
    print("Welcome Player, select you class")
    print(f"\nWarrior | {(Stats(**Character.default_stats['warrior']['stats']))} \nMage  |  {(Stats(**Character.default_stats['mage']['stats']))} \nHunter | {(Stats(**Character.default_stats['hunter']['stats']))} \n")
    while True:
        classanswer = input().lower()
        if classanswer in Character.default_stats:
            player = Player(classanswer)
            weapons = Character.default_stats[classanswer]['weapons']
            system('cls')
            print(f"YOU SELECTED {classanswer.upper()}\n")
            print("Your weapons are: ")
            print(*(weapon for weapon in weapons), sep='\n')
            
            input('\n\nPulsa cualquier tecla para empezar tu aventura')
            system('cls')
            return player, classanswer
        else:
            print('Please select a valid class')

def start_game():
    player, classanswer = choose_character_class()
    
    for i in range(1, 4):
        phase = i
        round = 1
        if player.is_alive or i > 3:
            enemy_name = random.choice(['goblin','skinwalker'])
            if enemy_name in Character.default_stats:
                enemy = Character(enemy_name)
                print('..................................................................................')
                print(enemy_name,' has appeared')
                print(classanswer)
                while (enemy.stats.hp > 0):
                
                    print('PHASE', phase)
                    print('Select an option!\n\n1. Attack()')
                    print("2. Defense\n3. Items\n4. Escape")
                    print("\n\n\t" + enemy_name.upper())
                    print(enemy.stats)
                    print("\n\n      YOUR STATS")
                    print(player.stats)
                    battleanswer = input()
                            
                            
                    match(battleanswer):
                        case '1':
                            # from pdb import set_trace; set_trace()

                            if player.is_critic() is True:
                                critic = player.default_stats[classanswer]['weaponattack'] + 0.2
                            else: 
                                critic = player.default_stats[classanswer]['weaponattack'] 
                            #player.default_stats[str(classanswer)]['weaponattack'] -= len(Character.default_stats)
                            herodamagedifference = (player.stats.strength * critic)
                            enemy.stats.hp = enemy.stats.hp - herodamagedifference

                            damagedifference = (enemy.stats.strength * enemy.default_stats[enemy_name]['weaponattack'])
                            player.stats.hp = player.stats.hp - damagedifference
                            
                            if player.stats.hp < 0:
                                break

                            if enemy.stats.hp < 0:
                                break

                            print("\nYou have done", herodamagedifference, 'damage to', enemy)
                            print(enemy, 'has done', damagedifference, 'damage to you\n')

                            round = round + 1
                        case '2':
                            if classanswer == 'warrior':
                                damagedifference = (enemy.stats.strength * enemy.default_stats[enemy_name]['weaponattack'])* player.default_stats['warrior']['shield']
                                player.stats.hp = player.stats.hp - damagedifference
                                print(enemy, 'has done', damagedifference, 'damage to you\n')
                            else:
                                print('Oh sorry, only class warrior can use defense')
                                damagedifference = (enemy.stats.strength * enemy.default_stats[enemy]['weaponattack'])
                                player.stats.hp = player.stats.hp - damagedifference
                                print(enemy, 'has done', damagedifference, 'damage to you\n')
                
                        case '3':
                            if  Items.items < 0:
                                print('You do not have items')
                            else:
                                player.stats.hp += 100
                                Items.items -=1
                        case '4':
                            print()
                            if player.escape():
                                print('¡¡You failed to escape!!')
                            else:
                                print("¡¡You managed to escape safely!!")
                                sys.exit()
                    
            if enemy.is_alive():
                print('YOU DIED')
                sys.exit() 
            elif player.is_alive():
                print('¡¡', enemy, 'has been slain, keep going!!')   
            if player.stats.hp > 70:
                print("Congratulations, you just earn a heatlh potion")
                Items.items += 1
        
        

    
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
                    critic = player.default_stats[classanswer]['weaponattack']
                    #     critic_attack = player.default_stats[classanswer]['weaponattack']
                    # else: 
                    #     critic_attack = player.default_stats[classanswer]['weaponattack'] + 0.2
                    #player.default_stats[str(classanswer)]['weaponattack'] -= len(Character.default_stats)
                    herodamagedifference = (player.stats.strength * critic)
                    bossstats.stats.hp = bossstats.stats.hp - herodamagedifference

                    damagedifference = (bossstats.stats.strength * bossstats.default_stats[enemy_name]['weaponattack'])
                    player.stats.hp = player.stats.hp - damagedifference

                    if player.stats.hp < 0:
                        break

                    if bossstats.stats.hp < 0:
                        break

                    print("\nYou have done", herodamagedifference, 'damage to', boss)
                    print(boss, 'has done', damagedifference, 'damage to you\n')
                    round = round + 1

                case '2':
                        if classanswer == 'warrior':
                            damagedifference = (enemy.stats.strength * enemy.default_stats[enemy_name]['weaponattack'])* player.default_stats['warrior']['shield']
                            player.stats.hp = player.stats.hp - damagedifference
                            print(enemy, 'has done', damagedifference, 'damage to you\n')
                        else:
                            print('Oh sorry, only class warrior can use defense')
                            damagedifference = (enemy.stats.strength * enemy.default_stats[enemy_name]['weaponattack'])
                            player.stats.hp = player.stats.hp - damagedifference
                            print(enemy, 'has done', damagedifference, 'damage to you\n')
                
                case '3':
                    if  Items.items < 0:
                        print('You do not have items')
                    else:
                        player.stats.hp += 100
                        Items.items -=1
                case '4':
                    print()
                    if player.escape():
                        print('¡¡You failed to escape!!')
                    else:
                        print("¡¡You managed to escape safely!!")
                        sys.exit()
                        
            if enemy.is_alive():
                print('YOU DIED')
                sys.exit() 
            elif player.is_alive():
                print('¡¡', boss, 'has been slain, keep going!!')   
            if player.stats.hp > 70:
                print("Congratulations, you just earn a heatlh potion")
                Items.items += 1
        

match(answer):
    case '1':
        start_game()
        
    case'2':
        sleep(delay)
        print("Aqui en un futuro implementaremos la opcion de agregar buffs desde un inicio")
        
    case'3':
        sleep(delay)
        print("Thanks for playing, see you later")
        sys.exit()

