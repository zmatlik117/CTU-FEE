from scipy import integrate
import numpy as np

def func(x):
    """
    testovaci funkce
    """
    return x**3 + 2 * x**2 - 5 * x - 8

def func2(x):
    """
    testovaci funkce
    """
    return np.sin(x)

# vyberu si kterou funkci ze chci integrovat
tested_func = func2

# poridim si osu x
step = int(1e6)
x_axis = np.linspace(0, np.pi, step)
# vycislim funkci
vals = tested_func(x_axis)
# pouziju simpsona
result = integrate.simps(vals, x_axis)
# a vysypu to do konzole - v tomhle pripade tak nejak cekam ze kdyz zintegruju horni pulku
# sinusovky ze to vyhodi 2
print(result)