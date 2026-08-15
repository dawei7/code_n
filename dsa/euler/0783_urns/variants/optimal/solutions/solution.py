"""Project Euler Problem 783: Urns.

Find E(10^6, 10) rounded to the nearest integer, where E(n, k) = E[ sum_{t=1}^n B_t(n, k)^2 ]
and B_t is the number of black balls removed on turn t from the urn.
"""


def _expected_sum_square(n: int, k: int) -> float:
    if n <= 0 or k <= 0:
        return 0.0

    m = float(2 * k)
    mu = 0.0
    s2 = 0.0
    M = float(k * (n + 1))

    total = 0.0
    comp = 0.0
    kf = float(k)

    for _ in range(n):
        Ey = mu + kf
        Ey2 = s2 + 2.0 * kf * mu + kf * kf

        denom = M * (M - 1.0)
        c1 = m * (M - m) / denom
        c2 = m * (m - 1.0) / denom

        Eb2 = c1 * Ey + c2 * Ey2

        y = Eb2 - comp
        t = total + y
        comp = (t - total) - y
        total = t

        coeff_y2 = 1.0 - 2.0 * m / M + c2
        s2_next = coeff_y2 * Ey2 + c1 * Ey
        mu_next = ((M - m) / M) * Ey

        mu, s2 = mu_next, s2_next
        M -= kf

    return total


def solve(n: int = 1_000_000, k: int = 10) -> int:
    """Compute E(n, k) using exact hypergeometric second moment recurrence and Kahan summation."""
    val = 0.0
    for _iter in range(1):
        val = _expected_sum_square(n, k)
    return int(val + 0.5)


if __name__ == "__main__":
    print(solve())
