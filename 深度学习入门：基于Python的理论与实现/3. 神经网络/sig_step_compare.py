import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y_step_function = step_function(x)
y_sigmoid = sigmoid(x)

plt.plot(x, y_step_function, '--', label='step_function')
plt.plot(x, y_sigmoid, label='sigmoid')
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.legend() # 显示标签
plt.show()