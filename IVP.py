import numpy as np


def f(y=None,t=None):
    return 0.5*t

def forward_euler(h, t0, y0, tf):
    while t0 < tf
        y0 = y0 + h*f(y0)
        y0 += h
    return y0

def rk2(h, t0, y0, tf):
    while t0 < tf:
        k1 = h * f(y0)
        k2 = h * f(y0+(2/3)*k1)
        y0 = y0 + (0.25*k1 + 0.75*k2)
    return y0

def rk4(h, t0, y0, tf):
    while t0 < tf:
        k1 = h * f(y0)
        k2 = h * f(y0 + 0.5*k1)
        k3 = h * f(y0 + 0.5*k2)
        k4 = h * f(y0 + k3)
        y0 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y0

def backward_euler(h, t0, y0, tf):
    while t0 < tf:
        y0 = y0 + h*f(y0, t0+h)
        t0 += h
    return y0

