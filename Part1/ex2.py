#ex2.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank % 2 == 0:
    print "Hello ", rank, "of ", size
else:
    print "Goodbye", rank, "of", size
