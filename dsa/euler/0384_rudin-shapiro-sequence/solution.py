"""Project Euler Problem 384: Rudin-Shapiro Sequence.

Find sum_{t=2..45} GF(t), where GF(t) = g(F(t), F(t-1)) and g(t, c) is the index of the c-th
occurrence of t in the summatory Rudin-Shapiro sequence s(n).
"""

from typing import List


def g_index(t: int, c: int) -> int:
    """Compute the 0-based index where value t occurs for the c-th time in s(n) in O(log t)."""
    if t == 1:
        return 0

    h = 1 << (t.bit_length() - 1)  # highest power of 2 <= t
    d = t - h

    if d == 0:
        if c <= t // 2:
            return (t * t // 4) + g_index(t // 2, c)
        return (t * t // 2) + g_index(t, c - (t // 2))

    if c > h:
        return (h * h) + g_index(2 * h - d, c - h)
    if c > h - d:
        return (h * h) + g_index(d, c + d - h)
    if c <= d:
        return (h * h // 2) + g_index(d, c)
    return (h * h // 2) + g_index(2 * h - t, c)


def solve(max_t: int = 45) -> int:
    """Compute sum_{t=2..max_t} g(F(t), F(t-1)) using O(log F(t)) recursive self-similarity."""
    # Generate Fibonacci numbers with F(0)=1, F(1)=1
    fib: List[int] = [1, 1]
    for _ in range(2, max_t + 1):
        fib.append(fib[-1] + fib[-2])

    total_sum = 0
    for t in range(2, max_t + 1):
        total_sum += g_index(fib[t], fib[t - 1])

    return total_sum


if __name__ == "__main__":
    print(solve())
