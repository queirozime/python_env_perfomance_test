#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import sys
import benchmark_decorator as dectimer

if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]
@dectimer.bench_time(3, sys.argv[1], environment)
def belief_propagation(N):
    """
        Run the belief propagation algorithm N times
    """
    dim = 5000
    A = np.random.rand(dim, dim)
    x = np.ones((dim,))

    for i in range(N):
        x = np.log(np.dot(A, np.exp(x)))
        x -= np.log(np.sum(np.exp(x)))
    return x


if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' N')
    print('Please specify the number of iterations.')
    sys.exit()

N = int(sys.argv[1])

print('Belief calculations:', N)

y = belief_propagation(N)
