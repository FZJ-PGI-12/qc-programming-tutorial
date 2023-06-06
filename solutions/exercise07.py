
prob0 = 0.8
prob1 = 0.2
amp0 = np.sqrt(prob0)
amp1 = np.sqrt(prob1)
circuit.initialize([amp0, amp1], 0)
