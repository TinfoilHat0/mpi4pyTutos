#ex3.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
if size != 5:
    print "Error: This program must run with 5 processes"
    comm.Abort()
else:
    print "Succes!"    
