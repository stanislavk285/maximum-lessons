import random
class Character:
    def __init__(self,name,hp,mana,min_damage,max_damage):
        self.name=name
        self.min_damage=min_damage
        self.max_damage=max_damage
        self.hp=hp
        self.mana=mana
    def fireball(self):
        self.mana=self.mana-30
        if self.mana>=0:
            damage=100+random.randint(self.min_damage,self.max_damage)
            print("{} использует заклинание fireball, нанося {} урона и теперь имеет {} маны".format(self.name,damage,self.mana))
        else:
            self.down_mana()
    def lightning(self):
        self.mana=self.mana-70
        if self.mana>=0:
            damage=150+random.randint(self.min_damage,self.max_damage)
            print("{} использует заклинание lightning, нанося {} урона и теперь имеет {} маны".format(self.name,damage,self.mana))
        else:
            self.down_mana()
    def ice_spike(self):
        self.mana=self.mana-50
        if self.mana>=0:
            damage=120+random.randint(self.min_damage,self.max_damage)
            print("{} использует заклинание lightning, нанося {} урона и теперь имеет {} маны".format(self.name,damage,self.mana))
        else:
            self.down_mana()
    def down_mana(self):
        if self.mana<=0:
            print("Недостаточно маны, используйте mana potion")
        if self.mana>100:
            print("Максимальный запас маны")
    def mana_potion(self):
        self.mana=self.mana+70
        if self.mana<=100:
            print("{} использовал mana potion и теперь имеет {} маны".format(self.name,self.mana))
        else:
            self.down_mana()
    def __str__(self):
        print("{} имеет {} очков здоровья и {} маны".format(
            self.name,self.hp,self.mana))
character=Character("Маг",300,100,50,80)
character.__str__()
character.fireball()
character.lightning()
character.mana_potion()
character.ice_spike()


