import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5]) # 仅权重和偏置与AND不同
    b = -.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print('OR(0, 0)：' + str(OR(0, 0))) # 输出0
print('OR(1, 0)：' + str(OR(1, 0))) # 输出1
print('OR(0, 1)：' + str(OR(0, 1))) # 输出1
print('OR(1, 1)：' + str(OR(1, 1))) # 输出1