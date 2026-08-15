"""Project Euler Problem 387: Harshad Numbers.

Find the sum of all strong, right truncatable Harshad primes less than 10^14.
"""

from collections import deque
from typing import List, Tuple


def is_prime(n_val: int) -> bool:
    """Deterministic Miller-Rabin primality test for n < 2^64."""
    if n_val < 2:
        return False
    if n_val in (2, 3):
        return True
    if n_val % 2 == 0 or n_val % 3 == 0:
        return False

    d = n_val - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for a in bases:
        if n_val <= a:
            break
        x = pow(a, d, n_val)
        if x == 1 or x == n_val - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n_val
            if x == n_val - 1:
                break
        else:
            return False
    return True


def solve(limit: int = 10**14) -> int:
    """Generate all right truncatable Harshad numbers and sum derived strong Harshad primes."""
    total_sum = 0

    # Queue stores tuples of (number, digit_sum)
    queue: deque[Tuple[int, int]] = deque((d, d) for d in range(1, 10))

    while queue:
        num, dsum = queue.popleft()

        # Check if num is a strong Harshad number
        if is_prime(num // dsum):
            # Check candidate primes formed by appending a single digit
            for last_digit in (1, 3, 7, 9):
                cand = num * 10 + last_digit
                if cand < limit and is_prime(cand):
                    total_sum += cand

        # Extend right truncatable Harshad tree
        for next_digit in range(10):
            nxt_num = num * 10 + next_digit
            nxt_dsum = dsum + next_digit
            if nxt_num * 10 < limit:
                if nxt_num % nxt_dsum == 0:
                    queue.append((nxt_num, nxt_dsum))

    return total_sum


if __name__ == "__main__":
    print(solve())
