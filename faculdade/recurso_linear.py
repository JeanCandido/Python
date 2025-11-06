import numpy as np


x = [-2, -2, -1, -1, 0, 0, 1, 1, 2, 2]
y = [0, 0, 2, 3, 4, 4, 5, 6, 8, 8]

x = [[1, i] for i in x]

def reg_linear(x, y):
    xt = np.transpose(x)
    xtx = np.dot(xt, x)
    beta = np.dot(np.dot(np.linalg.inv(xtx), xt), y)
    return beta

print(reg_linear(x, y))