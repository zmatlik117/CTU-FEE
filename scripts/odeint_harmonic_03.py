"""
Example s numerickym resenim harmonicke funkce - tentokrat s buzenim
"""

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

# konstanty rovnice
damp = 5
# docela zajimavy vysledky dava nadkriticky tlumeni pri buzeni
freq = 5
freq_buzeni = freq * 2
# je docela zajimavy ten faktor prasknout trebas na dvojnasobek zakladni frekvence systemu
# dela to docela zajimavy zazneje :)
amp_buzeni = 10000
# amp_buzeni muze byt pro smysluplne vysledky relativne velke, viz.
# https://en.wikipedia.org/wiki/Harmonic_oscillator#Sinusoidal_driving_force
omega = 2 * np.pi * freq

def dU_dx(U, x):
    # definice rovnice
    # x'' + 2 * damp * omega + omega**2 * x = amp_buzeni * cos(2 * pi * freq_buzeni * x)
    # takze eq[0] = x'
    # a     eq[1] = y'
    eq = [
        U[1],
        - 2 * damp * omega * U[1] - omega**2 * U[0] + amp_buzeni * np.sin(2 * np.pi * freq_buzeni * x)
        ]
    # protoze se ma vracet y' takze se to odlifruje pres rovnitko na druhou stranu
    return eq
    # NOTE asi to nemusi byt nutne list, tuple by mel stacit

# U0[0] = pocatecni poloha
# U0[1] = pocatecni rychlost
U0 = [0, 0]
xs = np.linspace(0, 2, 200000)
# co je extra sympaticky - nemusim resit iterovani - staci do toho nacpat casovou osu!!
# Takze pokud uz ji nekde mam pouzitou nemusim pocitat krok metody tak aby mi to sedelo
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]
plt.xlabel("x")
plt.ylabel("y")
plt.title("Damped harmonic oscillator")
plt.plot(xs,ys)
plt.grid()
plt.show()