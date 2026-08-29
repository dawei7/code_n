def r_max(a: int) -> int:
    """Find the maximum remainder r_max(a) when (a-1)^n + (a+1)^n is divided by a^2.

    Mathematical Principles Applied:
    1. Binomial Theorem Expansion Modulo a^2:
       (a - 1)^n = (-1)^n + n * (-1)^(n-1) * a + O(a^2).
       (a + 1)^n = 1^n + n * 1^(n-1) * a + O(a^2).

       Adding both expansions modulo a^2:
       - If n is EVEN: (a - 1)^n + (a + 1)^n = 1 - n*a + 1 + n*a = 2 (mod a^2).
       - If n is ODD:  (a - 1)^n + (a + 1)^n = -1 + n*a + 1 + n*a = 2*n*a (mod a^2).

    2. Maximizing 2*n*a (mod a^2):
       We want to maximize remainder R = (2 * n * a) mod a^2.
       This is equivalent to maximizing (2 * n) mod a.
       - If a is EVEN: maximum (2*n) mod a occurs when 2*n = a - 2  => R_max = a * (a - 2).
       - If a is ODD:  maximum (2*n) mod a occurs when 2*n = a - 1  => R_max = a * (a - 1).
    """
    if a % 2 == 0:
        return a * (a - 2)
    else:
        return a * (a - 1)


def solve(limit: int = 1000) -> int:
    """Find the sum of r_max(a) for 3 <= a <= limit (1,000).

    Time Complexity: O(limit) linear execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Sum closed-form r_max(a) values for a from 3 to 1,000
    return sum(r_max(a) for a in range(3, limit + 1))


if __name__ == "__main__":
    print(solve())
