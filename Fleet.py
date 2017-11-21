from Loader import Loader
from ShipData import ATTACK, ATTACK_FACTORS, HEALTH, LONG_NAME, SHIELD
import numpy as np


class Fleet(object):
    """docstring for Fleet."""

    def __init__(self, sd, name):
        super(Fleet, self).__init__()
        self.name = name
        self.fleet = Loader.load_fleet(sd, name)

    def get_random_target(self):
        return self.fleet[np.random.randint(0, len(self.fleet))]

    def attack(self, other):
        for s in self.fleet:
            target = other.get_random_target()
            s.do_attack(target)


    def evaluate_fleet(self):
        ships_to_remove = []
        for i in range(len(self.fleet)):
            if self.fleet[i].health <= 0:
                ships_to_remove.append(i)
            else:
                self.fleet[i].shield = self.fleet[i].data[SHIELD]

        # for i in ships_to_remove:
            # print(str(self.fleet[i]) + " has died!")
        print(self.name + " - straty: " + str(len(ships_to_remove)))
        self.fleet = np.delete(self.fleet, ships_to_remove)

    def print_fleet(self):
        for s in self.fleet:
            print(s)
