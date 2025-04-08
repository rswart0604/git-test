import numpy as np

def f(x):
    return np.square(x) - 7.0*x + 12.0

def g(x):
    return 2.0*x - 7.0

def newton(x0):
    while np.abs(f(x0)) > 1e-6:
        x0 = x0 - f(x0)/g(x0)
    return x0

x0 = 5.0
print(f'{newton(x0)}')
print('Real root is 4')
