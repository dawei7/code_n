"""Project Euler Problem 751: Concatenation Coincidence.

Find the only value of theta starting at a_1 = 2 such that the generated concatenation
tau = a_1.a_2 a_3 a_4 ... equals theta, rounded to 24 places after the decimal point.
"""

from decimal import Decimal, getcontext


def _get_tau(theta_val: Decimal, num_digits: int = 30) -> str:
    b = theta_val
    a1 = int(b)
    res = [str(a1), "."]

    current_digits = 0
    while current_digits < num_digits:
        floor_b = int(b)
        b = Decimal(floor_b) * (b - Decimal(floor_b) + Decimal(1))
        a_n = int(b)
        s = str(a_n)
        res.append(s)
        current_digits += len(s)

    return "".join(res)[: num_digits + 2]


def solve(target_digits: int = 24) -> str:
    """Compute theta using high-precision fixed point contraction iteration."""
    getcontext().prec = 100

    theta_str = "2.0"
    for _ in range(50):
        theta_val = Decimal(theta_str)
        tau_str = _get_tau(theta_val, target_digits + 6)
        if tau_str[: target_digits + 2] == theta_str[: target_digits + 2]:
            break
        theta_str = tau_str

    return theta_str[: target_digits + 2]


if __name__ == "__main__":
    print(solve())
