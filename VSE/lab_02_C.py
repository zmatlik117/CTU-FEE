# -*- coding: UTF-8 -*-
"""
Teplotni zavislost kondenzatoru

Stejne jako v pripade mereni teplotni zavislosti rezistance, i tento zdrojovy kod
je pripraven na ruzny krok v merenych teplotach a neni toho vyuzito

ZAVER
-----

Nutno zduraznit teplotni zavislost materialu C0G - skutecne jsme overili
ze tento material ma minimalizovanou teplotni zavislost.

Maximalni odchylka v merenem pasmu teplot je do 10%
od nominalni hodnoty pri 25°C.


"""

from matplotlib import pyplot as plt

R0 = 1105
T0 = 25
alpha = 4.5E-3
pt1k = [1105, 1198, 1295, 1408, 1518, 1617]  # mereno senzorem PT1000
temps_meas = [25, 40, 60, 80, 100, 116]  # mereno teplomerem
temps_pt1k = [(R - R0)/(R0*alpha) + T0 for R in pt1k]  # prepocet odporu na teplotu

# vyber zdroje teplot
temps = temps_meas
meas = {
    "1uF X7R": ([0.939E-6, 0.992E-6, 0.992E-6, 0.967E-6, 0.954E-6, 0.98E-6],
                temps),
    "47nF U2J": ([48.1E-9, 47.4E-9, 46.7E-9, 46E-9, 45.5E-9, 44.98E-9],
                 temps),
    "100nF Y5V": ([97.54E-9, 99.7E-9, 95.6E-9, 92.1E-9, 89.1E-9, 89.5E-9],
                  temps),
    "100nF X8R": ([96.2E-9, 99.9E-9, 98.8E-9, 97.3E-9, 97.3E-9, 100E-9],
                  temps),
    "47nF C0G": ([47E-9, 47E-9, 47E-9, 47E-9, 47E-9, 47.03E-9],
                 temps),
    "47nF Y2": ([49.0E-9, 48.9E-9, 47.7E-9, 48.4E-9, 48.1E-9, 47.7E-9],
                temps),
    "1nF slida": ([1.03E-9, 1.03E-9, 1.04E-9, 1.043E-9, 1.047E-9, 1.05E-9],
                  temps)

}

fig = plt.figure(dpi=200)
ax = fig.add_subplot()

ax.set_xlabel("Temp[°C]")
ax.set_ylabel("C[% nominal@25°C]")
for sensor, char in meas.items():
    x = char[0]
    y = char[1]
    nom = x[0]
    z = [number * 100 / nom for number in x]
    ax.plot(y, z, label=str(sensor), marker='s')
ax.grid()
ax.legend()

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.set_xlabel("Temp[°C]")
ax2.set_ylabel("Temp PT1000[°C]")
ax2.plot(temps_meas, temps_pt1k, label="PT1000")
ax2.grid()
ax2.legend()
plt.show()


