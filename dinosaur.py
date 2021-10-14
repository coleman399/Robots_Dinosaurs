class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
<<<<<<< HEAD
=======

    # def set_stats(self):
    #     self.name = input("enter dinosaur name: ")
    #     print(f"dinosaur name set to: {self.name}")
    #     self.health = int(input("set dinosaur health: "))
    #     print(f"dinosaur health set to: {self.health}")
    #     self.attack_power = int(input("set dinosaur attack power: "))
    #     print(f"dinosaur attack power set to: {self.attack_power}")
>>>>>>> 405b29e4b4a504919d65ff39a272412ea2b309a9

    def dino_attack(self, robot_to_attack):
        robot_to_attack.health -= self.attack_power