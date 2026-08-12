import math


def solve(limit: int = 999966663333) -> int:
    """Find sum of all semidivisible numbers not exceeding limit.
    
    Time Complexity: O(sqrt(limit) / log(sqrt(limit)))
    Space Complexity: O(sqrt(limit))
    """

    def sieve_primes(n):
        is_p = bytearray([1]) * (n + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])
        return [i for i in range(2, n + 1) if is_p[i]]

    max_p = int(math.sqrt(limit)) + 1000
    primes = sieve_primes(max_p)

    def sum_multiples(k, L, R):
        if L > R:
            return 0
        start = ((L + k - 1) // k) * k
        end = (R // k) * k
        if start > end:
            return 0
        cnt = (end - start) // k + 1
        return cnt * (start + end) // 2

    total_sum = 0
    for idx in range(len(primes) - 1):
        p1 = primes[idx]
        p2 = primes[idx + 1]

        L = p1 * p1 + 1
        R = min(p2 * p2 - 1, limit)

        if L > R:
            if p1 * p1 > limit:
                break
            continue

        s1 = sum_multiples(p1, L, R)
        s2 = sum_multiples(p2, L, R)
        s12 = sum_multiples(p1 * p2, L, R)

        total_sum += s1 + s2 - 2 * s12
        if p1 * p1 >= limit:
            break

    return total_sum
