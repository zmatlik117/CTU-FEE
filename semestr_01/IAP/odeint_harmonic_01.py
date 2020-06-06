from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint

# konstanty rovnice
amp = 20
damp = 0.1

def dU_dx(U, x):
    # definice rovnice
    # x'' + damp * x' + A * x = 0 zavedu substituci y = x'
    # takze eq[0] = x'
    # a     eq[1] = y'
    eq = [
        U[1],
        - 1 / amp * U[1] - damp * U[0]
        ]
    # protoze se ma vracet y' takze se to odlifruje pres rovnitko na druhou stranu
    return eq
    # NOTE asi to nemusi byt nutne list, tuple by mel stacit

U0 = [0, 1]
xs = np.linspace(0, 100, 2000)
# co je extra sympaticky - nemusim resit iterovani - staci do toho nacpat casovou osu!!
# Takze pokud uz ji nekde mam pouzitou nemusim pocitat krok metody tak aby mi to sedelo
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]
plt.xlabel("x")
plt.ylabel("y")
plt.title("Damped harmonic oscillator")
plt.plot(xs,ys)
plt.show()