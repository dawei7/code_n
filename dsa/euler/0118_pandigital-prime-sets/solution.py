import itertools


def is_prime(n: int) -> bool:
    """Fast wheel primality test for pandigital integer values.

    Mathematical Principles Applied:
    1. Wheel Primality Testing:
       Filter multiples of 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, then check candidate divisors 6k +/- 1 up to sqrt(n).
    """
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
    """Find the number of distinct 1-9 pandigital sets containing only prime elements.

    Mathematical Principles Applied:
    1. Permutations & Partition Tree Search:
       Generate all 9! = 362,880 permutations of digits {1..9}.
       For each permutation, partition it into 1 or more prime integer chunks.

    2. Canonical Increasing Order Enforcer:
       To ensure each unique set of primes is counted EXACTLY ONCE (since sets are unordered),
       we enforce strictly increasing prime elements: val > prev_prime.

    Time Complexity: O(9! * Partitions) executing in ~0.55s.
    Space Complexity: O(1) constant auxiliary space.
    """
    total_sets = 0

    def partition_search(
        digits: tuple[int, ...], start_idx: int, prev_prime: int
    ) -> None:
        """Backtracking partition search enforcing strictly increasing prime values."""
        nonlocal total_sets

        val = 0
        for i in range(start_idx, len(digits)):
            val = val * 10 + digits[i]
            # Enforce strictly increasing prime elements to avoid set permutations
            if val > prev_prime and is_prime(val):
                if i == len(digits) - 1:
                    # Valid full 1-9 pandigital prime set complete
                    total_sets += 1
                else:
                    # Recurse to partition remaining digits
                    partition_search(digits, i + 1, val)

    # Loop all 9! = 362,880 digit permutations of {1..9}
    for perm in itertools.permutations(range(1, 10)):
        partition_search(perm, 0, 0)

    # Return total count of unique 1-9 pandigital prime sets
    return total_sets


if __name__ == "__main__":
    print(solve())
