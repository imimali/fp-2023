import math
import matplotlib.pyplot as plt
import numpy as np
import time

nr_steps = 0


def f(n, m, p):
    """
    Does nothing useful, just convenient for complexity computation
    :param n: parameter, must be an integer
    :param m: another parameter, should ideally be greater than 0 for this to be
        interesting, but it works otherwise as well
    :param p: tricky parameter, should be greater than 0 and different from 1
    :return: 1 :))
    """
    global nr_steps
    nr_steps+=1
    if n <= 1:
        return 1
    q = n / p
    for _ in range(m):
        f(q, m, p)


if __name__ == '__main__':
    for p, m in [(2, 3)]:
        step_numbers = []
        theoretical = []
        empirical = []
        for n in range(1, 50):
            nr_steps = 0
            f(n, m, p)
            step_numbers.append(nr_steps)
            theoretical.append(m ** (math.log(n, p) + 1))

        plt.plot(step_numbers, label=f'actual nr steps')
        plt.plot(theoretical, label=f'theoretical')
        # plt.plot(empirical,label=f'empirical {n}-{m}-{p}')
    plt.xlabel('n')
    plt.ylabel('nr steps')
    plt.legend()

    plt.show()
