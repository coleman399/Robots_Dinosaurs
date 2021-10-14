from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack_power = 25
        self.power_level = 50
        self.weapon_names = ["laser cannon", "plasma rifle", "lightsaber"]
        self.set_weapon()

    def set_weapon(self):
        loop = True
        while loop is True:
            answer = input(f"do you want {self.name} to have a weapon(y/n)? ")
            if answer == "y":
                self.users_input = input(f"using the number keys, what weapon would you like {self.name} to use: {self.weapon_names[0]}, {self.weapon_names[1]}, or {self.weapon_names[2]}\n")
                while loop is True:
                    if self.users_input == "1":
                        self.weapon = Weapon(self.weapon_names[0], 50)
                        self.attack_power = 50
                        loop = False
                        continue
                    elif self.users_input == "2":
                        self.weapon = Weapon(self.weapon_names[1], 30)
                        self.attack_power = 30
                        loop = False
                        continue
                    elif self.users_input == "3":
                        self.weapon = Weapon(self.weapon_names[2], 100)
                        self.attack_power = 100
                        loop = False
                        continue
                    else:
                        print("please use the '1', '2', or '3' keys to make a selection")
            elif answer == "n":
                loop = False
                continue
            else:
                print("please use the 'y' or 'n' keys to make a selection.")

    def robo_attack(self, dino_to_attack):
        dino_to_attack.health -= self.attack_power
        self.power_level -= 10
