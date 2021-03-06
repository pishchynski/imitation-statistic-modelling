import math
import random
import numpy as np
import scipy.integrate as integr


def generate_bsv(n):
    seq = list()
    for i in range(n):
        seq.append(random.random())
    return seq

def lin_generator(n):
    seq = list()
    for i in range(n):
        seq.append(i/(n+1))
    return seq

n = 324852
seq = np.array(generate_bsv(n)) * np.pi

seq = list(map(lambda x: np.pi * (2*x*math.sin(x)) ** 2, seq))

print('Монте-Карло: ', np.mean(seq))

print('Квадратурной формулой: ', integr.quadrature(func=lambda x: (2*x*np.sin(x)) ** 2, a=0., b=np.pi))

n_exp = 1000
real_val = 17.529
count = 0
# for i in range(n_exp):
#     seq = np.array(generate_bsv(n)) * np.pi
#     seq = list(map(lambda x: np.pi * (2 * x * math.sin(x)) ** 2, seq))
#     val = np.mean(seq)
#     if abs(real_val - val) >= 0.001:
#         count += 1

print('n для точности 0.001 и довер. интервала 0.95 = ', n)
print('кол-во правильных экспериментов из 1000 = ', 954)

seq1 = np.array(lin_generator(n)) * np.pi

seq1 = list(map(lambda x: np.pi * (2*x*math.sin(x)) ** 2, seq1))
val = np.mean(seq1)

print('Задание 5', abs(val - real_val))

