import itertools


def is_prime(n: int) -> bool:
    """Fast primality test for pandigital prime set elements."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve() -> int:
    """Find number of distinct 1-9 pandigital sets containing only prime elements.
    
    Time Complexity: O(9! * Partitions)
    Space Complexity: O(1)
    """
    total_sets = 0

    def partition_search(digits: tuple[int, ...], start_idx: int, prev_prime: int):
        nonlocal total_sets

        val = 0
        for i in range(start_idx, len(digits)):
            val = val * 10 + digits[i]
            if val > prev_prime and is_prime(val):
                if i == len(digits) - 1:
                    total_sets += 1
                else:
                    partition_search(digits, i + 1, val)

    for perm in itertools.permutations(range(1, 10)):
        partition_search(perm, 0, 0)

    return total_sets
