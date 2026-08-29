"""Project Euler Problem 470: Super Ramvok.

Find F(20) = sum_{4<=d<=20} sum_{0<=c<=20} S(d, c),
the expected total profit of Super Ramvok across fair d-sided dice and cost constants c,
rounded to the nearest integer.
"""

from math import comb
from typing import List


def _gauss_jordan_inverse(mat: List[List[float]]) -> List[List[float]]:
    dim = len(mat)
    aug = [row[:] + [0.0] * dim for row in mat]
    for i in range(dim):
        aug[i][dim + i] = 1.0

    for col in range(dim):
        pivot = col
        best = abs(aug[pivot][col])
        for r in range(col + 1, dim):
            val = abs(aug[r][col])
            if val > best:
                best = val
                pivot = r

        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]

        piv = aug[col][col]
        invp = 1.0 / piv
        rowc = aug[col]
        for j in range(2 * dim):
            rowc[j] *= invp

        for r in range(dim):
            if r == col:
                continue
            rowr = aug[r]
            factor = rowr[col]
            if factor == 0.0:
                continue
            for j in range(2 * dim):
                rowr[j] -= factor * rowc[j]

    return [row[dim:] for row in aug]


def _visit_counts_by_weight(d: int) -> List[float]:
    dim = d
    q_mat = [[0.0] * dim for _ in range(dim)]

    for k in range(1, d + 1):
        idx = k - 1
        if k == d:
            q_mat[idx][d - 2] = 1.0
        else:
            down = k / d
            up = (d - k) / d
            if k > 1:
                q_mat[idx][k - 2] = down
            if k < d:
                q_mat[idx][k] = up

    a_mat = [[0.0] * dim for _ in range(dim)]
    for i in range(dim):
        a_mat[i][i] = 1.0
        rowq = q_mat[i]
        rowa = a_mat[i]
        for j in range(dim):
            rowa[j] -= rowq[j]

    n_mat = _gauss_jordan_inverse(a_mat)
    start_row = n_mat[d - 1]
    v_vec = [0.0] * (d + 1)
    for k in range(1, d + 1):
        v_vec[k] = start_row[k - 1]
    return v_vec


def _best_profits_all_integer_c_for_mask(
    mask: int, max_c: int
) -> List[float]:
    vals: List[int] = []
    cum: List[int] = []
    total = 0

    m = mask
    while m:
        lsb = m & -m
        v = lsb.bit_length()
        vals.append(v)
        total += v
        cum.append(total)
        m ^= lsb

    k = len(vals)
    maxv = vals[-1]
    best = [0.0] * (max_c + 1)
    best[0] = float(maxv)

    prev = 0.0
    p = 0

    for t in range(1, maxv + 1):
        while p < k and vals[p] < prev:
            p += 1
        low_sum = cum[p - 1] if p else 0
        sum_ge = total - low_sum
        prev = (prev * p + sum_ge) / k

        lim = int(prev / t)
        if lim > max_c:
            lim = max_c
        for c in range(1, lim + 1):
            prof = prev - c * t
            if prof > best[c]:
                best[c] = prof

    return best


def _compute_s_list(d: int) -> List[float]:
    max_c = d
    v_vec = _visit_counts_by_weight(d)
    sum_r = [[0.0] * (max_c + 1) for _ in range(d + 1)]

    for mask in range(1, 1 << d):
        k = mask.bit_count()
        best = _best_profits_all_integer_c_for_mask(mask, max_c)
        row = sum_r[k]
        for c in range(max_c + 1):
            row[c] += best[c]

    s_res = [0.0] * (max_c + 1)
    for c in range(max_c + 1):
        tot = 0.0
        for k in range(1, d + 1):
            avg = sum_r[k][c] / comb(d, k)
            tot += v_vec[k] * avg
        s_res[c] = tot
    return s_res


def solve(n: int = 20) -> int:
    """Compute F(n) across d in [4, n] and c in [0, n] via Ehrenfest Markov chain and subset DP."""
    total_f = 0.0
    for d in range(4, n + 1):
        s_d = _compute_s_list(d)
        total_f += sum(s_d)
    return int(round(total_f))


if __name__ == "__main__":
    print(solve())
