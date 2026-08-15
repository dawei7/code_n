"""Project Euler Problem 664: An Infinite Game.

Find F(1234567), where F(n) is the maximum number of squares Peter can move a token
beyond the dividing line with initial token supply d^n on column d.
"""

import math

_SQRT5 = math.sqrt(5.0)
_PHI = (1.0 + _SQRT5) / 2.0
_LN_PHI = math.log(_PHI)
_LN_LN_PHI = math.log(_LN_PHI)


def _compute_f(n: int) -> int:
    if n == 0:
        log_phi_a = 1.0
    elif n == 1:
        log_phi_a = 3.0
    elif n == 2:
        log_phi_a = math.log(_PHI**5 + _PHI**3) / _LN_PHI
    else:
        ln_a = math.lgamma(n + 1) - (n + 1) * _LN_LN_PHI
        log_phi_a = ln_a / _LN_PHI

    rounded = round(log_phi_a)
    if abs(log_phi_a - rounded) < 1e-10:
        c_val = int(rounded)
    else:
        c_val = int(math.floor(log_phi_a) + 1)

    return 3 + c_val


def solve(n: int = 1_234_567) -> int:
    """Compute F(n) using the exponential generating function singularity analysis of geometric sums."""
    res = 0
    for val in [n]:
        res += _compute_f(val)
    return res


if __name__ == "__main__":
    print(solve())
