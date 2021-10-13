from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.weapon = None
        self.attack_power = 0

    def set_stats(self):
        self.name = input("enter robot name: ")
        print(f"robot name set to: {self.name}")
        self.health = int(input("set robot health: "))
        print(f"robot health set to: {self.health}")
        self.attack_power = int(input("set robot attack power: "))
        print(f"robot attack power set to: {self.attack_power}")

    def weapon_choice(self, type, name, attack_power):
        self.weapon = Weapon(type, name, attack_power)

    def robo_attack(self, dino_to_attack):
        dino_to_attack.health -= self.weapon.attack_power