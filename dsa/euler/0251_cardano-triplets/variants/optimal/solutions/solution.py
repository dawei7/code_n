from math import gcd, isqrt


def solve(limit: int = 110_000_000) -> int:
    """Find the number of Cardano Triplets (a, b, c) such that a + b + c <= limit.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Cardano Triplet Algebraic Condition:
       (a + b*sqrt(c))^(1/3) + (a - b*sqrt(c))^(1/3) = 1.
       Cubing both sides and letting u, v be the cube roots yields:
           27 b^2 c = (8a - 1)(a + 1)^2.

    2. Divisibility and Substitution:
       For integer solutions, a == 2 (mod 3). Let a = 3m - 1 = 3k + 2.
       Then:
           b^2 c = (8m - 3) m^2.

    3. Coprime Fraction Parameterization:
       Let gcd(b, m) = g, with m = x * g and b = y * g (gcd(x, y) = 1).
       Substituting into b^2 c = (8m - 3) m^2 yields:
           y^2 c = (8xg - 3) x^2.
       Since gcd(x, y) = 1, y^2 must divide (8xg - 3).
       Thus y must be odd, and 8x * g == 3 (mod y^2) has a unique base solution g_0 mod y^2.
       All solutions are g = g_0 + t * y^2 for t >= 0.

    4. Linear Upper Bound Counting:
       The inequality a + b + c <= limit translates to:
           g * ((3x + y) * y^2 + 8x^3) <= limit * y^2 + y^2 + 3x^2.
       This directly yields the count of valid t for each coprime pair (x, y).

    Complexity:
    -----------
    - Time Complexity: O(y_max * x_max) parameter scan (~3 minutes).
    - Space Complexity: O(1) auxiliary memory.
    """
    ans = 0

    for y in range(1, isqrt(limit) + 1, 2):
        y2 = y * y
        inv_8 = pow(8, -1, y2) if y2 > 1 else 0
        inv_3 = (3 * inv_8) % y2 if y2 > 1 else 0

        max_x = int((limit * y2 / 8) ** (1 / 3)) + 1
        for x in range(1, max_x + 1):
            if gcd(x, y) != 1:
                continue

            if y2 == 1:
                g0 = 1
            else:
                inv_x = pow(x, -1, y2)
                g0 = (inv_3 * inv_x) % y2
                if g0 == 0:
                    g0 = y2

            coeff = (3 * x + y) * y2 + 8 * x**3
            max_g = (limit * y2 + y2 + 3 * x * x) // coeff

            if max_g >= g0:
                ans += (max_g - g0) // y2 + 1

    return ans


if __name__ == "__main__":
    print(solve())
