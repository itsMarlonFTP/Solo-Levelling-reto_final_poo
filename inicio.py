from random import choices
class Damage: 
    
    def critic(self) -> None:    
        self.is_critical: bool = choices(population=[False,True], cum_weights=[.6, 1])
    
    def escape(self) -> None:
        self.is_escape: bool = choices(population=[0,1], cum_weights=[.3, 1])

    def drop(self) -> None:
        self.drop_item = choices(population=[0,1], cum_weights=[.3, 1])
        return print('Drop', self.drop_item, 'items')


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
            'stats':{'hp':175, 'mana':150, 'power':100, 'strength':60},
            'weapons':{'big sword':0.5},
            'weaponattack':0.5
        }
    }

    def __init__(self, character_type: str) -> None:
        self.stats = Stats(**Character.default_stats[character_type]['stats'])
    
    def is_alive(self):
        return self.stats.hp > 0 

    def died(self):
        self.stats.hp = 0
        print("has died")
        

class Items:
    items= 0
