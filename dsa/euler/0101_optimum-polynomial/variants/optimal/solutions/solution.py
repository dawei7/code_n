from fractions import Fraction


def u(n: int) -> int:
    """Tenth degree generating polynomial function u_n."""
    return sum((-1)**i * (n**i) for i in range(11))


def lagrange_eval(points: list[tuple[int, int]], x_eval: int) -> int:
    """Evaluate Lagrange interpolating polynomial at x_eval for given integer points."""
    result = Fraction(0)
    k = len(points)
    for j in range(k):
        xj, yj = points[j]
        term = Fraction(yj)
        for m in range(k):
            if m != j:
                xm = points[m][0]
                term *= Fraction(x_eval - xm, xj - xm)
        result += term
    return int(result)


def solve() -> int:
    """Find sum of First Incorrect Terms (FITs) for BOPs of u_n up to k = 10.
    
    Time Complexity: O(deg^3)
    Space Complexity: O(deg)
    """
    points = [(n, u(n)) for n in range(1, 12)]

    sum_fits = 0
    for k in range(1, 11):
        fit = lagrange_eval(points[:k], k + 1)
        sum_fits += fit

    return sum_fits
