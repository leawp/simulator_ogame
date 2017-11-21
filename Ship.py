from ShipData import ATTACK, ATTACK_FACTORS, HEALTH, LONG_NAME, SHIELD
from random import random


class Ship(object):
    """Main ship class for all ingame ship types"""

    def __init__(self, shipdata, shortname):
        super(Ship, self).__init__()
        self.data = shipdata.get_data(shortname)
        self.shortname = shortname
        self.longname = self.data[LONG_NAME]
        self.health = self.data[HEALTH]
        self.shield = self.data[SHIELD]
        self.attack = self.data[ATTACK]

    def __str__(self):
        return self.longname + "\t " + str(self.health) + "\t " + str(self.shield) + "\t " + str(self.attack)

    def get_attack_chance(self, target_shortname):
        return 1 - 1.0 / self.data[ATTACK_FACTORS][target_shortname]

    def do_attack(self, target):

        while(True):
            if target.shield > 0:
                target.shield -= self.attack
                if target.shield < 0:
                    target.health += target.shield
                    target.shield = 0

            elif target.shield == 0:
                target.health -= self.attack

            if self.get_attack_chance(target.shortname) > random():
                continue
            break
