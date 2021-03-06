#!/usr/bin/env python

from __future__ import print_function

import numpy as np
import scipy.linalg
import sys
import benchmark_decorator as dectimer

#----------------------
# Function: sqrt_matrix
#----------------------

if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]

@dectimer.bench_time(3, sys.argv[1], environment)
def sqrt_matrix(A):
    """
        Take the square root of matrix A
    """
    B = scipy.linalg.sqrtm(A)

n = int(sys.argv[1])

print('Square root of matrix: ', n)

A = np.ones((n, n))
for i in range(n):
    A[i, i] = 6

sqrt_matrix(A)

print(' ')
