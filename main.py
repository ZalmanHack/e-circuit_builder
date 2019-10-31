from ecircuit import *

if __name__ == "__main__":
    circuit = ECircuit()
    circuit.enterTable()

    circuit.build()
    circuit.resizeMatrix()
    circuit.show()