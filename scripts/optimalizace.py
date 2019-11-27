import scipy
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def compare_results(result1, result2, tolerance):
    """
    compare if 2 results are equal within certain tolerance

    tolerance is applied to result1
    """
    tol = tolerance * result1 / 100
    if abs(result2 - result1) > tol:
        return True
    return False


def scalar1(x):
    return np.sin(x)*np.exp(-0.1*(x-0.6)**2)


def tested_function(x):
    freq = 1
    damp_fac = 0.1
    val = np.sin(freq * x)
    damp = np.exp(-1 * damp_fac * abs(x))
    return val * damp


no_samples = 10
niter = 1000
samples = []
original_estimate = 8

num = int(1e4)

x_axis = np.linspace(start=-20, stop=20, num=num)

function = tested_function

fig, ax = plt.subplots()
ax.plot(x_axis, function(x_axis), 'b')
ax.plot(original_estimate, function(original_estimate), marker='x', color='r')
ax.set(xlabel='x', ylabel='myfunc', title='pokus')
ax.grid()
plt.show(block=False)

for iteration in range(no_samples):
    print("iteration %s" % iteration)
    min_basinhop = scipy.optimize.basinhopping(func=function, x0=original_estimate, niter=niter)['x']
    result = function(min_basinhop)
    samples.append((min_basinhop, result))
    ax.plot(min_basinhop, result, marker='o')
    fig.canvas.draw()
plt.show()

for sample in samples:
    print(sample[0], sample[1])
