import numpy as np


def euler(stop, step_size):
    y = 0
    for x in np.arange(0, stop+step_size, step_size):
        y += 5 + 2 * x + 3 * x**2
    return y


print(euler(5, 0.0001))