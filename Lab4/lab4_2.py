import math
import random
import numpy as np
import scipy.integrate as integr


def generate_bsv(n):
    seq = list()
    for i in range(n):
        seq.append(random.random())
    return seq


n = 10000
seq = generate_bsv(n)
seq = list(map(lambda x: -np.log(1-x), seq))
seq = list(map(lambda x: np.exp(- x**2 + x), seq))
print('По Монте-Карло: ', np.mean(seq))
