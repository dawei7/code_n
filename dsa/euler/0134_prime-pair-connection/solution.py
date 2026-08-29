def solve(limit: int = 1000000) -> int:
    """Find the sum of S(p1, p2) for all consecutive prime pairs (p1, p2) with 5 <= p1 <= limit (1,000,000).

    Mathematical Principles Applied:
    1. Linear Congruence Equation for S(p1, p2):
       Let m = 10^d be the smallest power of 10 strictly greater than p1 (m > p1).
       The number S(p1, p2) ends in p1, so S = k * m + p1 for some non-negative integer k.
       S must also be divisible by p2:
       k * m + p1 == 0 (mod p2) => k * m == -p1 (mod p2).

    2. Modular Inverse via Extended Euclidean Algorithm:
       Since p2 is prime and m = 10^d is coprime to p2 (since p2 >= 7), m has a unique modular inverse m^-1 (mod p2).
       `inv_m = pow(m, -1, p2)`.
       k = ((-p1) * inv_m) mod p2.
       S(p1, p2) = k * m + p1.

    Time Complexity: O(N log p2) executing in ~0.20s.
    Space Complexity: O(Limit) memory for prime sieve array.
    """
    sieve_limit = limit + 100
    is_p = [True] * sieve_limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(sieve_limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, sieve_limit, i):
                is_p[j] = False

    primes = [i for i in range(sieve_limit) if is_p[i]]

    # Find starting index for p1 = 5
    idx_5 = primes.index(5)

    sum_s = 0
    # Process consecutive prime pairs (p1, p2)
    for idx in range(idx_5, len(primes) - 1):
        p1 = primes[idx]
        if p1 > limit:
            break
        p2 = primes[idx + 1]

        # Calculate m = 10^d > p1
        m = 1
        while m <= p1:
            m *= 10

        # Solve linear congruence k * m == -p1 (mod p2)
        inv_m = pow(m, -1, p2)
        k = ((-p1) * inv_m) % p2

        # Minimum integer S ending in p1 and divisible by p2
        s = k * m + p1
        sum_s += s

    # Return total sum of S(p1, p2) for all 5 <= p1 <= 1,000,000
    return sum_s


if __name__ == "__main__":
    print(solve())
