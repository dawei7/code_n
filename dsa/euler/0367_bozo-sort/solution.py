"""Project Euler Problem 367: Bozo Sort.

Find the expected number of 3-element random shuffles to sort a random permutation of 11 elements,
rounded to the nearest integer.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import factorial
from typing import Dict, Generator, List, Tuple


def solve(n: int = 11) -> int:
    """Compute the expected number of shuffles for Bozo sort on S_n via conjugacy class Markov chain."""
    if n <= 1:
        return 0

    # 1. Generate all integer partitions of n (conjugacy classes of S_n)
    def get_partitions(
        rem: int, max_val: int
    ) -> Generator[Tuple[int, ...], None, None]:
        if rem == 0:
            yield ()
            return
        for first in range(min(rem, max_val), 0, -1):
            for rest in get_partitions(rem - first, first):
                yield (first,) + rest

    partitions = list(get_partitions(n, n))
    num_states = len(partitions)
    p_to_idx: Dict[Tuple[int, ...], int] = {
        p: i for i, p in enumerate(partitions)
    }

    # 2. Compute the conjugacy class sizes: |C_lambda| = n! / prod(i^k_i * k_i!)
    class_sizes: Dict[Tuple[int, ...], int] = {}
    for p in partitions:
        counts = Counter(p)
        denom = 1
        for length, cnt in counts.items():
            denom *= (length**cnt) * factorial(cnt)
        class_sizes[p] = factorial(n) // denom

    # 3. Canonical representative permutation for each cycle type
    def canonical_perm(p: Tuple[int, ...]) -> List[int]:
        perm = list(range(n))
        curr = 0
        for length in p:
            for i in range(length - 1):
                perm[curr + i] = curr + i + 1
            perm[curr + length - 1] = curr
            curr += length
        return perm

    def get_cycle_type(perm: List[int]) -> Tuple[int, ...]:
        visited = [False] * n
        cycles: List[int] = []
        for i in range(n):
            if not visited[i]:
                curr = i
                length = 0
                while not visited[curr]:
                    visited[curr] = True
                    curr = perm[curr]
                    length += 1
                cycles.append(length)
        return tuple(sorted(cycles, reverse=True))

    # 4. Construct the linear system (I - P) E = 1
    all_triplets = list(combinations(range(n), 3))
    all_perms_3 = list(permutations(range(3)))
    tot_trans = len(all_triplets) * len(all_perms_3)

    matrix_a = [[0.0] * num_states for _ in range(num_states)]
    vector_b = [0.0] * num_states

    identity_type = tuple([1] * n)

    for p, idx in p_to_idx.items():
        if p == identity_type:
            matrix_a[idx][idx] = 1.0
            vector_b[idx] = 0.0
            continue

        matrix_a[idx][idx] = 1.0
        vector_b[idx] = 1.0
        rep = canonical_perm(p)

        trans_counts: Dict[Tuple[int, ...], int] = defaultdict(int)
        for i, j, k in all_triplets:
            vals = [rep[i], rep[j], rep[k]]
            for p3 in all_perms_3:
                new_p = list(rep)
                new_p[i] = vals[p3[0]]
                new_p[j] = vals[p3[1]]
                new_p[k] = vals[p3[2]]
                dst = get_cycle_type(new_p)
                trans_counts[dst] += 1

        for dst, count in trans_counts.items():
            prob = count / tot_trans
            matrix_a[idx][p_to_idx[dst]] -= prob

    # 5. Gaussian elimination solver
    for i in range(num_states):
        pivot = i
        while pivot < num_states and abs(matrix_a[pivot][i]) < 1e-12:
            pivot += 1
        matrix_a[i], matrix_a[pivot] = matrix_a[pivot], matrix_a[i]
        vector_b[i], vector_b[pivot] = vector_b[pivot], vector_b[i]

        factor = matrix_a[i][i]
        for j in range(i, num_states):
            matrix_a[i][j] /= factor
        vector_b[i] /= factor

        for r in range(num_states):
            if r != i and abs(matrix_a[r][i]) > 1e-12:
                row_factor = matrix_a[r][i]
                for j in range(i, num_states):
                    matrix_a[r][j] -= row_factor * matrix_a[i][j]
                vector_b[r] -= row_factor * vector_b[i]

    # 6. Weighted average over the uniform distribution on S_n
    total_expected = sum(
        class_sizes[p] * vector_b[p_to_idx[p]] for p in partitions
    )
    avg_expected = total_expected / factorial(n)

    return round(avg_expected)


if __name__ == "__main__":
    print(solve())
