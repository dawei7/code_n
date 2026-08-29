"""Project Euler Problem 481: Chef Showdown.

Find E(14) rounded to 8 decimal places, the expected number of dishes cooked
in a turn-based strategic cooking competition with 14 chefs having Fibonacci skills.
"""

from typing import List, Tuple


def _next_chef(i: int, mask: int) -> int:
    higher = mask & ~((1 << (i + 1)) - 1)
    if higher:
        return (higher & -higher).bit_length() - 1
    return (mask & -mask).bit_length() - 1


def _fib_skills(n: int) -> List[float]:
    fib = [0] * (n + 2)
    fib[1] = fib[2] = 1
    for i in range(3, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    denom = fib[n + 1]
    return [fib[i + 1] / denom for i in range(n)]


def solve(n: int = 14) -> str:
    """Compute E(n) rounded to 8 decimal places via subset DP and cyclic Markov systems."""
    skills = _fib_skills(n)
    full_mask = (1 << n) - 1

    w_table = [
        [[0.0 for _ in range(n)] for _ in range(n)] for _ in range(1 << n)
    ]
    e_table = [[0.0 for _ in range(n)] for _ in range(1 << n)]

    for i in range(n):
        mask = 1 << i
        w_table[mask][i][i] = 1.0
        e_table[mask][i] = 0.0

    masks_by_size: List[List[int]] = [[] for _ in range(n + 1)]
    for mask in range(1, 1 << n):
        masks_by_size[mask.bit_count()].append(mask)

    for size in range(2, n + 1):
        for mask in masks_by_size[size]:
            chefs = [i for i in range(n) if (mask >> i) & 1]
            m = len(chefs)
            pos = {chef: idx for idx, chef in enumerate(chefs)}

            a_arr = [0.0] * m
            b_arr = [[0.0] * n for _ in range(m)]
            c_arr = [0.0] * m

            for t, i in enumerate(chefs):
                p = skills[i]
                a_arr[t] = 1.0 - p

                best = -1.0
                tied: List[int] = []

                for j in chefs:
                    if j == i:
                        continue
                    mask2 = mask & ~(1 << j)
                    turn2 = _next_chef(i, mask2)
                    val = w_table[mask2][turn2][i]
                    if val > best + 1e-15:
                        best = val
                        tied = [j]
                    elif abs(val - best) <= 1e-15:
                        tied.append(j)

                if len(tied) == 1:
                    jstar = tied[0]
                else:
                    pi = pos[i]

                    def dist(cand_j: int) -> int:
                        pj = pos[cand_j]
                        d = pj - pi
                        if d <= 0:
                            d += m
                        return d

                    jstar = min(tied, key=dist)

                mask2 = mask & ~(1 << jstar)
                turn2 = _next_chef(i, mask2)

                small_w = w_table[mask2][turn2]
                b_arr[t] = [p * x for x in small_w]
                c_arr[t] = p * e_table[mask2][turn2]

            a_coeff = [0.0] * m
            b_const = [[0.0] * n for _ in range(m)]
            a_next = 1.0
            b_next = [0.0] * n

            for t in range(m - 1, -1, -1):
                a_coeff[t] = a_arr[t] * a_next
                bt = b_const[t]
                for k in range(n):
                    bt[k] = a_arr[t] * b_next[k] + b_arr[t][k]
                a_next = a_coeff[t]
                b_next = bt

            denom = 1.0 - a_coeff[0]
            w0 = [b_const[0][k] / denom for k in range(n)]

            for t, chef in enumerate(chefs):
                w_table[mask][chef] = [
                    a_coeff[t] * w0[k] + b_const[t][k] for k in range(n)
                ]

            ae_coeff = [0.0] * m
            be_const = [0.0] * m
            ae_next = 1.0
            be_next = 0.0

            for t in range(m - 1, -1, -1):
                ae_coeff[t] = a_arr[t] * ae_next
                be_const[t] = 1.0 + a_arr[t] * be_next + c_arr[t]
                ae_next = ae_coeff[t]
                be_next = be_const[t]

            denom_e = 1.0 - ae_coeff[0]
            e0 = be_const[0] / denom_e

            for t, chef in enumerate(chefs):
                e_table[mask][chef] = ae_coeff[t] * e0 + be_const[t]

    ans = e_table[full_mask][0]
    return f"{ans:.8f}"


if __name__ == "__main__":
    print(solve())
