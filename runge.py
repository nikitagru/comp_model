from functions import *
import matplotlib.pyplot as plt
import numpy as np

xm_all = []
ym_all = []
local_p = p


def xm_next(xm, ym):
    return xm + ((get_k1(xm, ym) + 2 * get_k2(xm, ym) + 2 * get_k3(xm, ym) + get_k4(xm, ym)) / 6)

def ym_next(xm, ym):
    return ym + ((get_l1(xm, ym) + 2 * get_l2(xm, ym) + 2 * get_l3(xm, ym) + get_l4(xm, ym)) / 6)

#------first iteration------
def get_k1(xm, ym):
    return h * x_func(xm, ym)

def get_l1(xm, ym):
    return h * y_func(xm, ym, local_p)
#------first iteration------


#------second iteration------
def get_k2(xm, ym):
    return h * x_func(xm + (get_k1(xm, ym) / 2), ym + (get_l1(xm, ym) / 2))

def get_l2(xm, ym):
    return h * y_func(xm + (get_k1(xm, ym) / 2), ym + (get_l1(xm, ym) / 2), local_p)
#------second iteration------


#------third iteration------
def get_k3(xm, ym):
    return h * x_func(xm + (get_k2(xm, ym) / 2), ym + (get_l2(xm, ym) / 2))

def get_l3(xm, ym):
    return h * y_func(xm + (get_k2(xm, ym) / 2), ym + (get_l2(xm, ym) / 2), local_p)
#------third iteration------

#------fourth iteration------
def get_k4(xm, ym):
    return h * x_func(xm + get_k3(xm, ym), ym + get_l3(xm, ym))

def get_l4(xm, ym):
    return h * y_func(xm + get_k3(xm, ym), ym + get_l3(xm, ym), local_p)
#------fourth iteration------

def calc(xm, ym):
    for i in range(10000):
        xm.append(round(xm_next(xm[i], ym[i]), 4))
        ym.append(round(ym_next(xm[i], ym[i]), 4))
        xm_all.append(round(xm_next(xm[i], ym[i]), 4))
        ym_all.append(round(ym_next(xm[i], ym[i]), 4))

def calcStableLoop(xm, ym, x_p):
    for i in range(10000):
        xm.append(round(xm_next(xm[i], ym[i]), 4))
        ym.append(round(ym_next(xm[i], ym[i]), 4))
        xm_all.append(round(xm_next(xm[i], ym[i]), 4))
        ym_all.append(round(ym_next(xm[i], ym[i]), 4))
        if (findSustainablePoints(xm[i], ym[i], xm[i + 1], ym[i + 1])):
            break


def printLimitLoops():
    fig, axs = plt.subplots(3)
    for j in range(3):
        for i in range(len(points)):
            xm = [points[i][0]]
            ym = [points[i][1]]
            if (i > 1):
                findSustainablePoints(xm[i - 1], ym[i - 1], xm[i - 2], ym[i -2])
            calc(xm, ym)
            axs[j].plot(xm, ym)

        plt.xlabel('X')
        plt.ylabel('Y')
        increment_p()
    plt.show()

def findSustainablePoints(x_i, y_i, x_ii, y_ii):
    if (x_i > restingX and x_ii > restingX and (y_ii - restingY) * (y_i - restingY) < 0):
        return True
    return False


def printPhasePortrait():
    # fig = plt.figure()
    for i in range(len(points)):
        xm = [points[i][0]]
        ym = [points[i][1]]
        calc(xm, ym)
    #     plt.plot(xm, ym)
    # plt.show()
    # findStableLoop(xm_all, ym_all)
    x_p = findStableLoop(xm_all, ym_all)

    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.show()

    xm = []
    ym = []

    for i in range(len(points)):
        xm.append(x_p)
        ym.append(restingY)
        calcStableLoop(xm, ym, x_p)
        
    return len(xm)

def get_b(y_i, x_i, k):
    return y_i - k * x_i

def get_k(y_i, x_i, y_ii, x_ii):
    return ((y_i - y_ii) / (x_i - x_ii))

def calc_x_p(y, b, k):
    return (y - b) / k


def findStableLoop(xm, ym):
    x_p = [100]
    y_i = 0
    x_i = 0
    y_ii = 0
    x_ii = 0

    counter = 0
    for i in range(len(xm)):
        if (findSustainablePoints(xm[i], ym[i], xm[i + 1], ym[i + 1])):
            y_i = ym[i]
            x_i = xm[i]
            y_ii = ym[i + 1]
            x_ii = xm[i + 1]
            
            k = get_k(y_i, x_i, y_ii, x_ii)
            b = get_b(y_i, x_i, k)
            x_p.append(calc_x_p(restingY, b, k))
            counter = counter + 1
            if (counter + 1 == len(xm)):
                print("Нет такой точки")
                break
            if (abs(x_p[counter - 1] - x_p[counter]) < 0.001):
                break
    print(x_p[len(x_p) - 1])
    return x_p[len(x_p) - 1]

    
    # while(abs(x_p[counter] - x_p[counter + 1]) > 0.001):
    #     k = get_k(ym[counter], xm[counter], ym[counter + 1], xm[counter + 1])
    #     b = get_b(ym[counter], xm[counter], k)
    #     x_p.append(calc_x_p(restingY, b, k))
    #     counter = counter + 1
    #     if (counter + 1 == len(xm)):
    #         print("Нет такой точки")
    #         break

points_count = []
term = []
parametr = []
for j in range(30):
    points_count.append(printPhasePortrait())
    term.append(points_count[j] * getH())
    parametr.append(local_p)
    local_p = local_p + 0.3
    xm_all = []
    ym_all = []

print('==============================')
print(points_count)
print('==============================')
print(term)

fig = plt.figure()
plt.plot(parametr, term)
plt.show()
# printLimitLoops()

# printPhasePortrait()

# print("x_m: ")
# print(xm)
# print("\n")

# print("y_m: ")
# print(ym)
