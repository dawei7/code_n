from fractions import Fraction


def u(n: int) -> int:
    """Tenth degree generating polynomial function u_n = 1 - n + n^2 - n^3 + n^4 - n^5 + n^6 - n^7 + n^8 - n^9 + n^10."""
    return sum((-1) ** i * (n**i) for i in range(11))


def lagrange_eval(points: list[tuple[int, int]], x_eval: int) -> int:
    """Evaluate Lagrange interpolating polynomial L_k(x) at x_eval for given integer points (x_1, y_1), ..., (x_k, y_k).

    Mathematical Principles Applied:
    1. Lagrange Interpolating Polynomial:
       Given k points (x_j, y_j) for j = 1..k, the unique polynomial of degree at most k - 1 is:
       L_k(x) = sum_{j=1}^k y_j * l_j(x)
       where l_j(x) = prod_{m != j} (x - x_m) / (x_j - x_m).

    2. Exact Rational Arithmetic:
       Using fractions.Fraction guarantees exact rational interpolation without floating-point precision loss.
    """
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

    # Return integer evaluation of Lagrange interpolating polynomial
    return int(result)


def solve() -> int:
    """Find the sum of First Incorrect Terms (FITs) for Best Optimum Polynomials (BOPs) of u_n up to k = 10.

    Mathematical Principles Applied:
    1. Optimum Polynomial OP(k, n):
       OP(k, n) is the degree k - 1 polynomial formed from the first k terms of sequence u_n.
       A term OP(k, n) is a First Incorrect Term (FIT) if OP(k, n) != u_n for the smallest n (which is n = k + 1).

    2. Sum of FITs:
       Sum FITs for k = 1 to 10 by interpolating OP(k, k + 1).

    Time Complexity: O(k^3) over k = 1..10 (executes in ~0.001s).
    Space Complexity: O(k) memory.
    """
    # Precompute first 11 terms of generating sequence u_n for n = 1..11
    points = [(n, u(n)) for n in range(1, 12)]

    sum_fits = 0
    # Evaluate FIT at x = k + 1 for each degree k = 1..10
    for k in range(1, 11):
        fit = lagrange_eval(points[:k], k + 1)
        sum_fits += fit

    # Return total sum of First Incorrect Terms
    return sum_fits


if __name__ == "__main__":
    print(solve())
