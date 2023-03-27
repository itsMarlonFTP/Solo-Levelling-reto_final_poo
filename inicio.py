
""" class Stats:
    def __init__(self,hp,mana,power,strength) -> None:
        self.hp:int=hp
        self.mana:int=mana
        self.power:int=power
        self.strength:int=strength
        
    
    def Warrior(self):
        self.hp = 150
        self.mana=60
        self.power=0
        self.strength=50
        
    def Hunter(self):
        self.hp = 100
        self.mana=60
        self.power=0
        self.strength=100
        
    def Mage(self):
        self.hp = 125
        self.mana=150
        self.power=50
        self.strength=15
    
    def Goblins(self):
        self.hp = 150
        self.mana=60
        self.power=0
        self.strength=50
        
    def Skinwalker(self):
        self.hp = 150
        self.mana=60
        self.power=0
        self.strength=50
        
    def Boss(self):
        self.hp = 150
        self.mana=60
        self.power=0
        self.strength=50 """

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
        
personaje_1 = Character('mage')
personaje_2 = Character('mage')
personaje_2.stats.mana += 50 
print(personaje_1.stats)
print(personaje_2.stats)