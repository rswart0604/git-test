import numpy as np

def f(x):
    return np.square(x) - 4*x - 3

def g(x):
    return np.sqrt(4*x+3)

def fixed_point(x0):
    while f(x0) > 1e-3:
        x0 = g(x0)
    return x0

