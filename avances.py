class Stats:
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
        self.strength=50