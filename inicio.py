class Damage: 
    # def __init__(self,AttackSword, AttackSpell, spells, objects) -> None:
    #     self.AttackSword:int=AttackSword
    #     self.AttackSpell:int=AttackSpell
    #     self.spells:int=spells
    #     self.objects:int=objects
    
    prob_critrate = [1, 2, 3, 4, 5] # Esto es una prueba para el ataque critico

    def __init__(self) -> None:    
                self.prob_critrate: int = choice(self.prob_critrate)
        
prob_critic = Damage()
if prob_critic != 5 :
    critic = False
else:
    critic = True
                            #print(critic.critrate)
                            #print("Daño critico:")
print(critic)
    

class Stats:

    def __init__(self, **options) -> None:    
        self.hp: int = options.get('hp', None) or 150
        self.mana: int = options.get('mana', None) or 60
        self.power: int = options.get('power', None) or 0
        self.strength: int = options.get('strength', None) or 50

    def __repr__(self) -> str:
        return f'HP: {self.hp} \tMana: {self.mana} \tPower: {self.power} \tStrength: {self.strength}'


class Character:

    default_stats = {
        'warrior': {'hp': 200},
        'hunter': {'hp':100, 'strength':100},
        'mage': {'hp':150, 'mana':150, 'power':100, 'strength':15,},
        'goblin': {'hp': 25},
        'skinwalker': {},
        'boss': {'hp':300, 'mana':150, 'power':100, 'strength':75},
    }

    def __init__(self, character_type: str) -> None:
        self.stats = Stats(**Character.default_stats[character_type])
    
    default_weapons = {
        'warrior': {'sword': 0.5, 'shield': 0.8},
        'hunter': {'dagger': 0.5},
        'mage': {'staff': 0.3},
        'goblin': {'knife': 0.4},
        'skinwalker': {'claws': 0.6},
        'boss': {'scythe': 0.5},
    }

if __name__ == '__main__':
    personaje_1 = Character('mage')
    personaje_2 = Character('mage')

    personaje_2.stats.mana += 50 
    print(personaje_1.stats)
    print(personaje_2.stats)
# <<<<<<< Updated upstream

# class Items: 

#     def __init__(self, hp_potion: int) -> None:
#         self.stats = Stats(**Character.default_stats[hp_potion])

#     HPpoti: int = Character() * 0.75

# print()



####### Randomizer for the CritRate Damage
# class Attack:

#     critrate = [1, 2, 3, 4, 5]

#     def __init__(self) -> None:    
#         self.critrate: int = choice(self.critrate)
   

# critic = Attack()
# print(critic.critrate)