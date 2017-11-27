

from ShipData import ShipData
from Ship import Ship
from Loader import Loader
from Fleet import Fleet
from appJar import gui

app = gui("Ogame Simulator GUI", "1200x600")

sd = ShipData()
Loader.load_ship_data(sd)
Loader.load_fast_attack_data(sd)
f1 = Fleet(sd, "flota_1")
f2 = Fleet(sd, "flota_2")
TYPY = ["mt", "dt", "lm", "cm", "kr", "ow", "sk", "re", "ss", "b", "n", "gs", "p"]


def load_ship_data(xd):
    global sd
    sd = ShipData()
    Loader.load_ship_data(sd)
    Loader.load_fast_attack_data(sd)
    global f1
    for typ in TYPY:
        app.setEntry(typ + "1", 0)
        app.setEntry(typ + "2", 0)

    f1 = Fleet(sd, "flota_1")
    for ship in f1.fleet:
        vstr = app.getEntry(ship.shortname + "1")
        v = int(0 if vstr == '' else vstr)
        app.setEntry(ship.shortname + "1", v + 1)
    global f2
    f2 = Fleet(sd, "flota_2")
    for ship in f2.fleet:
        vstr = app.getEntry(ship.shortname + "2")
        v = int(0 if vstr == '' else vstr)
        app.setEntry(ship.shortname + "2", v + 1)
    app.clearAllTextAreas()


def load_ship_data_from_fields(xd):
        global f1
        global f2
        global sd

        f1.fleet = []
        f2.fleet = []
        for typ in TYPY:
            v1 = int(app.getEntry(typ + "1"))
            for i in range(v1):
                f1.fleet.append(Ship(sd, typ))
            v2 = int(app.getEntry(typ + "2"))
            for i in range(v2):
                f2.fleet.append(Ship(sd, typ))


def run_sim(xd):
    app.clearAllTextAreas()
    output = ""

    for i in range(int(app.getSpinBox("Dlugosc rundy"))):
        if len(f1.fleet) == 0 or len(f2.fleet) == 0:
            break

        output += "\nRUNDA " + str(i + 1) + "\n"
        f1.attack(f2)
        f2.attack(f1)
        output += f1.evaluate_fleet() + "\n"
        output += f2.evaluate_fleet() + "\n"
        output += "\n-----------KONIEC RUNDY-----------"

    output += "\nKONIEC GRY"
    if len(f1.fleet) == 0:
        output += "\nZWYCIESTWO " + f2.name
    elif len(f2.fleet) == 0:
        output += "\nZWYCIESTWO " + f1.name
    else:
        output += "\nREMIS"
        # f1.print_fleet()
        # f2.print_fleet()
    app.setTextArea("output", output)


wiersz = 0
kolumna1 = 0
kolumna2 = 0
app.startPanedFrame("floty1")
app.addLabel("label1", "Flota 1", wiersz, kolumna1)
app.addLabelEntry("mt1")
app.addLabelEntry("dt1")
app.addLabelEntry("lm1")
app.addLabelEntry("cm1")
app.addLabelEntry("kr1")
app.addLabelEntry("ow1")
app.addLabelEntry("sk1")
app.addLabelEntry("re1")
app.addLabelEntry("ss1")
app.addLabelEntry("b1")
app.addLabelEntry("n1")
app.addLabelEntry("gs1")
app.addLabelEntry("p1")

app.startPanedFrame("floty2")
app.addLabel("label2", "Flota 2", wiersz, kolumna2)
app.addLabelEntry("mt2")
app.addLabelEntry("dt2")
app.addLabelEntry("lm2")
app.addLabelEntry("cm2")
app.addLabelEntry("kr2")
app.addLabelEntry("ow2")
app.addLabelEntry("sk2")
app.addLabelEntry("re2")
app.addLabelEntry("ss2")
app.addLabelEntry("b2")
app.addLabelEntry("n2")
app.addLabelEntry("gs2")
app.addLabelEntry("p2")
app.stopPanedFrame()

app.startPanedFrame("p1")
app.setStretch("none")
app.addLabel("Ustawienia", "Ustawienia")

app.addLabelEntry("flota_1")
app.setEntry("flota_1", "flota_1")

app.addLabelEntry("flota_2")
app.setEntry("flota_2", "flota_2")

app.addLabelSpinBoxRange("Dlugosc rundy", 1, 10)
app.setSpinBox("Dlugosc rundy", 6)
app.stopPanedFrame()

# start additional panes inside initial pane
app.startPanedFrame("p2")
app.addLabel("l2", "Akcje")
app.addButton("Load ship data from file", load_ship_data)
app.addButton("Load ship data", load_ship_data_from_fields)
app.addButton("Run simulation", run_sim)
app.addButton("Exit", app.stop)
app.stopPanedFrame()

app.startPanedFrame("p3")
app.addScrolledTextArea("output")

app.stopPanedFrame()

# stop initial pane
app.stopPanedFrame()

app.go()
