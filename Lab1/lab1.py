import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import math


def linear_generator(x0, a, c, M):
    xn = x0
    while True:
        yield xn
        xn = (a * xn + c) % M


def M_generator(gen1, gen2, M = 2 ** 10 + 1, k=64):
    v = [next(gen1) for _ in range(k)]
    while True:
        x, y = next(gen1), next(gen2)
        j = int(y * k / M)
        yield v[j]
        v[j] = x


def normally_psi(gen, M):
    while True:
        yield next(gen) / M


def discrete_psi(gen, j):
    while True:
        yield next(gen) % j

def moments_match(seq):
    n = len(seq)
    m = np.mean(seq)
    s2 = (1 / (n - 1)) * np.sum([(num - m) ** 2 for num in seq])
    ksi1 = m - 0.5
    ksi2 = s2 - 1/12
    c1 = math.sqrt(12 * n)
    c2 = ((n - 1) / n) * (0.0056 * 1/n + 0.0028 * 1/(n ** 2) - 0.0083 * 1/(n ** 3)) ** (-0.5)




if __name__ == '__main__':
    eps0 = 0.05

    lc_file = open('inputLC.txt', mode='r')
    gen0x0 = int(lc_file.readline())
    gen0a = int(lc_file.readline())
    gen0c = int(lc_file.readline())
    gen0M = int(lc_file.readline())
    lc_file.close()

    mm_file = open('inputMM.txt', mode='r')
    gen1x0 = int(mm_file.readline())
    gen1a = int(mm_file.readline())
    gen1c = int(mm_file.readline())
    gen1M = int(mm_file.readline())

    gen2x0 = int(mm_file.readline())
    gen2a = int(mm_file.readline())
    gen2c = int(mm_file.readline())
    gen2M = int(mm_file.readline())

    genK = int(mm_file.readline())
    mm_file.close()

    gen3M = 2 ** 10 + 1

    gen0 = linear_generator(gen0x0, gen0a, gen0c, gen0M)
    gen1 = linear_generator(gen1x0, gen1a, gen1c, gen1M)
    gen2 = linear_generator(gen2x0, gen2a, gen2c, gen2M)
    gen3 = M_generator(gen1, gen2, gen3M, genK)
    gens = [gen0, gen1, gen2, gen3]
    maxs = [gen0M, gen1M, gen2M, gen1M]

    n1 = 10000
    n2 = 10 ** 6

    all_examples = []

    for i in range(4):
        gen = normally_psi(gens[i], maxs[i])
        all_examples.append(np.array([next(gen) for _ in range(n1)]))
        all_examples.append(np.array([next(gen) for _ in range(n2)]))


    for examples in all_examples:
        moments_match(examples)

    fig = plt.figure()

    for i in range(8):
        plt.subplot(3, 3, i + 1)
        plt.scatter(all_examples[i][:-1], all_examples[i][1:])
    plt.show()