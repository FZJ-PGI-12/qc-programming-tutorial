circuit.barrier()
circuit.cx(Alices_q[0], Alices_q[1])
circuit.h(Alices_q[0])
circuit.barrier()
circuit.measure(Alices_q[0], Alices_c[0])
circuit.measure(Alices_q[1], Alices_c[1])

