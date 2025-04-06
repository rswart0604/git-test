import numpy as np


def f(x):
    return np.square(x)

def g(x=None,t=None):
    return 2*x

def forward_euler(h, t0, y0, tf):
    while t0 < tf
        y0 = y0 + h*g(y0)
        y0 += h
    return y0



