import bisect


def solve(limit: int = 10**8) -> int:
    """Find number of semiprimes n < limit.
    
    Time Complexity: O(limit/2 * log log(limit/2) + pi(sqrt(limit)) * log(pi(limit/2)))
    Space Complexity: O(limit/2)
    """
    max_prime = limit // 2

    is_p = bytearray([1]) * (max_prime + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(max_prime**0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = b'\x00' * len(is_p[i * i::i])

    primes = [i for i in range(max_prime + 1) if is_p[i]]

    count = 0
    for i, p1 in enumerate(primes):
        if p1 * p1 >= limit:
            break
        max_p2 = (limit - 1) // p1
        idx = bisect.bisect_right(primes, max_p2)
        count += (idx - i)

    return count
