from scipy import integrate
import sympy
import numpy as np

# poridim si osu x
step = int(1e6)

# definice mezi - pro numpy a sympy je nutno definovat zvlast
# zejmena v pripade matematickych konstant!!
low_np = 0
low_sp = 0

high_np = np.pi + 1         # todle je cislo spocitane na docela dost desetinnych mist
high_sp = sympy.pi + 1      # ale todle uz je matematicky presny symbol!!

x_axis = np.linspace(low_np, high_np, step)
# vycislim funkci
vals = np.sin(x_axis)
# pouziju simpsona
result = integrate.simps(vals, x_axis)
# a vysypu to do konzole - v tomhle pripade tak nejak cekam ze kdyz zintegruju horni pulku
# sinusovky ze to vyhodi 2
print(result)

# matematicky presny vysledek. cerna magie. Prostudujte si dokumentaci k modulu sympy
i, x = sympy.symbols('i, x')
i = sympy.Integral(sympy.sin(x), (x, low_sp, high_sp))
print("Integral to solve: %s" % i)

integral_solved = i.doit()
print("analytical solution : %s" % integral_solved)
integral_evalued = integral_solved.evalf()
print("floating point evaluation of solution: %s" % integral_evalued)
error = (integral_evalued - result) / integral_evalued
print("Error of numerical solution = %s " % error)
