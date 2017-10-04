import numpy as np
import re

def generate(N) :
    """Generate the Cyclic Matrix multiplication Table
    
    :param N: Size
    :type N: int
    """
    G = np.atleast_2d(np.arange(1, N))
    return G * G.T % N



def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

def prime(n):
    return [x for x in range(n+1) if isprime(x)]