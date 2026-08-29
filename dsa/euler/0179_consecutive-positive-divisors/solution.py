def solve(limit: int = 10000000) -> int:
    """Find the number of integers 1 < n < limit (10,000,000) for which n and n + 1 have the exact same number of positive divisors.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Divisor Function Multiplicative Property:
       For prime factorization n = p_1^{e_1} * p_2^{e_2} * ... * p_k^{e_k},
       the divisor count function d(n) is multiplicative:
           d(n) = (e_1 + 1) * (e_2 + 1) * ... * (e_k + 1)

    2. Linear Sieve (Euler's Sieve) for Multiplicative Functions:
       Compute d(n) in strictly O(N) linear time:
       - Maintain `e[n]`, the exponent of the smallest prime factor of n.
       - For prime p: d[p] = 2, e[p] = 1.
       - If p divides i:
             e[i * p] = e[i] + 1
             d[i * p] = (d[i] // (e[i] + 1)) * (e[i * p] + 1)
       - If p does not divide i (coprime):
             e[i * p] = 1
             d[i * p] = d[i] * 2

    3. Consecutive Equal Divisor Count Comparison:
       Iterate n from 2 to limit - 1:
           if d[n] == d[n + 1]: count += 1

    Complexity:
    -----------
    - Time Complexity: O(limit) strictly linear time (~2.80s for limit = 10^7).
    - Space Complexity: O(limit) memory for divisor count and exponent arrays.
    """
    primes = []
    d = [0] * (limit + 1)
    e = [0] * (limit + 1)
    d[1] = 1

    # Linear sieve for d(n) in O(N) time
    for i in range(2, limit + 1):
        if d[i] == 0:
            primes.append(i)
            d[i] = 2
            e[i] = 1

        for p in primes:
            ip = i * p
            if ip > limit:
                break
            if i % p == 0:
                e[ip] = e[i] + 1
                d[ip] = (d[i] // (e[i] + 1)) * (e[ip] + 1)
                break
            else:
                e[ip] = 1
                d[ip] = d[i] * 2

    count = 0
    # Compare consecutive divisor counts d(n) == d(n + 1)
    for n in range(2, limit):
        if d[n] == d[n + 1]:
            count += 1

    # Return total number of consecutive equal divisor pairs
    return count


if __name__ == "__main__":
    print(solve())
