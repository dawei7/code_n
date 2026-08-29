"""Project Euler Problem 588: Quintinomial Coefficients.

Find sum_{k=1}^{18} Q(10^k), where Q(k) is the number of odd coefficients
in the expansion of (x^4 + x^3 + x^2 + x + 1)^k.
"""

from typing import List


def _build_transitions(active: bool) -> List[List[int]]:
    digits = range(5) if active else (0,)
    trans = [[0] * 16 for _ in range(2)]
    for bit in (0, 1):
        for state in range(16):
            next_state = 0
            for c in range(4):
                if (state >> c) & 1:
                    for d in digits:
                        s = c + d
                        if (s & 1) == bit:
                            nc = s >> 1
                            next_state ^= 1 << nc
            trans[bit][state] = next_state
    return trans


_TRANS_ACTIVE = _build_transitions(True)
_TRANS_INACTIVE = _build_transitions(False)


def _q_func(k: int) -> int:
    num_bits = k.bit_length() + 3
    dp = [0] * 16
    dp[1] = 1

    for i in range(num_bits):
        trans = _TRANS_ACTIVE if ((k >> i) & 1) else _TRANS_INACTIVE
        ndp = [0] * 16
        for state, cnt in enumerate(dp):
            if cnt:
                ndp[trans[0][state]] += cnt
                ndp[trans[1][state]] += cnt
        dp = ndp

    return sum(cnt for state, cnt in enumerate(dp) if (state & 1))


def solve(max_exp: int = 18) -> int:
    """Compute sum_{m=1}^{max_exp} Q(10^m) using GF(2) carry automaton DP."""
    total = 0
    k = 10
    for _ in range(max_exp):
        total += _q_func(k)
        k *= 10
    return total


if __name__ == "__main__":
    print(solve())
