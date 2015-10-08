#A basic implementaion of naive ER algorithm
#An example run with 3 processors and n = 3, p = 1.0
#mpiexec -n 3 python erdös-renyi.py 3 1.0

import numpy
import sys
from random import random
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#takes in command-line arguments [n, p]
n = int(sys.argv[1])
p = float(sys.argv[2])

#number of nodes that this process will process
nNodes = n/size
#starting node index for that particular process
low_index = nNodes*rank
#distribute remaining nodes(if any) to processes one by one
if n%size > rank:
    nNodes += 1
#if the previous processes has extra nodes, update low_index accordingly
if n%size > rank-1:
    low_index += rank
else:
    low_index += n%size
high_index = low_index + nNodes
#print(low_index, high_index)


#local edge_list
edge_list = []
#naive ER algorithm
for i in range(low_index, high_index):
    for j in range(i+1, n):
        r = random()
        if r < p:
            edge_list.append((i, j))
print(edge_list)
