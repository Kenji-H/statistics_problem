import bisect

import numpy as np

# create a dice with given frequency
def create_dice(freq):
    cdf = np.cumsum(freq)
    def dice():
        p = np.random.uniform()
        return bisect.bisect_left(cdf, p)
    return dice

if __name__ == '__main__':
    dice = create_dice([1.05/6, 0.95/6, 1.0/6, 1.0/6, 1.05/6, 0.95/6])
    for _ in xrange(1000):
        print dice()
