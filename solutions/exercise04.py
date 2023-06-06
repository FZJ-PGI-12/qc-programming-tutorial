num_steps = 10
for index in range(0, num_steps + 1):
    angle = index * np.pi/float(num_steps)
    # Create a Quantum Circuit acting on the 1 qubit register
    circuit = QuantumCircuit(1)
    # add hadamard gate
    circuit.rx(angle, 0)

    # run the circuit
    simulator = StatevectorSimulator()
    job = simulator.run(circuit)
    result = job.result()
    statevector = result.get_statevector()

    # display statevector after each rotation
    print('Angle=', index, '* pi /', num_steps)
    display(statevector.draw(output='bloch'))
