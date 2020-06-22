# -*- coding: UTF-8 -*-
"""
Fazova trajektorie spinani ruznych typu zateze tranzistorem - myslim ze to byl KD503
"""
#pylint: disable=invalid-name

from matplotlib import pyplot as plt
import numpy as np

POINTS = 100

def graf_time(t, u, i, dt, dv, di):
    t_ax = [time * dt for time in t]
    i_ax = [curr * di for curr in i]
    v_ax = [volt * dv for volt in u]
    fig = plt.figure(dpi=200)
    ax = fig.add_subplot()
    ax.set_xlabel("t[uS]")
    ax.set_ylabel("")
    ax.plot(t_ax, i_ax, label='Ic[A]')
    ax.plot(t_ax, v_ax, label='Uce[V]')
    ax.grid()
    ax.legend(loc='upper left')
    plt.show()

def graf_xy(u, i, dv, di):
    i_ax = [curr * di for curr in i]
    v_ax = [volt * dv for volt in u]
    fig = plt.figure(dpi=200)
    ax = fig.add_subplot()
    ax.set_xlabel("Uce[V]")
    ax.set_ylabel("Ic[A]")
    ax.plot(v_ax, i_ax)
    ax.grid()
    plt.show()


def graf_xy_soar(u, i, dv, di, ic, uce, pmax, p_u, u_p):
    i_ax = [curr * di for curr in i]
    v_ax = [volt * dv for volt in u]
    # soar
    i_max_ax = np.full((POINTS + 1, 1), ic)
    u_ax = np.linspace(0, uce, POINTS + 1)
    soar = np.zeros([POINTS + 1])
    i_pm = pmax / u_ax
    for idx in range(0, POINTS + 1):
        if i_pm[idx] > i_max_ax[idx]:
            soar[idx] = i_max_ax[idx]
        else:
            soar[idx] = i_pm[idx]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel("Uce[V]")
    ax.set_ylabel("Ic[A]")
    ax.plot(v_ax, i_ax, label='KD503 op area')
    ax.plot(u_ax, soar, label='KD503 SOAR')
    ax.legend()
    ax.grid()
    plt.show()


def graf_SOAR(ic, uce, pmax, p_u, u_p):
    i_max_ax = np.full((POINTS + 1, 1), ic)
    u_ax = np.linspace(0, uce, POINTS + 1)
    soar = np.zeros([POINTS + 1])
    i_pm = pmax / u_ax
    for idx in range(0, POINTS + 1):
        if i_pm[idx] > i_max_ax[idx]:
            soar[idx] = i_max_ax[idx]
        else:
            soar[idx] = i_pm[idx]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel("Uce[V]")
    ax.set_ylabel("Ic[A]")
    ax.plot(u_ax, soar)
    ax.grid()
    plt.show()


# transistor SOAR
ic_max = 20  # A
uce_max = 80  # V
p_max = 150  # W
p_u = 70  # W
u_p = 30  # V

# resistive load
t_div = 200E-6
v_div = 50  # V/div
i_div = 1  # 1A/1V
r_t = [0.1, 0.2, 0.2, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.4, 7.4, 7.5]
r_u = [0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3]
r_i = [0.1, 0.1, 0.1, 0.4, 1.3, 1.75, 2.0, 2.33, 2.66, 2.7, 0.1, 0.1]

graf_xy_soar(r_u, r_i, v_div, i_div, ic_max, uce_max, p_max, p_u, u_p)


