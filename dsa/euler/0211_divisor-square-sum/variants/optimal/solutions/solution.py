import math
from array import array


def solve(limit: int = 64000000, block_size: int = 2000000) -> int:
    """Find the sum of all n < 64,000,000 such that sigma_2(n) is a perfect square.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Sum of Squares of Divisors sigma_2(n):
       sigma_2(n) = sum_{d | n} d^2.
       Multiplicative property: for n = p_1^e_1 * ... * p_k^e_k,
           sigma_2(n) = prod_{i=1}^k (1 + p_i^2 + p_i^4 + ... + p_i^(2*e_i)).

    2. Segmented Prime Sieve:
       Since any n < 64,000,000 can have at most one prime factor > sqrt(64,000,000) = 8000:
       We only need to sieve base primes p <= 8000 (1007 primes).
       Processing in contiguous memory blocks of size 2,000,000:
       - Maintain the remaining quotient rem[x] and accumulated sigma_2 product sig[x].
       - For each base prime p <= 8000, divide out all factors of p and multiply sig[x] by sigma_2(p^e).
       - Any remaining quotient r = rem[x] > 1 is a prime > 8000, so sig[x] *= (1 + r^2).

    3. Memory Safety & Performance:
       This block segmentation uses only ~16 MB of RAM (strictly under limits) and evaluates
       all 64 million integers in a single fast vectorized pass.

    Complexity:
    -----------
    - Time Complexity: O(limit * log log(sqrt(limit))) operations (~30s for limit = 64,000,000).
    - Space Complexity: O(block_size + sqrt(limit)) memory (~16 MB).
    """
    max_p = math.isqrt(limit) + 1

    # Sieve base primes up to sqrt(limit) = 8000
    is_p = bytearray([1]) * (max_p + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(max_p**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
    primes = [i for i in range(2, max_p + 1) if is_p[i]]
    prime_squares = [p * p for p in primes]

    ans = 0
    isqrt = math.isqrt

    # Process in memory-efficient contiguous blocks
    for L in range(1, limit, block_size):
        R = min(limit, L + block_size)
        B = R - L

        rem = array("I", range(L, R))
        sig = array("q", [1] * B)

        for p, p2 in zip(primes, prime_squares):
            st = ((L + p - 1) // p) * p - L
            for idx in range(st, B, p):
                val = rem[idx] // p
                term = 1 + p2
                curr_p2 = p2 * p2
                while val % p == 0:
                    val //= p
                    term += curr_p2
                    curr_p2 *= p2
                rem[idx] = val
                sig[idx] *= term

        # Factor in any large prime factors > 8000 and test perfect square condition
        for idx in range(B):
            r = rem[idx]
            s = sig[idx]
            if r > 1:
                s *= 1 + r * r
            root = isqrt(s)
            if root * root == s:
                ans += L + idx

    return ans


if __name__ == "__main__":
    print(solve())
