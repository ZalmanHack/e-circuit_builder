import sys
import time

from ecircuit import *


def console():
    circuit = ECircuit(Mode.console)
    circuit.enterTable()
    circuit.build()
    circuit.show()
    table = circuit.getTable()
    for i in table:
        print(i)
    print("-----------------")
    circuit.minimize()
    table = circuit.getTable()
    for i in table:
        print(i)
    print("-----------------")
    circuit.setTable(table)
    circuit.build(add_knots=False)
    circuit.show()


def consoleWithGraphics():
    circuit = ECircuit(Mode.graphic)
    circuit.builder.enterTable()
    circuit.builder.build()
    circuit.show()


if __name__ == "__main__":

    j = [0,1,2,3]
    print(j[2:-1])

    if len(sys.argv) == 1:
        print("---------- Консольный режим ----------")
        console()
        input("Для продолжения, нажмите любую клавишу...")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-G":
            print("---------- Консольный режим + графический вывод ----------")
            consoleWithGraphics()
            input("Для продолжения, нажмите любую клавишу...")
    else:
        print("Ошибка. Слишком много параметров.")
        time.sleep(5)
        sys.exit(1)
