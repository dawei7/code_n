"""Project Euler Problem 740: Secret Santa.

Find q(100) rounded to 10 decimal places, where q(n) is the probability that the last
person gets at least one slip with their own name in the two-slip Secret Santa process.
"""

from collections import defaultdict
from typing import DefaultDict, Dict, Tuple

State = Tuple[int, int, int, int]


def solve(n: int = 100) -> str:
    """Compute q(n) using state-compressed Markov chain dynamic programming."""
    dist: Dict[State, float] = {(0, n - 1, 2, 0): 1.0}

    for t in range(n - 1):
        m = (n - 1) - t
        t_total = 2 * n - 2 * t

        newdist: DefaultDict[State, float] = defaultdict(float)

        for (u1, u2, k, sp), prob in dist.items():
            u0 = m - u1 - u2

            for s, cnt in ((0, u0), (1, u1), (2, u2)):
                if cnt == 0:
                    continue
                p_actor = prob * (cnt / m)

                uu1, uu2 = u1, u2
                if s == 1:
                    uu1 -= 1
                elif s == 2:
                    uu2 -= 1

                c1 = t_total - s
                inv_c1 = 1.0 / c1

                first_outcomes = []
                if k:
                    first_outcomes.append((k * inv_c1, uu1, uu2, k - 1, sp))
                if uu1:
                    first_outcomes.append((uu1 * inv_c1, uu1 - 1, uu2, k, sp))
                if uu2:
                    first_outcomes.append(
                        (2 * uu2 * inv_c1, uu1 + 1, uu2 - 1, k, sp)
                    )
                if sp:
                    first_outcomes.append((sp * inv_c1, uu1, uu2, k, sp - 1))

                for p1, u1_1, u2_1, k_1, sp_1 in first_outcomes:
                    c2 = (t_total - 1) - s
                    inv_c2 = 1.0 / c2

                    if k_1:
                        sp_new = sp_1 + s
                        newdist[(u1_1, u2_1, k_1 - 1, sp_new)] += (
                            p_actor * p1 * (k_1 * inv_c2)
                        )
                    if u1_1:
                        sp_new = sp_1 + s
                        newdist[(u1_1 - 1, u2_1, k_1, sp_new)] += (
                            p_actor * p1 * (u1_1 * inv_c2)
                        )
                    if u2_1:
                        sp_new = sp_1 + s
                        newdist[(u1_1 + 1, u2_1 - 1, k_1, sp_new)] += (
                            p_actor * p1 * (2 * u2_1 * inv_c2)
                        )
                    if sp_1:
                        sp_new = (sp_1 - 1) + s
                        newdist[(u1_1, u2_1, k_1, sp_new)] += (
                            p_actor * p1 * (sp_1 * inv_c2)
                        )

        dist = newdist

    ans = sum(prob for (u1, u2, k, sp), prob in dist.items() if k > 0)
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
