"""
Test IAP

Zavery:

1)  scipy.integrate.odeint je dost slusny solver pro soustavy dif. rovnic 1. radu.
    Hromada fyziky jede timhle smerem - v podstate vsechny pohyby se pocitaji pres
    Hamiltonovy rovnice v polohach a hybnostech -> nativni reseni pro prirodu
    + sikovne se pouziva kvuli uz treba existujici casove ose. Pro prvni vykop idealni
    Docela slusne vysledky pro zadane podminky dava 1k iteraci

2)  RK45 je hodne pokrocily solver - jako vsechny metody ve scipy modulu ma perfektni
    dokumentaci. Hodne se vyuziva dedicnosti obecneho solveru - nekdo se nad navrhem skutecne dobre zamyslel
    protoze to ma hlavu a patu.
    Metoda NEPRACUJE s konstantnim casovym krokem - sama si voli vhodny krok podle velikosti
    posledni zmeny!
    Slusne vysledky dava pro max_step=0.0001, kdyz je vetsi tak jsou videt v grafu hrby
    Diky dedicnosti a kompatibilnimu interface je srovnani s RK 23
    VYHRADNE otazka prejmenovani metody!!

3)  Implementace RK45 podle https://rosettacode.org/wiki/Runge-Kutta_method#Python
    Vysledky dava - ale narozdil od scipy nekontroluje spolehlivost vypoctu!!
    Pro pocet kroku << 10000 (e.g. 1000) vypocet neni numericky stabilni a neni jak se to zavcasu dozvedet!!

4)  Suma sumarum:
    Uzit scipy.integrate.odeint pro prvni vykopy, je jednoducha na pouziti, funguje spolelive ale muze byt
    casove narocna pro slozitejsi funkce. Tezko rict jestli by pomohl vyrazne JIT preklad(python module numba)
    ponevadz scipy je postaveno na numpy - a ten ma tenzorove vypocty predkompilovne z C, takze je to celkem fofr

    RK vlastni implementace by mohla byt optimalizovana JIT prekladem - ale nedovedu si predstavit use case

    scipy.integrate.RKxy je vhodno pouzit na vypocet slozitejsich problemu, optimalizovano promennym casovym krokem.
    Davalo by smysl v pripade nejakych slozitejsich fci zkusit nejprve pomoci odeint vyresit problem
    s nahodne ovlivnenymi pocatecnimi podminkami (numpy.random.uniform) a pak kouknout jestli se tam alespon ramcove RK45 trefila
"""

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint, RK45

freq = 50
L = 10 / 314
R = 10
C = 10**-5
omega = 2 * np.pi * freq

def dU_dx(U, t):
    # pro vetsi prehlednost vychroustam ir a ud
    # rovnice spocitana na papire
    ir = U[0]
    ud = U[1]
    eq = np.array([
        (5 * np.sin(omega * t) - ud - R * ir) / L,
        (ir - 10**-7 * (np.exp(19 * ud) - 1)) / C
        ])
    return eq


def dU_dt_RK(t, y):
    # prevolavani kvuli poradi argumentu v RK
    return dU_dx(y, t)


def rk4(f, x0, y0, x1, n):
    # from https://rosettacode.org/wiki/Runge-Kutta_method#Python
    _vx = [0] * (n + 1)
    _vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    _vx[0] = x = x0
    _vy[0] = y = y0
    for i in range(1, n + 1):
        result = f(x, y)
        k1 = h * result
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        _vx[i] = x = x0 + i * h
        _vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return _vx, _vy

# pocatecni podminky
U0 = [0, 0]
# casova osa
xs = np.linspace(0, 0.04, 1000)
# vypocet
Us = odeint(dU_dx, U0, xs)
il = Us[:, 0]
udiode = Us[:, 1]
# rekonstrukce buzeni
buzeni = 5 * np.sin(omega * xs)
# runge kutta metoda ze scipy
# je docela zajimavy co to udela kdyz povolim velkej max_step, da to min presny vysledky
runge_kutta = RK45(fun=dU_dt_RK, t0=0, y0=[0, 0], t_bound=0.04, max_step=0.0001)
rk_ir = []
rk_ud = []
timestamp = []
while runge_kutta.status == 'running':
    rk_ir.append(runge_kutta.y[0])
    rk_ud.append(runge_kutta.y[1])
    timestamp.append(runge_kutta.t)
    runge_kutta.step()
if runge_kutta.status == 'failed':
    raise ValueError("Runge Kutta calculation failed")

# vlastni implementace runge kutta
vx, vy = rk4(f=dU_dt_RK, x0=0, y0=U0, x1=0.04, n=10000)
# nutna transpozice seznamu protoze ma spatny tvar
vy = list(map(list, zip(*vy)))

# grafovani
plt.xlabel("t")
plt.ylabel("amplitude")
plt.title("RLC with diode")
plt.plot(xs, il, label='ir', linestyle='--')
plt.plot(xs, udiode, label='ud', linestyle='--')
plt.plot(xs, buzeni, label='uZ', linestyle='-')
# grafovani RK
plt.plot(timestamp, rk_ir, label='rk_ir', linestyle=':')
plt.plot(timestamp, rk_ud, label='rk_ud', linestyle=':')
# grafovani custom implementace RK
plt.plot(vx, vy[0], label='rk_cust_ir', linestyle='-.')
plt.plot(vx, vy[1], label='rk_cust_ud', linestyle='-.')
plt.legend()
plt.grid()
plt.show()
