"""Project Euler 255: Rounded Square Roots

Calculate the average number of iterations required to find the rounded-square-root
of a 14-digit number (10^13 <= n < 10^14) using the modified Heron's method.
"""

from __future__ import annotations


def solve(d: int = 14) -> str:
    """Calculates the average number of iterations for all d-digit numbers

    using interval-splitting recursion over discrete quotients.
    """
    if d % 2 == 1:
        x0 = 2 * 10 ** ((d - 1) // 2)
    else:
        x0 = 7 * 10 ** ((d - 2) // 2)

    l_total = 10 ** (d - 1)
    r_total = 10**d - 1
    total_n = r_total - l_total + 1

    total_iterations = 0

    def count_iters(x: int, left: int, right: int, steps: int) -> None:
        nonlocal total_iterations
        # Quotient range q = ceil(n / x) for n in [left, right]
        q_min = (left + x - 1) // x
        q_max = (right + x - 1) // x

        # Next iterate x_next = (x + q) // 2
        x_min = (x + q_min) // 2
        x_max = (x + q_max) // 2

        for x_next in range(x_min, x_max + 1):
            q_low = 2 * x_next - x
            q_high = q_low + 1

            sub_l = max(left, (q_low - 1) * x + 1)
            sub_r = min(right, q_high * x)
            if sub_l > sub_r:
                continue

            if x_next == x:
                total_iterations += (sub_r - sub_l + 1) * steps
            else:
                count_iters(x_next, sub_l, sub_r, steps + 1)

    count_iters(x0, l_total, r_total, 1)

    avg = total_iterations / total_n
    return f"{avg:.10f}"


if __name__ == "__main__":
    print(solve())
