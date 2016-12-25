import sys, argparse
import numpy as np
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-mn', '--mod_normally', action='store_true', dest='mod')
    args = parser.parse_args()
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

    gen0 = linear_generator(gen0x0, gen0a, gen0c, gen0M)
    gen1 = linear_generator(gen1x0, gen1a, gen1c, gen1M)
    gen2 = linear_generator(gen2x0, gen2a, gen2c, gen2M)
    gen3 = M_generator(gen1, gen2, 2 ** 10 + 1, genK)
    gens = [gen1, gen2, gen3]
    maxs = [101, 2 ** 10 + 1, 101]

    n1 = 10000
    n2 = 2 ** 20

    examples01 = [next(gen0) for i in range(n1)]
    examples02 = [next(gen0) for i in range(n2)]

    examples11 = [next(gen1) for i in range(n1)]
    examples12 = [next(gen1) for i in range(n2)]

    examples21 = [next(gen2) for i in range(n1)]
    examples22 = [next(gen2) for i in range(n2)]

    examples31 = [next(gen3) for i in range(n1)]
    examples32 = [next(gen3) for i in range(n2)]

    all_examples = [examples01, examples02, examples11, examples12, examples21, examples22, examples31, examples32]

    fig = plt.figure()

    for i in range(3):
        jmax = 5
        if i == 2:
            jmax = 4
        for j in range(2, jmax):
            plt.subplot(4, 3, i * 3 + j - 1)
            plt.scatter([all_examples[i * 3 + j - 2][k] for k in range(len(all_examples[i * 3 + j - 2])-1)], [all_examples[i * 3 + j - 2][k] for k in range(1, len(all_examples[i * 3 + j - 2]))])

    plt.show()