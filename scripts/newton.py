import time
import sympy
import numpy as np
import matplotlib.pyplot as plt

"""
Obecny popis metody tecen
x_k+1 = x_k - f(x_k) / f_diff(x_k)

"""

# poridim si symboly se kterymi budu racovat
x, a = sympy.symbols('x, a')
f, f_diff, func = sympy.symbols('f, f_diff, func', function=True)

# testovana funkce
# f = x**2 + 2 * x - 10
f = sympy.sqrt(x) - 1
print(f)
# symbolicke reseni f = 0:
res = sympy.solve(f, x)
print("Prusecky funkce s nulou:")
for val in res:
    print(val.evalf())

# prvni derivace
f_diff = sympy.diff(f, x)
print(f_diff)

num_func = sympy.lambdify([x], f)
num_diff = sympy.lambdify([x], f_diff)

# prvotni odhad pruseciku s nulou
x_k = -10

fig, ax = plt.subplots()
x = np.linspace(0, 5, 100)
y = np.sqrt(x) - 1
ax.plot(x, y)
ax.grid()

for i in range(10):
    x_k = x_k - num_func(x_k) / num_diff(x_k)
    ax.plot(x_k.real, num_func(x_k).real, marker='o')
plt.show()

