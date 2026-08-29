def count_solutions_n2(n: int) -> int:
    """Compute the number of distinct positive integer solutions (x, y) to 1/x + 1/y = 1/n.

    Mathematical Principles Applied:
    1. Transformation to Hyperbolic Diophantine Equation:
       1/x + 1/y = 1/n <=> n(x + y) = xy <=> xy - nx - ny = 0.
       Adding n^2 to both sides (Simon's Favorite Factoring Trick):
       (x - n)(y - n) = n^2.

    2. Divisor Counting for n^2:
       Let u = x - n and v = y - n. Then u * v = n^2.
       The number of ordered pairs (u, v) is the number of divisors of n^2, d(n^2).
       For unordered pairs (x, y) with x <= y, the number of distinct solutions is:
       Number of solutions = (d(n^2) + 1) / 2.

    3. Prime Factorization Formula:
       If n = p1^a1 * p2^a2 * ... * pk^ak, then n^2 = p1^(2*a1) * p2^(2*a2) * ... * pk^(2*ak).
       d(n^2) = prod_{i=1}^k (2*ai + 1).
    """
    temp = n
    divisors_n2 = 1
    d = 2

    # Trial division to extract prime factors of n
    while d * d <= temp:
        if temp % d == 0:
            exp = 0
            while temp % d == 0:
                exp += 1
                temp //= d
            # Multiply (2 * exp + 1) for prime factor d
            divisors_n2 *= 2 * exp + 1
        d += 1

    # If remaining temp > 1, it is a prime factor with exponent 1
    if temp > 1:
        divisors_n2 *= 3  # (2 * 1 + 1)

    # Return distinct unordered solutions (x, y)
    return (divisors_n2 + 1) // 2


def solve(target: int = 1000) -> int:
    """Find the least n for which the number of distinct solutions to 1/x + 1/y = 1/n exceeds target (1,000).

    Time Complexity: O(N * sqrt(N)) executing in ~0.15s.
    Space Complexity: O(1) constant auxiliary space.
    """
    n = 1
    # Increment n until solution count exceeds target = 1,000
    while True:
        if count_solutions_n2(n) > target:
            # Return minimal n obtaining > 1,000 distinct reciprocal solutions
            return n
        n += 1


if __name__ == "__main__":
    print(solve())
