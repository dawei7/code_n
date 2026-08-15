import math


def solve(max_n: int = 10000) -> int:
    """Find sum_{N=5}^{10000} D(N) where D(N) = -N if max product P(N) is terminating decimal, else +N.

    Mathematical Principles Applied:
    1. Continuous Optimization of Part Product:
       Let P(N, k) = (N / k)^k for k equal parts.
       Taking natural logarithm: f(k) = ln P(N, k) = k * (ln N - ln k).
       Setting derivative f'(k) = ln N - ln k - 1 = 0 => ln(N / k) = 1 => k = N / e.
       The continuous maximum occurs at k_real = N / e (where e = 2.71828...).
       The optimal integer parts count k is either floor(N / e) or ceil(N / e).

    2. Terminating vs Non-Terminating Decimal Test:
       The maximum product P(N, k) = (N / k)^k is a terminating decimal iff the simplified denominator
       d = k / gcd(N, k) has NO prime factors other than 2 and 5!
       - If d = 2^a * 5^b: P(N, k) is terminating => D(N) = -N.
       - Otherwise:       P(N, k) is non-terminating => D(N) = +N.

    3. Total Summation across N = 5..10000:
       Sum D(N) for N from 5 to 10,000.

    Time Complexity: O(max_n * log max_n) executing in ~0.01s.
    Space Complexity: O(1) constant auxiliary space.
    """
    E = math.e
    total = 0

    for N in range(5, max_n + 1):
        # Optimal integer parts count k is near N / e
        k1 = int(N / E)
        k2 = k1 + 1

        # Compare ln P(N, k1) vs ln P(N, k2)
        if k1 * math.log(N / k1) > k2 * math.log(N / k2):
            k = k1
        else:
            k = k2

        # Simplify denominator d = k / gcd(N, k)
        d = k // math.gcd(N, k)
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5

        # Check if simplified denominator d consists only of prime factors 2 and 5
        if d == 1:
            total -= N
        else:
            total += N

    # Return total sum sum_{N=5}^{10000} D(N)
    return total


if __name__ == "__main__":
    print(solve())
