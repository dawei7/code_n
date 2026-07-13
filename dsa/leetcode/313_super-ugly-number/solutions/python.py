"""Multi-stream dynamic programming for LeetCode 313."""


def _nth_super_ugly(n: int, primes: list[int]) -> int:
    ugly = [1] * n
    pointers = [0] * len(primes)
    candidates = primes[:]
    for index in range(1, n):
        next_value = min(candidates)
        ugly[index] = next_value
        for prime_index, prime in enumerate(primes):
            if candidates[prime_index] == next_value:
                pointers[prime_index] += 1
                candidates[prime_index] = prime * ugly[pointers[prime_index]]
    return ugly[-1]


def solve(n: int, primes: list[int]) -> int:
    return _nth_super_ugly(n, primes)
