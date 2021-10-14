import random
import sys
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        print("--- Begin Battle ---")
        self.battle()
        self.dino_turn()
        self.robot_turn()
        self.dino_attack()
        self.robo_attack()
        if len(self.fleet.fleet_list) == 0:
            self.display_winner()
        elif len(self.herd.herd_list) == 0:
            self.display_winner()
        else:
            self.run_game()
    
    def battle(self):
        self.fighting_robot = random.choices(self.fleet.fleet_list)[0]
        self.fighting_dino = random.choices(self.herd.herd_list)[0]

    def dino_turn(self):
        self.fighting_dino.dino_attack(self.fighting_robot)
        print(f"{self.fighting_dino.name} hits {self.fighting_robot.name} for {self.fighting_dino.attack_power} points while using {random.choice(self.fighting_dino.attack_names)}.") 
        print(f"{self.fighting_dino.name} has {self.fighting_dino.energy_level} energy left.")

    def robot_turn(self):
        self.fighting_robot.robo_attack(self.fighting_dino)
        print(f"{self.fighting_robot.name} hits {self.fighting_dino.name} for {self.fighting_robot.attack_power} points.")
        print(f"{self.fighting_robot.name} has {self.fighting_robot.power_level} power left.")

    def dino_attack(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            self.dino_turn()
        if self.fighting_robot.health <= 0:
            self.fleet.fleet_list.remove(self.fighting_robot)
            print(f"{self.fighting_robot.name} has been defeated.")
            if len(self.fleet.fleet_list) == 0:
                self.display_winner()
            else:
                self.battle()
        if self.fighting_dino.health <= 0:
            self.herd.herd_list.remove(self.fighting_dino)
            print(f"{self.fighting_dino.name} has been defeated.")
            if len(self.herd.herd_list) == 0:
                self.display_winner()
            else:
                self.battle()

    def robo_attack(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            self.robot_turn()
        if self.fighting_robot.health <= 0:
            self.fleet.fleet_list.remove(self.fighting_robot)
            print(f"{self.fighting_robot.name} has been defeated.")
            if len(self.fleet.fleet_list) == 0:
                self.display_winner()
            else:
                self.battle()
        if self.fighting_dino.health <= 0:
            self.herd.herd_list.remove(self.fighting_dino)
            print(f"{self.fighting_dino.name} has been defeated.")
            if len(self.herd.herd_list) == 0:
                self.display_winner()
            else:
                self.battle()

    def display_winner(self):
        if len(self.fleet.fleet_list) == 0:
            print("The dinosaurs defeated the robots!")
            sys.exit()
        else:
            print("The robots defeated the dinosaurs!")
            sys.exit()
