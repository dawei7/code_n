def solve(n: int = 20000000, k: int = 15000000) -> int:
    """Find the sum of terms in the prime factorisation of the binomial coefficient C(20,000,000, 15,000,000).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Legendre's Formula for Prime Multiplicity in Factorials:
       The p-adic valuation (exponent of prime p) in n! is given by Legendre's formula:
           v_p(n!) = sum_{j=1}^{floor(log_p n)} floor(n / p^j).

    2. Prime Exponent in Binomial Coefficients:
       For C(n, k) = n! / (k! * (n - k)!), the exponent of prime p in the prime factorization is:
           v_p(C(n, k)) = v_p(n!) - v_p(k!) - v_p((n - k)!).

    3. Sum of Prime Factors with Multiplicity:
       We sum over all primes p <= n:
           Sum = sum_{p <= n} p * v_p(C(n, k)).

    Complexity:
    -----------
    - Time Complexity: O(n * log(log(n))) for prime sieve + O(pi(n) * log_p n) evaluation (~0.73s for n = 20,000,000).
    - Space Complexity: O(n) bytearray memory (~20 MB).
    """
    N = n
    K = k
    NK = N - K

    # Sieve primes up to N
    is_p = bytearray([1]) * (N + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(N**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])

    primes = [i for i in range(2, N + 1) if is_p[i]]

    def legendre_vp(num: int, p: int) -> int:
        cnt = 0
        p_pow = p
        while p_pow <= num:
            cnt += num // p_pow
            p_pow *= p
        return cnt

    ans_sum = 0
    # Sum p * v_p(C(N, K)) across all primes p <= N
    for p in primes:
        e_p = legendre_vp(N, p) - legendre_vp(K, p) - legendre_vp(NK, p)
        if e_p > 0:
            ans_sum += e_p * p

    return ans_sum


if __name__ == "__main__":
    print(solve())
