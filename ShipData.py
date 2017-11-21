LONG_NAME = 0
HEALTH = 1
SHIELD = 2
ATTACK = 3
ATTACK_FACTORS = 4

class ShipData(object):
    """class containing ship info"""

    def __init__(self):
        super(ShipData, self).__init__()
        self.ships = {}

    def add_ship_data(self, data):
        shortname, longname, health, shield, attack = data
        if not shortname in self.ships:
            self.ships[shortname] = (longname, int(health), int(shield), int(attack), {})
        else:
            Exception("Tried to add the same ship twice!")

    def add_fast_attack_data(self, shortname, enemy, factor):
        if shortname in self.ships:
            self.ships[shortname][ATTACK_FACTORS][enemy] = factor
        else:
            Exception("Ship does not exist in the ship data table!")

    def get_data(self, shortname):
        if shortname in self.ships:
            return self.ships[shortname]
        return None
