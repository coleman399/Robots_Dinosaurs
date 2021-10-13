from battlefield import Battlefield
# from fleet import Fleet
# from herd import Herd

# fleet = Fleet()
# herd = Herd()

# dinosaur1 = Dinosaur()
# dinosaur2 = Dinosaur()
# dinosaur3 = Dinosaur()

# dinosaur1.set_stats()
# dinosaur2.set_stats()
# dinosaur3.set_stats()

# robot1 = Robot()
# robot2 = Robot()
# robot3 = Robot()

# robot1.set_stats()
# robot2.set_stats()
# robot3.set_stats()

# loop = True

# while loop is True:
#     answer = input("do you want robots to have weapons(y/n)? ")
#     if answer == "y":
#         robot1.weapon_choice(True, input(f"name {robot1.name}'s weapon: "), int(input("set weapon attack power: ")))
#         robot2.weapon_choice(True, input(f"name {robot2.name}'s weapon: "), int(input("set weapon attack power: ")))
#         robot3.weapon_choice(True, input(f"name {robot3.name}'s weapon: "), int(input("set weapon attack power: ")))
#         loop = False
#         continue
#     elif answer == "n":
#         loop = False
#         continue
#     else:
#         print("please use the 'y' or 'n' keys to make a selection.")

# fleet.add_to_fleet(robot1)
# fleet.add_to_fleet(robot2)
# fleet.add_to_fleet(robot3)

# herd.add_to_herd(dinosaur1)
# herd.add_to_herd(dinosaur2)
# herd.add_to_herd(dinosaur3)

battlefield = Battlefield()
battlefield.run_game()
