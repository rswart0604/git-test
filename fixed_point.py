import numpy as np

def f(x):
    return np.square(x) - 7*x + 12

def g(x):
    return np.sqrt(7*x - 12)

def fixed_point(x0):
    while np.abs(f(x0)) > 1e-6:
        x0 = g(x0)
    return x0

x0 = 4.6
print(f"{fixed_point(x0)}")
print(f"Real root is 4")
