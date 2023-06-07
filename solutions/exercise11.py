# define function to print statevector from circuit
def get_statevector(circuit):
    simulator = StatevectorSimulator()
    job = simulator.run(circuit)
    result = job.result()
    statevector = result.get_statevector()
    return statevector

# prepare circuit (exercise 06)
Alices_q = QuantumRegister(2, name='alice')
Bobs_q = QuantumRegister(1, name='bob')
Alices_c = ClassicalRegister(2, name='alice-c')
Bobs_c = ClassicalRegister(1, name='bob-c')
circuit = QuantumCircuit(Alices_q, Bobs_q, Alices_c, Bobs_c)
print("After: Prepare circuit")
display(get_statevector(circuit).draw(output='latex'))

# initialize (exercise 07)
prob0 = 0.8
prob1 = 0.2
amp0 = np.sqrt(prob0)
amp1 = np.sqrt(prob1)
circuit.initialize([amp0, amp1], 0)
print("After: Initialize")
display(get_statevector(circuit).draw(output='latex'))

# entangle A and B (exercise 08)
circuit.h(Alices_q[1])
circuit.cx(Alices_q[1], Bobs_q[0])
print("After: Entanglement between A and B")
display(get_statevector(circuit).draw(output='latex'))

# entangle both of A's qubits (exercise 09, first part)
circuit.barrier()
circuit.cx(Alices_q[0], Alices_q[1])
circuit.h(Alices_q[0])
print("After: Entanglement in A")
display(get_statevector(circuit).draw(output='latex'))

# measure both of A's qubits (exercise 09, first part)
circuit.barrier()
circuit.barrier()
circuit.measure(Alices_q[0], Alices_c[0])
print("After: After first measurement")
display(get_statevector(circuit).draw(output='latex'))
circuit.measure(Alices_q[1], Alices_c[1])
print("After: After second measurement")
display(get_statevector(circuit).draw(output='latex'))

# apply B's corrections (exercise 10)
circuit.barrier()
circuit.x(Bobs_q).c_if(Alices_c[1], 1)
circuit.z(Bobs_q).c_if(Alices_c[0], 1)
print("After: After B's corrections")
display(get_statevector(circuit).draw(output='latex'))
