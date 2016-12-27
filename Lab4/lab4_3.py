import math
import random
import numpy as np
import scipy.integrate as integr

data = np.genfromtxt('33-student.txt', delimiter=' ')
A, f = data[:-1], data[-1]
print(A.shape, f.shape)

print(np.max(A))

from copy import deepcopy
x_new = deepcopy(f)
x_prev = deepcopy(f) - 1000
while abs(np.max(x_prev - x_new)) > 0.00001:
    x_prev = deepcopy(x_new)
    x_new = A.dot(x_new) + f
    print(np.max(x_new - A.dot(x_new) - f))
