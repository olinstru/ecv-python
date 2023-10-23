import random
from rich import print
from dice import Dice
from character import Character, Mage, Warrior, Thief

from rich.pretty import pprint


def main():
    warrior = Warrior("Tom", 20, 8, 3, Dice(6))
    mage = Mage("Helen", 20, 8, 3, Dice(6))
    thief = Thief("Jean", 20, 8, 3, Dice(6))
    farmer = Character("Bernard", 20, 8, 3, Dice(6))

    cars = [warrior, mage, thief, farmer]
    stats = {}

    car1: Character = random.choice(cars)
    cars.remove(car1)
    car2: Character = random.choice(cars)
    cars.remove(car2)
    
    print(car1)
    print(car2)
    
    stats[car1.get_name()] = 0
    stats[car2.get_name()] = 0
    
    print(stats)
    
    for i in range(100):
        car1.regenerate()
        car2.regenerate()
        while (car1.is_alive()) and (car2.is_alive()):
            car1.attack(car2)
            car2.attack(car1)
        if (car1.is_alive()):
            stats[car1.get_name()] += 1
        else:
            stats[car2.get_name()] += 1
    
    print(stats)


if __name__ == "__main__":
    main()
