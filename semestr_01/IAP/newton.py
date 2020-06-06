import sympy
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import time

"""
Obecny popis metody tecen
x_k+1 = x_k - f(x_k) / f_diff(x_k)

"""

def tested_function(x):
    """
    Testovaci funkce
    """
    return x**2 + 2 * x - 20

# poridim si symboly se kterymi budu racovat
x = sympy.symbols('x')
f, f_diff = sympy.symbols('f, f_diff', function=True)
tick = time.perf_counter()
res = sympy.solve(f, x)
tock = time.perf_counter()
print("Prusecky funkce s nulou:")
for val in res:
    print(val.evalf())
print("zabralo %ss" % (tock - tick))

# testovana funkce
f = tested_function(x)
x_num = np.linspace(-10, 10, 500)
y = tested_function(x_num)


# prvni derivace
f_diff = sympy.diff(f, x)
# analyticke vyrazy konvertuju do funkce ktera jde v pythonu volat a vraci cislo
num_func = sympy.lambdify([x], f)
num_diff = sympy.lambdify([x], f_diff)

# prvotni odhad pruseciku s nulou
x_k = 10

fig, ax = plt.subplots()
ax.plot(x_num, y)
ax.grid()
tick = time.perf_counter()
try:
    for _i in range(50):
        x_k = x_k - num_func(x_k) / num_diff(x_k)
        ax.plot(x_k.real, num_func(x_k).real, marker='+')
except ZeroDivisionError:
    print("Nemozno dopocitat vysledek")
    print("Vypocet se pravdepodobne ztratil v inflexi nebo linearni casti funkce")
tock = time.perf_counter()
print("numericky vysledek: %s" % x_k)
print("zabralo %ss" % (tock - tick))

# ted to zkusime trosku elegantnejsi metodou
tick = time.perf_counter()
# fsolve uvnitr pouziva newtonovu iteracni metodu, ale pocita s tim ze
# a) vysledek nemusi dopocitat a nevyhazuje vyjimku kdyz podeli nulou
# b) se ji da predhodit cele pole pocatecnich odhadu odkud ma zacit
# -> upocita mnohem vic reseni en bloc!!! Neni ovsem zaruceno ze najde VSECHNA!
sol = fsolve(tested_function, np.array([10, -10]))
tock = time.perf_counter()
print("reseni pres jeden z mnoha solveru scipy %s" % sol)
for s in sol:
    ax.scatter(s, tested_function(s), marker='x')
print("zabralo %ss" % (tock - tick))

plt.show()
