from dinosaur import Dinosaur

<<<<<<< HEAD
class Herd:
    def __init__(self):
        self.herd_list = []
        self.herd()
    
    def herd(self):
        trex = Dinosaur("T-Rex", 100, 25)
=======

class Herd:
    def __init__(self):
        self.herd_list = []
        self.add_to_herd()
    
    def add_to_herd(self):
        trex = Dinosaur("Trex", 100, 25)
>>>>>>> 405b29e4b4a504919d65ff39a272412ea2b309a9
        velociraptor = Dinosaur("Velociraptor", 100, 25)
        triceratops = Dinosaur("Triceratops", 100, 25)
        self.herd_list.append(trex)
        self.herd_list.append(velociraptor)
        self.herd_list.append(triceratops)