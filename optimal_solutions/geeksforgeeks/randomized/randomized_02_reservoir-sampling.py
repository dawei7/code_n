"""Optimal solution for randomized_02: Reservoir Sampling.

Pick k items uniformly at random from a stream of unknown
length. Standard algorithm: fill the reservoir with the first
k items; for each subsequent item i (i >= k), replace a
random reservoir index with probability k / (i + 1).
"""


def solve(stream, k, n):
    import random
    if k <= 0 or n == 0:
        return []
    reservoir = list(stream[:k])
    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir
