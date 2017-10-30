

from ShipData import ShipData
from Loader import Loader

sd = ShipData()
Loader.load_ship_data(sd)
Loader.load_fast_attack_data(sd)
f1 = Loader.load_fleet("flota_1.txt")
f2 = Loader.load_fleet("flota_2.txt")


import pdb; pdb.set_trace()
