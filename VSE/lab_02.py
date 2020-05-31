"""
Teplotni zavislost odporu
"""

from matplotlib import pyplot as plt

# meas = {sample: ([temp, R])}

temps = [22.0, 45, 60, 80, 100, 115]
meas = {
    "PT100": ([108.6, 112.4, 119.8, 125.8, 133.3, 140.7],
              temps),
    "PTC60": ([59.22, 58.1, 61.3, 74.6, 147.9, 4100],
              temps),
    "TR212 4k7": ([4687, 4671, 4654, 4637, 4618, 4601],
                  temps),
    "TR154 6k8": ([6685, 6669, 6657, 6643, 6630, 6618],
                  temps),
    "NTC 6k8": ([7578, 6070, 3860, 2700, 1833, 1222],
                temps),
    "NTC 40R": ([39.08, 26.80, 15.8, 9.88, 6.04, 3.72],
                temps),

}


plt.xlabel("Temp[\u00b0C]")
plt.ylabel("R[% nominal@25\u00b0C]")
for sensor, char in meas.items():
    x = char[0]
    y = char[1]
    nom = x[0]
    z = [number * 100 / nom for number in x]
    plt.plot(y, z, label=str(sensor)+"\u00b0C")
plt.grid()
plt.legend()
plt.ylim(95, 105)
plt.show()
