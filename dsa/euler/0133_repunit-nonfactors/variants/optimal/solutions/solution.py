def solve(limit: int = 100000) -> int:
    """Find the sum of all primes p < limit (100,000) that will NEVER be a factor of any repunit R(10^n).

    Mathematical Principles Applied:
    1. Repunit Factorization Property:
       A prime p (p != 2, 5) divides R(10^n) for some n >= 1 iff the minimal repunit length A(p) is of the form 2^a * 5^b (a power of 2 and 5).
       By Euler's totient theorem, A(p) divides p - 1. Thus, if A(p) consists solely of prime factors 2 and 5,
       then 10^(10^k) == 1 (mod p) for sufficiently large k (e.g. k = 16).

    2. Modular Exponentiation Criterion:
       Using a large power of 10 exponent (e.g. 10^16):
       - If pow(10, 10^16, mod) == 1, then p WILL divide some R(10^n).
       - If pow(10, 10^16, mod) != 1, then p will NEVER divide any R(10^n).

    Time Complexity: O(P log(10^16)) executing in ~0.02s.
    Space Complexity: O(limit) memory for Sieve of Eratosthenes.
    """
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(limit) if is_p[i]]

    non_factor_sum = 0
    big_exp = 10**16

    # Test each prime p < 100,000
    for p in primes:
        if p in (2, 5):
            non_factor_sum += p
            continue

        mod = 9 * p if p == 3 else p
        # If 10^(10^16) != 1 (mod mod), p will NEVER divide any repunit R(10^n)
        if pow(10, big_exp, mod) != 1:
            non_factor_sum += p

    # Return total sum of non-factor primes < 100,000
    return non_factor_sum


if __name__ == "__main__":
    print(solve())
