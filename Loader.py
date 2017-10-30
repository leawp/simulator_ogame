
class Loader(object):
    """class for loading game data from text files"""

    def __init__(self):
        super(Loader, self).__init__()

    @staticmethod
    def load_ship_data(shipdata):
        f = open('./data/dane_statkow.txt')
        lines = f.readlines()[1:]
        for line in lines:
            shipdata.add_ship_data(line.split(" "))

    @staticmethod
    def load_fast_attack_data(shipdata):
        f = open('./data/szybkie_dziala.txt')
        lines = f.readlines()
        ship_names = lines[0].split(" ")[1:]

        lines = lines[1:]
        for line in lines:
            line = line.split(" ")
            shortname = line[0]
            line = line[1:]
            for i in range(len(line)):
                shipdata.add_fast_attack_data(shortname, ship_names[i], int(line[i]))

    @staticmethod
    def load_fleet(fleetname):
        pass
