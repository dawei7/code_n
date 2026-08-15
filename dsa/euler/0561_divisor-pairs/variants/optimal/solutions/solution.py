"""Project Euler Problem 561: Divisor Pairs.

Find Q(10^12), where Q(n) = sum_{i=1..n} E(904961, i), and E(m, n) is the 2-adic
valuation of the number of distinct divisor pairs (a, b) with a | b of (p_m#)^n.
"""


def solve(n: int = 10**12, m: int = 904961) -> int:
    """Compute Q(n) in O(log n) time using 2-adic valuation reductions and Legendre loop."""
    k1 = (n + 1) // 2
    k2 = n // 2

    # Legendre identity: sum_{k=1..K} v_2(k) = sum_{j>=1} floor(K / 2^j)
    odd_v2_sum = 0
    shift = 1
    while (k1 >> shift) > 0:
        odd_v2_sum += k1 >> shift
        shift += 1

    even_v2_sum = 0
    shift = 1
    while (k2 >> shift) > 0:
        even_v2_sum += k2 >> shift
        shift += 1

    odd_sum = m * odd_v2_sum
    even_sum = even_v2_sum

    return odd_sum + even_sum


if __name__ == "__main__":
    print(solve())
