def solve(k: int = 10**9, target_count: int = 40) -> int:
    """Find the sum of the first 40 prime factors of the massive repunit R(10^9).

    Mathematical Principles Applied:
    1. Repunit Divisibility Theorem:
       R(k) = (10^k - 1) / 9.
       For a prime p (p != 2, 5):
       - If p == 3: p divides R(k) iff 10^k == 1 (mod 27).
       - If p != 3: p divides R(k) iff 10^k == 1 (mod p).

    2. Modular Binary Exponentiation:
       `pow(10, 10**9, mod)` evaluates 10^(10^9) mod p in O(log k) = 30 multiplication steps!

    3. Prime Factor Collection:
       Sieve primes up to 200,000, test 10^k == 1 (mod mod), and sum the first 40 qualifying prime factors.

    Time Complexity: O(Limit log K) executing in ~0.01s.
    Space Complexity: O(Limit) memory for Sieve of Eratosthenes.
    """
    limit = 200000
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(limit) if is_p[i]]

    prime_factors = []
    # Test primes in ascending order
    for p in primes:
        if p in (2, 5):
            continue  # 2 and 5 never divide any repunit R(k)

        mod = 9 * p if p == 3 else p
        # Check if 10^k == 1 (mod mod) via modular binary exponentiation
        if pow(10, k, mod) == 1:
            prime_factors.append(p)
            # Break as soon as 40 prime factors are collected
            if len(prime_factors) == target_count:
                break

    # Return total sum of the first 40 prime factors of R(10^9)
    return sum(prime_factors)


if __name__ == "__main__":
    print(solve())
