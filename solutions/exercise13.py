thetas = ParameterVector('theta', num_qubits)
for i in range(num_qubits):
    ansatz.h(i)
    ansatz.ry(thetas[i], i)
for i in range(num_qubits):
    ansatz.cx(i, (i + 1) % num_qubits)
