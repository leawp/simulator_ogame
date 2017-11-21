

from ShipData import ShipData
from Loader import Loader
from Fleet import Fleet

sd = ShipData()
Loader.load_ship_data(sd)
Loader.load_fast_attack_data(sd)
f1 = Fleet(sd, "flota_1")
f2 = Fleet(sd, "flota_2")


for i in range(6):
    if len(f1.fleet) == 0 or len(f2.fleet) == 0:
        break

    print("RUNDA " + str(i + 1))
    f1.attack(f2)
    f2.attack(f1)
    f1.evaluate_fleet()
    f2.evaluate_fleet()
    print("-----------KONIEC RUNDY-----------")

if len(f1.fleet) == 0:
    print("ZWYCIESTWO " + f2.name)
elif len(f2.fleet) == 0:
    print("ZWYCIESTWO " + f1.name)
else:
    print("REMIS")
    f1.print_fleet()
    f2.print_fleet()
