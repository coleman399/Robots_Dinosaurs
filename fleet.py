class Fleet:
    def __init__(self):
        self.fleet_list = []
    
    def add_to_fleet(self, robot):
        self.fleet_list.append(robot)
        print(self.fleet_list)