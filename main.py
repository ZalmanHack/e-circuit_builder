import sys
import time

from ecircuit import *


def console():
    circuit = ECircuit(Mode.console)
    circuit.enterTable()
    circuit.build()
    circuit.show()
    table = circuit.getTable()
    circuit.minimize()
    table = circuit.getTable()
    for i in table:
        print(i)
    circuit.setTable(table)
    circuit.build()
    circuit.show()


def consoleWithGraphics():
    circuit = ECircuit(Mode.graphic)
    circuit.builder.enterTable()
    circuit.builder.build()
    circuit.show()


if __name__ == "__main__":



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
