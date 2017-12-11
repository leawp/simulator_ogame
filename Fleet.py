from Loader import Loader
from ShipData import ATTACK, ATTACK_FACTORS, HEALTH, LONG_NAME, SHIELD
import numpy as np
from random import random
from pprint import pprint


class Fleet(object):
    """class containing basic fleet operations and game related functions
    """

    def __init__(self, sd, name):
        """assings the fleet name to the object and loads the fleet data based on the fleet name"""
        super(Fleet, self).__init__()
        self.name = name
        self.fleet = Loader.load_fleet(sd, name)

    def get_random_target(self):
        """chooses a random target based on uniform distribution random value"""
        return self.fleet[np.random.randint(0, len(self.fleet))]

    def attack(self, other):
        """sequenially executes the attack function for each ship on the fleet list"""
        for s in self.fleet:
            s.do_attack(other)


    def evaluate_fleet(self):
        """decides to remove or keep sheeps in the fleet, regenerates shields"""
        ships_to_remove = []
        for i in range(len(self.fleet)):
            if self.fleet[i].health <= 0:
                ships_to_remove.append(i)
            else:
                self.fleet[i].shield = self.fleet[i].data[SHIELD]


        self.fleet = np.delete(self.fleet, ships_to_remove)
        return self.name + " - straty: " + str(len(ships_to_remove))

    def print_fleet(self):
        """prints the fleet nicely"""
        pprint(self.fleet)
