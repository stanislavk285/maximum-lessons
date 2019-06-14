import random

class Tank:
    def __init__(self,name,armor,min_damage,max_damage,hp):
        self.armor=armor
        self.name=name
        self.min_damage=min_damage
        self.max_damage=max_damage
        self.hp=hp
    def run(self):
        print(self.name+" выдвигается...")
    def down_health(self,damage):
        if self.hp<=0:
            print("Танк {} уничтожен".format(self.name))
        else:
            self.hp=self.hp-damage
            print("У {} осталось {} очков здоровья".format(self.name,self.hp))
    def fire(self,enemy):
        damage=random.randint(self.min_damage,self.max_damage)
        enemy.down_health(damage)
        print("{} стреляет по {}".format(self.name, enemy.name))
    def __str__(self):
        return "{} имеет броню в {} мм, урон в диапазоне {}-{} очков и {} hp".format(
            self.name,self.armor,self.min_damage,self.max_damage,self.hp)       
tank1=Tank("T-34",100,15,60,300)
tank2=Tank("Tiger",150,20,80,450)
tank1.fire(tank2)



