# create strucks for gates and Io for it to initilize

class Gates:
    gate_type = ""
    inputs = []
    output = -1

    def __init__(self, gate, Input, output):
        self.gate_type = gate
        self.inputs = Input
        self.output = output


class Circuit:
    gates = []
    ioList = {}
    outPut = []
    max_input = 1

    def __init__(self, gateList):
        self.gates = gateList


class Simulator:
    fileName = ""
    testVector = ""
    finalOutput = ""
    circuit = Circuit([])

    def __init__(self, filename="s27.txt", testVector="1010101"):
        self.max_input = 1
        self.fileName = filename
        self.testVector = testVector

    def Run(self):
        self.readNets()
        self.simulate_circuit()
        for i in self.circuit.outPut:
            self.finalOutput = self.finalOutput + str(self.circuit.ioList[str(i)])
        print("Input : " + self.testVector + "    Output : " + self.finalOutput)

    def readNets(self):
        logic_file = open(self.fileName)
        logic = logic_file.readlines()
        logic_file.close()
        self.parse_circuit(logic)


    def parse_circuit(self, logic):
        for line in logic:
            parse_line = line.split()
            gate = parse_line[0]
            if gate in ["INV", "BUF"]:
                self.circuit.gates.append(Gates(gate, [parse_line[1]], parse_line[2]))
                self.update_max_input([parse_line[1], parse_line[2]])
            elif gate in ["AND", "OR", "NAND", "NOR"]:
                self.circuit.gates.append(Gates(gate, [parse_line[1], parse_line[2]], parse_line[3]))
                self.update_max_input([parse_line[1], parse_line[2], parse_line[3]])
            elif gate in ["INPUT"]:
                parse_line.pop(0)
                parse_line.pop(len(parse_line) - 1)
                for i, io in enumerate(parse_line):
                    self.circuit.ioList[io] = int(self.testVector[i])
            else:
                parse_line.pop(0)
                parse_line.pop(len(parse_line) - 1)
                self.circuit.outPut = parse_line

        for i in range(1, self.max_input + 1):
            if str(i) not in self.circuit.ioList.keys():
                self.circuit.ioList[str(i)] = -1

    # Function to update max_input
    def update_max_input(self, values):
        max_val = max(map(int, values))
        if max_val > self.max_input:
            self.max_input = max_val

    def simulate_circuit(self):
        evaluate_gates = []
        while self.circuit.gates:
            self.find_ready_gates(evaluate_gates)
            self.evaluate_rady_gates(evaluate_gates)

    def evaluate_rady_gates(self, evaluate_gates):
        for gate in evaluate_gates:
            if gate.gate_type == "INV":
                self.circuit.ioList[gate.output] = int(not self.circuit.ioList[gate.inputs[0]])

            elif gate.gate_type == "BUF":
                self.circuit.ioList[gate.output] = int(self.circuit.ioList[gate.inputs[0]])

            elif gate.gate_type == "AND":
                self.circuit.ioList[gate.output] = int(
                    self.circuit.ioList[gate.inputs[0]] & self.circuit.ioList[gate.inputs[1]])

            elif gate.gate_type == "NAND":
                self.circuit.ioList[gate.output] = int(
                    not (self.circuit.ioList[gate.inputs[0]] and self.circuit.ioList[
                        gate.inputs[1]]))
            elif gate.gate_type == "NOR":
                self.circuit.ioList[gate.output] = int(
                    not (self.circuit.ioList[gate.inputs[0]] or self.circuit.ioList[
                        gate.inputs[1]]))
            elif gate.gate_type == "OR":
                self.circuit.ioList[gate.output] = int(self.circuit.ioList[gate.inputs[0]] or self.circuit.ioList[
                    gate.inputs[1]])

    def find_ready_gates(self, evaluate_gates):
        for gate in self.circuit.gates:
            evaluate = True
            for inputs in gate.inputs:
                if self.circuit.ioList[inputs] == -1:
                    evaluate = False
            if evaluate:
                evaluate_gates.append(gate)
                self.circuit.gates.remove(gate)
