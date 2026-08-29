"""Project Euler Problem 684: Inverse Digit Sum.

Find sum_{i=2}^{90} S(f_i) mod 1000000007, where s(n) is the smallest number with digit sum n,
and S(k) = sum_{n=1}^k s(n).
"""

_MOD = 1_000_000_007


def _sum_s(k: int) -> int:
    """Compute S(k) = sum_{n=1}^k s(n) modulo 1000000007 in O(log k) time."""
    q = k // 9
    r = k % 9
    pow10_q = pow(10, q, _MOD)
    full_blocks = (6 * (pow10_q - 1) - 9 * (q % _MOD)) % _MOD
    rem_sum = (((r + 1) * (r + 2) // 2 - 1) * pow10_q - r) % _MOD
    return (full_blocks + rem_sum) % _MOD


def solve(max_i: int = 90) -> int:
    """Compute sum_{i=2}^{max_i} S(f_i) modulo 1000000007."""
    f = [0] * (max_i + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, max_i + 1):
        f[i] = f[i - 1] + f[i - 2]

    total = 0
    for i in range(2, max_i + 1):
        total = (total + _sum_s(f[i])) % _MOD

    return total


if __name__ == "__main__":
    print(solve())
