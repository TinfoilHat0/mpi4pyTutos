#mpiexec -n 5 python ex3.py
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

randNum = numpy.random.random_sample(1)
print "Process: ", rank, "generated: ", randNum
comm.Send(randNum, dest = (rank+1)%size)
print "Process: ", rank, "sent: ", randNum
comm.Recv(randNum, source = (rank-1)%size)
print "Process: ", rank, "received: ", randNum
