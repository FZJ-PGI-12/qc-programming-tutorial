circuit.barrier()
circuit.x(Bobs_q).c_if(Alices_c[1], 1)
circuit.z(Bobs_q).c_if(Alices_c[0], 1)
