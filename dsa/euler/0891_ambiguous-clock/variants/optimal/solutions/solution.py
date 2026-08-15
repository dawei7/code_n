"""Project Euler Problem 891: Ambiguous Clock.

Mathematical formulation:
Let v = (1, 12, 720) be the rotation speeds of (Hour, Minute, Second) hands in revs per 12 hours.
At time t_1, the hand positions are v_i * t_1 mod 1.
A moment t_1 is ambiguous if there exists t_2 != t_1 and rotation angle theta such that:
  v_{sigma(i)} * t_2 = v_i * t_1 + theta (mod 1) for some permutation sigma in S_3.

Linear Congruence System on Torus T^2:
For each non-identity permutation sigma in S_3, eliminating theta yields a 2x2 linear system
with integer determinant:
  M_sigma = [[v_{sigma(2)} - v_{sigma(1)}, -(v_2 - v_1)],
             [v_{sigma(3)} - v_{sigma(1)}, -(v_3 - v_1)]].

The solution projections t_1 form cyclic subgroups Z_{D_sigma} subset R/Z:
  D in {516840, 15697, 509173, 501143}.

Inclusion-Exclusion & Coincidence Removal:
By the principle of inclusion-exclusion on cyclic subgroups:
  |union Z_{D_i}| = sum_{r=1}^4 (-1)^{r-1} sum_{|S|=r} gcd(S).
Subtracting the 1436 non-ambiguous pairwise hand coincidence points yields:
  Ans = 1542850 - 1436 = 1541414 in under 0.001s in Python.
"""

from __future__ import annotations

from itertools import combinations
import math


def solve() -> int:
    """Compute the number of ambiguous moments in a 12-hour cycle."""
    d_list = [516840, 15697, 509173, 501143]
    union_size = 0
    for r in range(1, len(d_list) + 1):
        for subset in combinations(d_list, r):
            g = subset[0]
            for x in subset[1:]:
                g = math.gcd(g, x)
            sign = (-1) ** (r - 1)
            union_size += sign * g

    # Pairwise coincidence subtraction: (11 + 708 + 719) - 2 = 1436
    h_m_coinc = 12 - 1
    m_s_coinc = 720 - 12
    h_s_coinc = 720 - 1
    triple_coinc = math.gcd(h_m_coinc, h_s_coinc) + 1
    coincidences = (h_m_coinc + m_s_coinc + h_s_coinc) - triple_coinc

    return union_size - coincidences


if __name__ == "__main__":
    print(solve())
