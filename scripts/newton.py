import sympy
import numpy as np
import matplotlib.pyplot as plt

"""
Obecny popis metody tecen
x_k+1 = x_k - f(x_k) / f_diff(x_k)

"""

# poridim si symboly se kterymi budu racovat
x = sympy.symbols('x')
f, f_diff = sympy.symbols('f, f_diff', function=True)

# testovana funkce
f = x**2 + 2 * x - 20
# f = sympy.sqrt(x) - 1

print("testovana fce f = %s" % f)
# symbolicke reseni f = 0:
res = sympy.solve(f, x)
print("Prusecky funkce s nulou:")
for val in res:
    print(val.evalf())

# prvni derivace
f_diff = sympy.diff(f, x)
# analyticke vyrazy konvertuju do funkce ktera jde v pythonu volat a vraci cislo
num_func = sympy.lambdify([x], f)
num_diff = sympy.lambdify([x], f_diff)

# prvotni odhad pruseciku s nulou
x_k = -10

fig, ax = plt.subplots()
x = np.linspace(-10, 10, 500)
# y = np.sqrt(x) - 1
y = x**2 + 2 * x - 20
ax.plot(x, y)
ax.grid()

try:
    for _i in range(50):
        x_k = x_k - num_func(x_k) / num_diff(x_k)
        ax.plot(x_k.real, num_func(x_k).real, marker='o')
except ZeroDivisionError:
    print("Nemozno dopocitat vysledek")
    print("Vypocet se pravdepodobne ztratil v inflexi nebo linearni casti funkce")
print("numericky vysledek: %s" % x_k)
plt.show()
