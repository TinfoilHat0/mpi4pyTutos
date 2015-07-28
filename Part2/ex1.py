#mpiexec -n 2 python ex1.py 5
import numpy
import sys
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

n = int(sys.argv[1])
randNum = numpy.zeros(n)

if rank == 1:
    for i in range(0, n):
        randNum[i] = numpy.random.random_sample(1)
        print "Process", rank, "drew the number", randNum[i]
        comm.Send(randNum, dest=0)

if rank == 0:
    for i in range(0, n):
        print "Process", rank, "before receiving has the number", randNum[i]
        comm.Recv(randNum, source=1)
        print "Process", rank, "received the number", randNum[i]
