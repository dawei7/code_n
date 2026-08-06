"""Multi-stream dynamic programming for LeetCode 313."""


def _nth_super_ugly(n: int, primes: list[int]) -> int:
    ugly = [1] * n
    pointers = [0] * len(primes)
    candidates = primes[:]
    for i in range(1, n):
        next_value = min(candidates)
        ugly[i] = next_value
        for j, prime in enumerate(primes):
            if candidates[j] == next_value:
                pointers[j] += 1
                candidates[j] = prime * ugly[pointers[j]]
    return ugly[-1]


def solve(n: int, primes: list[int]) -> int:
    return _nth_super_ugly(n, primes)
