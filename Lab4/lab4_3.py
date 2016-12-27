import numpy as np

A, f = [], []
with open('33-student.txt') as file:
    n = int(file.readline().strip())
    for i in range(n):
        A.append([float(x) for x in file.readline().split()])
    file.readline()
    f = [float(x) for x in file.readline().split()]

A, f = np.array(A), np.array(f)

print(np.max(A))

from copy import deepcopy
x_new = deepcopy(f)
x_prev = deepcopy(f) - 1000
while abs(np.max(x_prev - x_new)) > 0.00001:
    x_prev = deepcopy(x_new)
    x_new = A.dot(x_new) + f
    print(np.max(x_new - A.dot(x_new) - f))

print('==================')
for i in range(15):
    print(x_new[i])
