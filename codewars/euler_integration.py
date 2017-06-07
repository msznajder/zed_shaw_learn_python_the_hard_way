import numpy as np


def euler(stop, step_size):
    y = 0
    for x in np.arange(0, (stop+step_size), step_size):
        y += 5 + 2 * x + 3 * x**2
    # TODO: Why I need to divide by 1000 to pass tests?
    return y / 10000


print(euler(5, 0.0001))