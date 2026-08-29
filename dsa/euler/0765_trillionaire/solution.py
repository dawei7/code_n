"""Project Euler Problem 765: Trillionaire.

Find the maximum probability of reaching at least 10^12 grams of gold starting from 1 gram
after 1000 rounds of optimal coin-betting (p=0.6), rounded to 10 decimal digits.
"""

from typing import List


def _binom_coeffs(n: int) -> List[int]:
    c = [1] * (n + 1)
    for k in range(1, n + 1):
        c[k] = c[k - 1] * (n - k + 1) // k
    return c


def solve(n: int = 1000, M: int = 1_000_000_000_000, digits: int = 10) -> str:
    """Compute exact maximal success probability using martingale budget and Neyman-Pearson likelihood ordering."""
    total_paths = 1 << n
    budget_paths = total_paths // M

    comb = _binom_coeffs(n)

    suffix = [0] * (n + 2)
    for k in range(n, -1, -1):
        suffix[k] = suffix[k + 1] + comb[k]

    k0 = 0
    for k in range(n, -1, -1):
        if suffix[k] > budget_paths >= suffix[k + 1]:
            k0 = k
            break

    rem = budget_paths - suffix[k0 + 1]

    pow2 = [1] * (n + 1)
    pow3 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = pow2[i - 1] * 2
        pow3[i] = pow3[i - 1] * 3

    den = 5**n
    num = 0
    for k in range(k0 + 1, n + 1):
        num += comb[k] * pow3[k] * pow2[n - k]

    if rem > 0:
        num += rem * pow3[k0] * pow2[n - k0]

    scale = 10**digits
    q, r = divmod(num * scale, den)
    if r * 2 >= den:
        q += 1
    int_part, frac_part = divmod(q, scale)
    return f"{int_part}.{str(frac_part).zfill(digits)}"


if __name__ == "__main__":
    print(solve())
