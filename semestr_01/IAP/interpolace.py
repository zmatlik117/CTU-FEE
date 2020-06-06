from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

# z kolika vyorku udelam orezanou funkci
samples = 6
# jakeho radu chci interpolacni polynom
order = 4
inter_functions = []
# orezana osa x
x_axis = np.linspace(0, 2 * np.pi, samples)
# poctiva osa x se spoustou vzorku
x_axis_true = np.linspace(0, 2 * np.pi, 1000)
# a orezana funkce vycislena
signal = np.sin(x_axis)

# grafovani
fig, ax = plt.subplots()
ax.plot(x_axis, signal, 'ro:')
ax.grid()

# vykreslim interpolaci pro vsechny rady az po order - 1 definovany nahore
# pocita se od nulteho, proto 4
for kind in range(order):
    inter = interpolate.interp1d(x_axis, signal, kind=kind)
    inter_functions.append(inter)
    line = ax.plot(x_axis_true, inter(x_axis_true), '--', label=kind)
ax.legend()

plt.show()
