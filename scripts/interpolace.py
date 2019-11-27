from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

samples = 6
order = 4
inter_functions = []

x_axis = np.linspace(0, 2 * np.pi, samples)
x_axis_true = np.linspace(0, 2 * np.pi, 1000)
signal = np.sin(x_axis)
# plot signal

fig, ax = plt.subplots()
ax.plot(x_axis, signal, 'ro:')

for kind in range(order):
    inter = interpolate.interp1d(x_axis, signal, kind=kind)
    inter_functions.append(inter)
    line = ax.plot(x_axis_true, inter(x_axis_true), '--', label=kind)
ax.legend()

plt.show()
