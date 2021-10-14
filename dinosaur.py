class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.energy_level = 50
        self.attack_names = ("Bite", "Tailswipe", "Stomp")

    def dino_attack(self, robot_to_attack):
        robot_to_attack.health -= self.attack_power
        self.energy_level -= 10