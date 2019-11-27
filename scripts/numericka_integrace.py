from scipy import integrate
import numpy as np

def func(x):
    return x**3 + 2* x**2 -5*x -8

def func2(x):
    return np.sin(x)

step = int(1e6)
x_axis = np.linspace(0, np.pi, step)

vals = func2(x_axis)

result = integrate.simps(vals, x_axis)
print(result)