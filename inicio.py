class Damage: 
    def __init__(self,AttackSword, AttackSpell, spells, objects) -> None:
        self.AttackSword:int=AttackSword
        self.AttackSpell:int=AttackSpell
        self.spells:int=spells
        self.objects:int=objects

    def slash(self):
        self.AttackSword = 1.5 * Stats.Warrior()

class Stats:

    def __init__(self, **options) -> None:    
        self.hp: int = options.get('hp', None) or 150
        self.mana: int = options.get('mana', None) or 60
        self.power: int = options.get('power', None) or 0
        self.strength: int = options.get('strength', None) or 50

    def __repr__(self) -> str:
        return f'HP: {self.hp}\nMana: {self.mana}\nPower: {self.power}\nStrength: {self.strength}'


class Character:

    default_stats = {
        'warrior': {},
        'hunter': {'hp':100, 'strength':100},
        'mage': {'hp':125, 'mana':150, 'power':50, 'strength':15},
        'goblin': {},
        'skinwalker': {},
        'boss': {'hp':300, 'mana':150, 'power':25, 'strength':100},
    }

    def __init__(self, character_type: str) -> None:
        self.stats = Stats(**Character.default_stats[character_type])
        
        
class Weapons:
    weapon_library = {
        'dagger':1.3,
        'shield':0.3,
        'staff':1.3,
        'sword':1.3,
    }
    dagger : int = 1.3 #esto es por cuanto se multiplicará cada arma por la fuerza, para esta misma incrementar el daño inflingido
    shield : int = 0.3 #Aca puse 0.3 para que al recibir el ataque, el daño del ataque se multiplica por el valor de shield, reduciendo el valor, por lo tanto reduciendo el daño recibido
    staff : int = 1.3  #esto es por cuanto se multiplicará cada arma por la fuerza, para esta misma incrementar el daño inflingido
    sword : int = 1.3 #esto es por cuanto se multiplicará cada arma por la fuerza, para esta misma incrementar el daño inflingido

personaje_1 = Character('mage')
personaje_2 = Character('mage')

personaje_2.stats.mana += 50 
print(personaje_1.stats)
print(personaje_2.stats)
<<<<<<< Updated upstream

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