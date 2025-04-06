import numpy as np
import matplotlib.pyplot as plt

def f(y=None,t=None):
    return 0.5*t

def forward_euler(h, t0, y0, tf):
    while t0 <= tf:
        y0 = y0 + h*f(y0,t0)
        t0 += h
    return y0

def rk2(h, t0, y0, tf):
    while t0 <= tf:
        k1 = h * f(y0,t0)
        k2 = h * f(y0+(2/3)*k1,t0+(2/3)*h)
        y0 = y0 + 0.25*k1 + 0.75*k2
        t0 += h
    return y0

def rk4(h, t0, y0, tf):
    while t0 < tf:
        k1 = h * f(y0,t0)
        k2 = h * f(y0 + 0.5*k1,t0+0.5*h)
        k3 = h * f(y0 + 0.5*k2,t0+0.5*h)
        k4 = h * f(y0 + k3,t0+h)
        y0 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        t0 += h
    return y0

def backward_euler(h, t0, y0, tf):
    while t0 < tf:
        y0 = y0 + h*f(y0, t0+h)
        t0 += h
    return y0

# i want to do some more tests here; let's test rk2
_rk2 = np.vectorize(rk2, excluded=['t0','y0','tf'])
fig1, ax1 = plt.subplots()
hh = np.array([0.001, 0.002, 0.005])
rk2_yy = _rk2(hh, 0, 0, 50)
rk2_errs = np.abs(625 - rk2_yy)
ax1.loglog(hh, rk2_errs, '-o', label='RK2')
m, _ = np.polyfit(np.log(hh), np.log(rk2_errs), 1)
print(f'Order of rk2 is {m}')

_forward_euler = np.vectorize(forward_euler, excluded=['t0','y0','tf'])
hh = np.array([0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02])
euler_yy = _forward_euler(hh, 0, 0, 50)
euler_errs = np.abs(625 - euler_yy)
ax1.loglog(hh, euler_errs, '-o', label='Euler')
m, _ = np.polyfit(np.log(hh), np.log(euler_errs), 1)
print(f'Order of forward euler is {m}')
fig1.savefig('plot.png')

print(rk2_yy)

