import numpy as np
import matplotlib.pyplot as plt

Is = 95e-6
VT = 150e-3
E = 1
R = 100


def f1(x):
    return (E - x) / R - Is * (np.exp(x / VT) - 1)


def fT(x):
    return (E - x) / R


def fD(x):
    return Is * (np.exp(x / VT) - 1)


x = np.linspace(-2, 2, 1000)
y1 = f1(x)
yT = fT(x)
yD = fD(x)

fp, axp = plt.subplots()
axp.set_xlabel("uD")
axp.set_ylabel("i")
axp.plot(x, fT(x), label="Thévenin")
axp.plot(x, fD(x), label="Diode")
axp.set_ylim((-1, 1))
axp.set_ylim((0 , .05))
axp.grid()
axp.legend()

fi, axi = plt.subplots()
axi.set_xlabel("uD")
axi.set_ylabel("i")
axi.plot(x, f1(x))
axi.set_ylim((-1, 1))
axi.set_ylim((-0.1 , .05))
axi.set_yticks([0])
axi.set_yticklabels(["0"])
axi.grid()
axi.legend()

plt.show()