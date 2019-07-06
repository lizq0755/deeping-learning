import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print('AND(0, 0)：' + str(AND(0, 0))) # 输出0
print('AND(1, 0)：' + str(AND(1, 0))) # 输出0
print('AND(0, 1)：' + str(AND(0, 1))) # 输出0
print('AND(1, 1)：' + str(AND(1, 1))) # 输出1