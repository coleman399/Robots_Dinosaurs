from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.fleet()
    
<<<<<<< HEAD
    def fleet(self):
        terminator1 = Robot("Terminator XXLF001", 100)
        terminator2 = Robot("Terminator XXLF002", 100)
        terminator3 = Robot("Terminator XXLF003", 100)
        self.fleet_list.append(terminator1)
        self.fleet_list.append(terminator2)
        self.fleet_list.append(terminator3)
=======
    def add_to_fleet(self, robot):
        self.fleet_list.append(robot)
        print(self.fleet_list)
>>>>>>> 405b29e4b4a504919d65ff39a272412ea2b309a9
