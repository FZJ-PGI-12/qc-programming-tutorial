simulator = QasmSimulator()
for num_shots in [10, 100, 1000, 10000]:
    job = simulator.run(circuit, shots=num_shots)
    result = job.result()
    counts = result.get_counts()
    print('Num shots:', num_shots)
    display(plot_histogram(counts))
