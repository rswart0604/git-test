import numpy as np

def f(x):
    return np.square(x)-4*x-10

def g(x):
    return 2*x-4

def newton(x0):
    while f(x0) > 1e-3:
        x0 = x0 - g(x0)/f(x0)
    return x0

