class Character:

    def __init__(self, name, strenght, inteligence, defense, hp):
        self.name = name
        self.strenght = strenght
        self.inteligence = inteligence
        self.defense = defense
        self.hp = hp
    
    def attributes(self):
        print(self.name, ":", sep="")
        print("·strenght:", self.strenght)
        print("·Inteligencia:", self.inteligence)
        print("·defense:", self.defense)
        print("·hp:", self.hp)

    def level_up(self, strenght, inteligence, defense):
        self.strenght = self.strenght + strenght
        self.inteligence = self.inteligence + inteligence
        self.defense = self.defense + defense

    def is_alive(self):
        return self.hp > 0

    def died(self):
        self.hp = 0
        print(self.name, "has died")

    def damage(self, enemy):
        if self.strenght > enemy.defense:
            return self.strenght - enemy.defense
        else:
            return 0

    def attack(self, enemy):
        damage = self.damage(enemy)
        if damage > 0:
            enemy.hp = enemy.hp - damage
            print(self.name, "has done", damage, "damage point to", enemy.name)
            if enemy.is_alive():
                print("The hp of", enemy.name, "is", enemy.hp)
            else:
                enemy.died()
        else:
            print(self.name, "has done", self.strenght, "damage points to the armor of", enemy.name)
            enemy.defense = enemy.defense - self.strenght
            print("The armor of", enemy.name, "is", enemy.defense)

class Warrior(Character):
    
    def __init__(self, name, strenght, inteligence, defense, hp, sword):
        super().__init__(name, strenght, inteligence, defense, hp)
        self.sword = sword

    def change_weapon(self):
        option = int(input("Elige un arma: (1) Acero Valyrio, damage 8. (2) Matadragones, damage 10"))
        if option == 1:
            self.sword = 8
        elif option == 2:
            self.sword = 10
        else:
            print("Número de arma incorrecta")

    def attributes(self):
        super().attributes()
        print("·sword:", self.sword)

    def damage(self, enemy):
        return self.strenght*self.sword - enemy.defense

class Mage(Character):

    def __init__(self, name, strenght, inteligence, defense, hp, book):
        super().__init__(name, strenght, inteligence, defense, hp)
        self.book = book

    def attributes(self):
        super().attributes()
        print("·book:", self.book)

    def damage(self, enemy):
        if self.inteligence*self.book > enemy.defense:
            return self.inteligence*self.book - enemy.defense
        else:
            return 0

    def attack(self, enemy):
        damage = self.damage(enemy)
        if damage > 0:
            enemy.hp = enemy.hp - damage
            print(self.name, "has done", damage, "damage point to", enemy.name)
            if enemy.is_alive():
                print("The hp of", enemy.name, "is", enemy.hp)
            else:
                enemy.died()
        else:
            print(self.name, "has done", self.inteligence*self.book, "damage points to the armor of", enemy.name)
            enemy.defense = enemy.defense - self.inteligence*self.book
            print("The armor of", enemy.name, "is", enemy.defense)

def combat(player_1, player_2):
    turn = 1
    while player_1.is_alive() and player_2.is_alive():
        print("\nturn", turn)
        print(">>> Action from ", player_1.name,":", sep="")
        player_1.attack(player_2)
        if player_2.hp == 0:
            break
        print(">>> Action from ", player_2.name,":", sep="")
        if player_1.hp == 0:
            break
        player_2.attack(player_1)
        turn = turn + 1
    if player_1.is_alive():
        print("\n" + player_1.name, "won")
    elif player_2.is_alive():
        print("\n" + player_2.name, "won")
    else:
        print("\nIt's a tie")

Character_1 = Warrior("Guts", 20, 10, 4, 100, 4)
Character_2 = Mage("Vanessa", 5, 15, 4, 100, 4)

Character_1.attributes()
Character_2.attributes()      

combat(Character_1, Character_2)