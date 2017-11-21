

from ShipData import ShipData
from Loader import Loader
from Fleet import Fleet
from appJar import gui

app = gui("Ogame Simulator GUI", "900x600")

sd = ShipData()
Loader.load_ship_data(sd)
Loader.load_fast_attack_data(sd)
f1 = Fleet(sd, "flota_1")
f2 = Fleet(sd, "flota_2")


def load_ship_data(xd):
    global sd
    sd = ShipData()
    Loader.load_ship_data(sd)
    Loader.load_fast_attack_data(sd)
    global f1
    f1 = Fleet(sd, "flota_1")
    global f2
    f2 = Fleet(sd, "flota_2")
    app.clearAllTextAreas()


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


app.startPanedFrame("p1")
app.setStretch("none")
app.addLabel("Ustawienia", "Ustawienia")

app.addLabelEntry("flota_1")
app.setEntry("flota_1", "flota_1")

app.addLabelEntry("flota_2")
app.setEntry("flota_2", "flota_2")

app.addLabelSpinBoxRange("Dlugosc rundy", 1, 10)
app.setSpinBox("Dlugosc rundy", 6)


# start additional panes inside initial pane
app.startPanedFrame("p2")
app.addLabel("l2", "Akcje")
app.addButton("Load ship data", load_ship_data)
app.addButton("Run simulation", run_sim)
app.addButton("Exit", app.stop)
app.stopPanedFrame()

app.startPanedFrame("p3")
app.addScrolledTextArea("output")

app.stopPanedFrame()

# stop initial pane
app.stopPanedFrame()

app.go()
