import Ship as s
import ShipData as sd


class Loader(object):
    """class for loading game data from text files"""

    @staticmethod
    def load_ship_data(shipdata):
        """loads the ship data defined in dane_statkow.txt"""
        f = open('./data/dane_statkow.txt')
        lines = f.readlines()[1:]
        for line in lines:
            shipdata.add_ship_data(line.strip().split(" "))

    @staticmethod
    def load_fast_attack_data(shipdata):
        """loads the ship fast attack data defined in dane_statkow.txt"""
        f = open('./data/szybkie_dziala.txt')
        lines = f.readlines()
        ship_names = lines[0].strip().split(" ")[1:]

        lines = lines[1:]
        for line in lines:
            line = line.strip().split(" ")
            shortname = line[0]
            line = line[1:]
            for i in range(len(line)):
                shipdata.add_fast_attack_data(shortname, ship_names[i], int(line[i]))

    @staticmethod
    def load_fleet(shipdata, fleetname):
        """loads the ship data defined in /data/{fleetname}/.txt"""
        f = open('./data/' + fleetname + '.txt')
        lines = f.readlines()
        lines = lines[1:]
        fleet = []
        for line in lines:
            line = line.split(' ')
            ship_type, count = line[0], int(line[1])
            for i in range(count):
                fleet.append(s.Ship(shipdata, ship_type))

        return fleet
