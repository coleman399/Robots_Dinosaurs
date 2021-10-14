from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.fleet()
    
    def fleet(self):
        terminator1 = Robot("Terminator XXLF001", 100)
        terminator2 = Robot("Terminator XXLF002", 100)
        terminator3 = Robot("Terminator XXLF003", 100)
        self.fleet_list.append(terminator1)
        self.fleet_list.append(terminator2)
        self.fleet_list.append(terminator3)