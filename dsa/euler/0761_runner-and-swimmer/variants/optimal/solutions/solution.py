"""Project Euler Problem 761: Runner and Swimmer.

Find the critical maximal speed V_Hexagon of the runner in a regular hexagonal pool,
below which the swimmer can always escape and above which the runner can always catch,
rounded to 8 digits after the decimal point.
"""

import math


def solve(n: int = 6) -> str:
    """Compute critical speed V_n for a regular n-gon pool using optimal control / pursuit boundary."""
    theta = math.pi / n
    tangent = math.tan(theta)

    branch = 0
    for k in range(n + 1):
        value = math.sin(k * theta) - (k + n) * tangent * math.cos(k * theta)
        if value >= 0:
            branch = k - 1
            break

    argument = 2 * math.sin(branch * theta) / ((branch + n) * tangent) - math.cos(
        branch * theta
    )
    argument = min(1.0, max(-1.0, argument))
    alpha = (branch * theta + math.acos(argument)) / 2.0
    ans = 1.0 / math.cos(alpha)
    return f"{ans:.8f}"


if __name__ == "__main__":
    print(solve())
