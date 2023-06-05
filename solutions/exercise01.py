# Create a Quantum Circuit acting on the 1 qubit register
circuit = QuantumCircuit(1)
# add hadamard gate
circuit.h(0)
# display the circuit
display(circuit.draw('mpl'))
