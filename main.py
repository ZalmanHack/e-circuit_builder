from ecircuit import *

if __name__ == "__main__":
    circuit = ECircuit()
    circuit.enterTable()
    print(circuit.getTable())
    print(circuit.getMatrix())

    circuit.build()
    print(circuit.getMatrix())
    circuit.show()