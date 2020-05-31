# -*- coding: UTF-8 -*-
"""
Teplotni zavislost odporu

Puvodne pripraveno na situaci ze se teplota muze v prubehu mereni menit,
v prubehu mereni jsme od toho upustili.

ZAVER
-----

TR212 a TR154 se tvari jako rezistory, u nichz je teplotni zavislost parazitnim
jevem a je zadano aby byla co nejmensi.

NTC 6k8 a 40R maji velmi podobnou teplotni zavislost, ktera naznacuje podobnou
technologii vyroby. Zavislost neni linearni a pripomina klesajici exponencialu.
V uzkem rozsahu teplot je vsak mozno zavislost pomerne snadno linearizovat s
dostatecne malou chybou, pouzitelnou pro technicke ucely.

Krivka pro PT100 naznacuje mocninny charakter -> pro siroke rozsahy teplot nemusi
postacovat prace pouze s teplotnim koeficientem alpha a muze byt nutne uzit
vyssi rady. Zalezi na aplikaci a pozadovane presnosti mereni teplot.

PTC60 vykazuje silne exponencialni narust hodnoty rezistance v
merenem rozsahu teplot. Uziti jako tepelne pojistky/soucast odmagnetovavacich
obvodu CRT obrazovek neni prekvapive.
"""

from matplotlib import pyplot as plt

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

fig = plt.figure()
gs = fig.add_gridspec(1, 3)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
# spans two rows:
ax3 = fig.add_subplot(gs[0, 2])
axes = [ax1, ax2, ax3]
ylimits = [
    (98, 102),
    (0, 200),
    (0, 10000)
]

for axis, (ylimit_lo, ylimit_hi)in zip(axes, ylimits):
    axis.set_xlabel("Temp[°C]")
    axis.set_ylabel("R[% nominal@25°C]")
    for sensor, char in meas.items():
        ohm = char[0]
        temp = char[1]
        nom = ohm[0]  # @25°C
        ohm_rel = [number * 100 / nom for number in ohm]
        axis.plot(temp, ohm_rel, label=str(sensor), marker='s')
    axis.grid()
    axis.legend(loc='upper left')
    axis.set_ylim(ylimit_lo, ylimit_hi)
plt.show()
