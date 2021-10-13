class Robot:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.weapon = ""
        self.attack_power = 0

    def set_stats(self):
        self.name = input("enter robot name: ")
        print(f"robot name set to: {self.name}")
        self.health = int(input("set robot health: "))
        print(f"robot health set to: {self.health}")
        self.weapon = input("what weapon is the robot using: ")
        print(f"robot weapon set to: {self.weapon}")
        self.attack_power = int(input("set robot attack power: "))
        print(f"robot attack power set to: {self.attack_power}")
