import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# priprava dat
samples = 10
noise = 2
x = np.linspace(0, 10, samples)
# puvodni primka
y = 3 + 2 * x
# pridame sumiky
noise = np.random.randint(-noise, noise, samples)
test = y + noise

# linregres vraci celou tuhle kopu informaci a je nutno posbirat vsechno
slope, inter, rvalue, pvalue, stderr = linregress(x, test)
# zajima nas v tuhle chvili jen tohle
print(
    "slope = %.3f, intercept=%.3f, corellation coeff=%.3f, stderr=%.3f" % (
        slope, inter, rvalue, stderr
        )
    )
# zrekonstruujeme si prolozenou primku
regr = x * slope + inter

fig, ax = plt.subplots()
ax.plot(x, y, 'b', label='puvodni primka')
# mame jen par zasumnenych bodu
ax.scatter(x, test, color='r', marker='o', label='se sumikama')
ax.plot(x, regr, color='g', label='prolozena primka')
ax.grid()
ax.legend()
plt.show()
