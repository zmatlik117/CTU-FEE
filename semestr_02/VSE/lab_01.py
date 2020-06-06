# -*- coding: UTF-8 -*-
"""
Teplotni zavislost tranzistoru

Z casovych duvodu byla merena pouze teplotni zavislost IGBT tranzistoru.

Z grafu je patrne, ze s rostouci teplotou pri Ugs=const Id prudce roste,
v zavislosti na pracovnim bode i vice nez dvojnasobne!
V pripade ze by nekdy nekdo hodlal IGBT tranzistor pouzit jinak nez jako spinace,
t.j. v linearnim rezimu, musi pri navrhu obvodu toto nutne vzit v uvahu.

V pripade uziti paralelnich IGBT pro zvyseni max Id je nutno mit je na chladici
co nejbliz k sobe, idealne na stejnem cipu - teploti zavislost by snadno mohla
zpusobit pretizeni nektereho z nich a pak skonci v kremikovem nebi vsechny.
"""

from matplotlib import pyplot as plt

transistor = {
    35: ([0, 1, 3.8, 5, 5.15, 5.35, 5.45, 5.55],
         [0, 0, 0, 0.2, 0.3, 0.75, 1.2, 1.7]),
    50: ([0, 4, 4.5, 4.95, 5.05, 5.25, 5.35, 5.49],
         [0, 0, 0.05, 0.25, 0.6, 0.9, 1.3, 2]),
    75: ([0, 4, 4.5, 4.75, 4.95, 5.15, 5.25, 5.35],
         [0, 0, 0.1, 0.2, 0.5, 1.1, 1.65, 2.4])
}

plt.xlabel("Ugs[V]")
plt.ylabel("Id[A]")
plt.title("IRG4PH40U")
for temp, char in transistor.items():
    x = char[0]
    y = char[1]
    plt.plot(x, y, label=str(temp)+"°C", marker='s')
    plt.xlim(3, 6)
    plt.grid()
    plt.legend()
plt.show()
