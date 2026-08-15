"""Project Euler Problem 368: A Kempner-like Series.

Find the sum of the modified harmonic series omitting all terms where the denominator contains
3 or more equal consecutive digits, rounded to 10 decimal places.
"""

from collections import deque
from math import comb
from typing import List, Optional, Tuple


def solve(max_prefix_len: int = 4, moment_order: int = 10) -> str:
    """Compute the sum of the Kempner-like series using automaton moment resolvents."""
    num_states = 20

    def state_info(s: int) -> Tuple[int, int]:
        return s // 2, (s % 2) + 1

    def next_state(s: int, d: int) -> Optional[int]:
        last_d, count = state_info(s)
        if d == last_d:
            if count == 2:
                return None
            return d * 2 + 1
        return d * 2 + 0

    # Precompute valid transitions from each automaton state
    transitions: List[List[Tuple[int, int]]] = []
    for s in range(num_states):
        t_list: List[Tuple[int, int]] = []
        for d in range(10):
            ns = next_state(s, d)
            if ns is not None:
                t_list.append((d, ns))
        transitions.append(t_list)

    # Solve the 20x20 linear system for the discounted moments Z_k(s)
    z_moments = [[0.0] * num_states for _ in range(moment_order + 1)]

    for k in range(moment_order + 1):
        mat_a = [[0.0] * num_states for _ in range(num_states)]
        vec_b = [0.0] * num_states

        denom_k = 10.0 ** (k + 1)

        for s in range(num_states):
            mat_a[s][s] = 1.0
            rhs = 0.0
            for d, ns in transitions[s]:
                mat_a[s][ns] -= 1.0 / denom_k

                term = (d**k) / denom_k

                for j in range(k):
                    binomial_coef = comb(k, j)
                    term += (
                        (1.0 / denom_k)
                        * binomial_coef
                        * (d ** (k - j))
                        * z_moments[j][ns]
                    )

                rhs += term
            vec_b[s] = rhs

        # Gaussian elimination
        for i in range(num_states):
            pivot = i
            while pivot < num_states and abs(mat_a[pivot][i]) < 1e-12:
                pivot += 1
            mat_a[i], mat_a[pivot] = mat_a[pivot], mat_a[i]
            vec_b[i], vec_b[pivot] = vec_b[pivot], vec_b[i]

            factor = mat_a[i][i]
            for j in range(i, num_states):
                mat_a[i][j] /= factor
            vec_b[i] /= factor

            for r in range(num_states):
                if r != i and abs(mat_a[r][i]) > 1e-12:
                    row_factor = mat_a[r][i]
                    for j in range(i, num_states):
                        mat_a[r][j] -= row_factor * mat_a[i][j]
                    vec_b[r] -= row_factor * vec_b[i]

        for s in range(num_states):
            z_moments[k][s] = vec_b[s]

    # BFS traversal to sum direct prefixes and append infinite moment tails
    total_sum = 0.0
    queue = deque()
    for d in range(1, 10):
        s = d * 2 + 0
        queue.append((d, s, 1))

    while queue:
        val, s, length = queue.popleft()
        total_sum += 1.0 / val

        if length == max_prefix_len:
            # Taylor expansion of infinite tail
            for k in range(moment_order + 1):
                sign = (-1) ** k
                term = sign * z_moments[k][s] / (val ** (k + 1))
                total_sum += term
            continue

        for next_d in range(10):
            ns = next_state(s, next_d)
            if ns is not None:
                queue.append((val * 10 + next_d, ns, length + 1))

    return f"{total_sum:.10f}"


if __name__ == "__main__":
    print(solve())
