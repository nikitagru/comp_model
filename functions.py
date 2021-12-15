p = 3
q = 1
h = 0.01 #0.001
restingX = 1
restingY = 1

points = [[2, 1], [1, 1.1], [0.5, 1], [1, 0.5], [3, 1], [1, 3], [2, 4], [4, 2]]
# points = [[2, 1], [1, 2], [2, 4], [4, 2]]
# points = [[2, 1], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7]]
# points = [[1, 1.1], [1, 1.05], [1, 1.02]]

def x_func(xm, ym):
    return 1 - xm * ym
    # return ym

def y_func(xm, ym, local_p):
    return local_p * ym * (xm - ((1 + q) / (q + ym)))
    # return xm * (-1)

def increment_p():
    global p
    p = p + 1

def getH():
    global h
    return h
