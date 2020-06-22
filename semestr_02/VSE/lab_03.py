# -*- coding: UTF-8 -*-
"""
Fazova trajektorie spinani ruznych typu zateze tranzistorem - myslim ze to byl KD503
"""
#pylint: disable=invalid-name

from matplotlib import pyplot as plt
import numpy as np

POINTS = 500

def graf_time(t, u, i, dt, dv, di, title):
    t_ax = [time * dt for time in t]
    i_ax = [curr * di for curr in i]
    v_ax = [volt * dv for volt in u]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel("t[S]")
    ax.set_ylabel("")
    ax.plot(t_ax, i_ax, label='Ic[A]')
    ax.plot(t_ax, v_ax, label='Uce[V]')
    ax.grid()
    ax.legend(loc='upper left')
    plt.title(title)
    plt.show()


def graf_xy_soar(u, i, dv, di, ic, uce, pmax, p_u, u_p, title):
    i_ax = [curr * di for curr in i]
    v_ax = [volt * dv for volt in u]
    # soar
    i_max_ax = np.full((POINTS, 1), ic)
    u_ax = np.linspace(0, uce, POINTS)
    soar = np.zeros([POINTS])
    soar_reduced = np.zeros([POINTS])
    i_pm = pmax / u_ax
    i_pm_reduced = p_u / u_ax
    for idx in range(0, POINTS):
        if i_pm[idx] > i_max_ax[idx]:
            soar[idx] = i_max_ax[idx]
            soar_reduced[idx] = i_max_ax[idx]
        else:
            soar[idx] = i_pm[idx]
            if idx * uce < POINTS * u_p:
                soar_reduced[idx] = i_pm[idx]
            else:
                soar_reduced[idx] = i_pm_reduced[idx]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel("Uce[V]")
    ax.set_ylabel("Ic[A]")
    ax.plot(v_ax, i_ax, label=title)
    ax.plot(u_ax, soar, label='SOAR')
    ax.plot(u_ax, soar_reduced, label='SOAR@T=100°C')
    ax.legend()
    ax.grid()
    plt.show()


# transistor SOAR
ic_max = 20  # A
uce_max = 80  # V
p_max = 150  # W
p_u = 65  # W
u_p = 30  # V

# resistive load
title = 'R zatez'
r_t_div = 200E-6
r_v_div = 50  # V/div
r_i_div = 1  # 1A/1V
r_t = [0.1, 0.2, 0.2, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.4, 7.4, 7.5]
r_u = [0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3]
r_i = [0.1, 0.1, 0.1, 0.4, 1.3, 1.75, 2.0, 2.33, 2.66, 2.7, 0.1, 0.1]

graf_time(r_t, r_u, r_i, r_t_div, r_v_div, r_i_div, title)
graf_xy_soar(
    r_u, r_i, r_v_div, r_i_div,
    ic_max, uce_max, p_max, p_u, u_p,
    title)

# RL load
title = 'RL bez kompenzace'
rl_t_div = 200E-6
rl_v_div = 50  # V/div
rl_i_div = 1  # 1A/1V
rl_t = [0.1, 0.2, 0.2, 1.0, 3.0, 5.0, 7.0, 7.4, 7.5, 7.6, 7.7, 7.8]
rl_u = [0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 2.4, 2.2, 0.5, 0.3]
rl_i = [0.1, 0.1, 0.1, 0.33, 1.33, 1.75, 2.8, 3, 1.5, 0.1, 0.1, 0.1]

graf_time(rl_t, rl_u, rl_i, rl_t_div, rl_v_div, rl_i_div, title)
graf_xy_soar(
    rl_u, rl_i, rl_v_div, rl_i_div,
    ic_max, uce_max, p_max, p_u, u_p,
    title)

# RL load with diode
title = 'RL + dioda'
rld_t_div = 200E-6
rld_v_div = 50  # V/div
rld_i_div = 1  # 1A/1V
rld_t = [0.1, 0.2, 0.2, 1.0, 3.0, 5.0, 7.0, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.2]
rld_u = [0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 1, 0.8, 0.66, 0.5, 0.45, 0.4, 0.3]
rld_i = [0.1, 0.1, 0.1, 0.33, 1.33, 1.75, 2.8, 3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

graf_time(rld_t, rld_u, rld_i, rld_t_div, rld_v_div, rld_i_div, title)
graf_xy_soar(
    rld_u, rld_i, rld_v_div, rld_i_div,
    ic_max, uce_max, p_max, p_u, u_p,
    title)
