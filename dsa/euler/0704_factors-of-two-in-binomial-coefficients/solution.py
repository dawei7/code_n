"""Project Euler Problem 704: Factors of Two in Binomial Coefficients.

Find S(10^16), where S(N) = sum_{n=1}^N F(n) and F(n) = max_{0 <= m <= n} v2(binom(n, m)).
"""


def solve(n: int = 10_000_000_000_000_000) -> int:
    """Compute S(N) in O(log N) time using Kummer's theorem and Legendre's formula."""
    sum_log2 = 0
    k = 0
    while (1 << (k + 1)) <= n:
        count = 1 << k
        sum_log2 += k * count
        k += 1
    sum_log2 += k * (n - (1 << k) + 1)

    v2_fact = 0
    p = 2
    while p <= n + 1:
        v2_fact += (n + 1) // p
        p <<= 1

    num_full = (n + 1).bit_length() - 1

    ans = sum_log2 - v2_fact + num_full
    return ans


if __name__ == "__main__":
    print(solve())
