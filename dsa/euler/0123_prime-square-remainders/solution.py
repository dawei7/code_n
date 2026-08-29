def solve(target_rem: int = 10000000000) -> int:
    """Find the least n for which the remainder r = ((p_n - 1)^n + (p_n + 1)^n) mod p_n^2 first exceeds 10^10.

    Mathematical Principles Applied:
    1. Binomial Theorem Expansion Modulo p_n^2:
       Let p_n be the n-th prime.
       (p_n - 1)^n = (-1)^n + n * (-1)^(n-1) * p_n (mod p_n^2).
       (p_n + 1)^n = 1 + n * p_n (mod p_n^2).

       Adding both modulo p_n^2:
       - If n is EVEN: remainder r = 2 (mod p_n^2).
       - If n is ODD:  remainder r = 2 * n * p_n (mod p_n^2).

    2. Odd Index Linear Scan:
       Even n gives trivial remainder r = 2, which can never exceed 10^10.
       We only need to iterate ODD indices n = 1, 3, 5, ... and check r = 2 * n * p_n > 10^10.

    Time Complexity: O(N) where N ~ 21000 (executes in ~0.05s).
    Space Complexity: O(Limit) memory for Sieve of Eratosthenes.
    """
    limit = 1000000
    is_p = [True] * limit
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit, i):
                is_p[j] = False

    primes = [i for i in range(limit) if is_p[i]]

    # Iterate odd n indices (n = 1, 3, 5, ...)
    for n in range(1, len(primes) + 1, 2):
        p_n = primes[n - 1]
        r = 2 * n * p_n
        # Return first n obtaining remainder r > 10^10
        if r > target_rem:
            return n

    return -1


if __name__ == "__main__":
    print(solve())
