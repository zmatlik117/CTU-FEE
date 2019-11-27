from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def tested_function(x):
    """
    Testovana funkce

    Da se sem napsat vselijaka cunarna
    """
    freq = 1
    damp_fac = 0.1
    val = np.sin(freq * x)
    damp = np.exp(-1 * damp_fac * abs(x))
    return val * damp


# kolikrat hodlam opakovat optimalizacni vypocet
no_samples = 10
# kolik kroku chci v optimalizaci provest
niter = 1000
# kde si tipnu minimum - je to umyslne nastaveny nekam totalne do pryc aby se to obcas netrefilo
original_estimate = 8

samples = []
# na kolik samplu chci natrhat osu x
num = int(1e4)
x_axis = np.linspace(start=-20, stop=20, num=num)
# akorat alias pro funkci aby se to kdyztak lip prebiralo pres copy-paste-modify
function = tested_function

# resim grafovani
fig, ax = plt.subplots()
ax.plot(x_axis, function(x_axis), 'b')
# tuknu tam prvni vykop kde cekam minimum
ax.plot(original_estimate, function(original_estimate), marker='x', color='r')
ax.set(xlabel='x', ylabel='myfunc', title='tested function')
ax.grid()
plt.show(block=False)

# probehnu vsechny vypocty
for iteration in range(no_samples):
    print("iteration %s" % iteration)
    # basinhop je principialne dost podobnej simulated annealing, proto je
    # simulated annealing ve scipy deprecated
    min_basinhop = optimize.basinhopping(func=function, x0=original_estimate, niter=niter)['x']
    result = function(min_basinhop)
    samples.append((min_basinhop, result))
    # prasknu to do grafu jako bod
    ax.plot(min_basinhop, result, marker='o')
    fig.canvas.draw()
plt.show()

# a vysypu do konzole nalezeny minima - ne vzdy se trefi do globalniho
for sample in samples:
    print(sample[0], sample[1])
