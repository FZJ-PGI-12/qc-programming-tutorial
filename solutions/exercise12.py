circuit.barrier()
circuit.measure(Bobs_q, Bobs_c)

simulator = QasmSimulator()
job = simulator.run(circuit, shots=10000)
result = job.result()
counts = result.get_counts()
display(plot_histogram(counts))
