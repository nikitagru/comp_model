from functions import *
import matplotlib.pyplot as plt
import numpy as np

def xm_next(xm, ym):
    return xm + h * x_func(xm, ym)

def ym_next(xm, ym):
    return ym + h * y_func(xm, ym)


xm = [1]
ym = [0]

for i in range(10000):
    xm.append(round(xm_next(xm[i], ym[i]), 4))
    ym.append(round(ym_next(xm[i], ym[i]), 4))

fig = plt.figure()
plt.plot(xm, ym)
plt.show()

print("x_m: ")
print(xm)
print("\n")

print("y_m: ")
print(ym)

