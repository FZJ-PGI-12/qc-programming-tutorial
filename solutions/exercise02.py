# Create a Quantum Circuit acting on the 1 qubit register
circuit = QuantumCircuit(2)
# add hadamard gate
circuit.h(0)
circuit.cnot(0, 1)
# display the circuit
display(circuit.draw('mpl'))
