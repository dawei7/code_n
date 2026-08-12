import math


def solve(limit: int = 10000) -> int:
    """Find smallest odd composite number that cannot be written as prime + 2 * k^2.
    
    Time Complexity: O(N * sqrt(N))
    Space Complexity: O(N)
    """
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    for c in range(9, limit, 2):
        if not is_prime[c]:
            written = False
            k = 1
            while 2 * k * k < c:
                if is_prime[c - 2 * k * k]:
                    written = True
                    break
                k += 1
            if not written:
                return c

    return -1
