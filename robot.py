from random import weibullvariate
from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.set_weapon()

    def set_weapon(self):
        self.weapon = Weapon(input(f"what weapon would you like {self.name} to use: "), int(input("using number keys, how much power does this weapon have? ")))

    def robo_attack(self, dino_to_attack):
        dino_to_attack.health -= self.weapon.attack_power
