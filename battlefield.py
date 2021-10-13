import random
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dead_robots = []
        self.dead_dinosaurs = []
    
    def run_game(self):
        print("--- Begin Battle ---")
        print(self.herd.herd_list[0].name)
        # self.battle()
        # self.dino_turn()
        # self.robot_turn()
        # self.dino_attack()
        # self.robo_attack()
        # self.display_winners()

# fleet.name? for every variable in the list? there isn't a better way?

    def battle(self):
        for robots in self.import_fleet.fleet_list:
            self.fleet.append(robots.name)
            print(f"{robots.name} added to fleet.")
        for dinos in self.import_herd.herd_list:
            self.herd.append(dinos.name)
            print(f"{dinos.name} added to herd.")

    def dino_turn(self):
        self.fighting_dino.dino_attack(self.fighting_robot)
        print(f"{self.fighting_dino.name} hits {self.fighting_robot.name} for {self.fighting_dino.attack_power} points.")

    def robot_turn(self):
        self.fighting_robot.robo_attack(self.fighting_dino)
        print(f"{self.fighting_robot.name} hits {self.fighting_dino.name} for {self.fighting_robot.weapon.attack_power} points.")

    def dino_attack(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            self.dino_turn()
        if self.fighting_robot.health <= 0:
            self.fleet.remove(self.fighting_robot)
            self.battle()
        if self.fighting_dino.health <= 0:
            self.herd.remove(self.fighting_dino)
            self.battle()

    def robo_attack(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            self.robot_turn()
        if self.fighting_robot.health <= 0:
            self.fleet.remove(self.fighting_robot)
            self.battle()
        if self.fighting_dino.health <= 0:
            self.remove(self.fighting_dino)
            self.battle()

    def display_winner(self):
        if self.fleet == 0:
            print("The dinosaurs defeated the robots!")
        if self == 0:
            print("The robots defeated the dinosaurs!")
