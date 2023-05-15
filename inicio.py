from random import choices

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
        'warrior': {
            'stats': {'hp': 200,},
            'weapons': {'sword': 0.5},
            'weaponattack':0.5,
            'shield':0.3
        },
        'hunter':{
            'stats': {'hp':100,'strength':100},
            'weapons': {'dagger'},
            'weaponattack':0.5
        },
        
        'mage':{
            'stats':{'hp':150,'mana':150,'power':100,'strength':15},
            'weapons':{'staff':0.3},
            'weaponattack':0.3
        } ,
        'goblin':{
            'stats':{'hp':50},
            'weapons':{'knife':0.4},
            'weaponattack':0.4
        },
        'skinwalker': {
            'stats':{'hp':70},
            'weapons':{'claws':0.6},
            'weaponattack':0.6
        },
         'beru': {
            'stats':{'hp':150, 'mana':150, 'power':100, 'strength':75},
            'weapons':{'claws':0.5},
            'weaponattack':0.5
        },
        'igris': {
            'stats':{'hp':175, 'mana':150, 'power':100, 'strength':70},
            'weapons':{'big sword':0.5},
            'weaponattack':0.5
        }
    }

    def __init__(self, character_type: str) -> None:
        self.stats = Stats(**Character.default_stats[character_type]['stats'])
        self.name = character_type.title()
    
    def __str__(self) -> str:
        return self.name
    
    def is_alive(self):
        return self.stats.hp > 0 

    def died(self):
        self.stats.hp = 0
        print("has died")
        
    def attack(self, target: 'Character'):
        target.stats.hp -= self.stats.strength


class Player(Character):
    
    def __init__(self, character_type: str) -> None:
        super().__init__(character_type)
    
    def is_critic(self) -> None:    
        return choices(population=[False,True], cum_weights=[.6, .6])
    
    def escape(self) -> None:
        return choices(population=[False,True], cum_weights=[.3, 1])
    
    def died(self):
        exit()

    # def drop(self) -> None:
    #     self.drop_item = choices(population=[0,1], cum_weights=[.3, 1])
    #     return print('Drop', self.drop_item, 'items')
        

class Items:
    items= 0

class Mage(Character):
    def attack(self, target: 'Character'):
        target.stats.hp -= self.stats.mana