"""Project Euler Problem 589: Poohsticks Marathon.

Find S(100) rounded to 2 decimal places, where S(k) is the sum of expected
game durations E(m, n) for 2 <= m <= k and 1 <= n < m.
"""

from math import isfinite
from typing import List, Tuple


def _arith_sum(a: int, b: int) -> float:
    if a > b:
        return 0.0
    n = b - a + 1
    return (a + b) * n / 2.0


def _expected_min_consecutive(low: int, high: int) -> float:
    length = high - low + 1
    denom = length * length
    total = 0.0
    for i in range(length):
        v = low + i
        w = (2 * length - 2 * i - 1) / denom
        total += v * w
    return total


def _gauss_solve(a_mat: List[List[float]], b_vec: List[float]) -> List[float]:
    n = len(a_mat)
    for i in range(n):
        a_mat[i].append(b_vec[i])

    for col in range(n):
        piv = col
        best = abs(a_mat[col][col])
        for r in range(col + 1, n):
            v = abs(a_mat[r][col])
            if v > best:
                best = v
                piv = r
        if best < 1e-18:
            raise RuntimeError("Singular/ill-conditioned system")

        if piv != col:
            a_mat[col], a_mat[piv] = a_mat[piv], a_mat[col]

        row = a_mat[col]
        inv = 1.0 / row[col]
        for j in range(col, n + 1):
            row[j] *= inv

        for r in range(n):
            if r == col:
                continue
            factor = a_mat[r][col]
            if factor == 0.0:
                continue
            rr = a_mat[r]
            for j in range(col, n + 1):
                rr[j] -= factor * row[j]

    return [a_mat[i][n] for i in range(n)]


def _compute_c1_direct(n: int, m: int) -> Tuple[List[float], float]:
    length = m - n + 1
    a_low = n + 5
    a_high = m + 5
    m_val = a_high

    emin_a = _expected_min_consecutive(a_low, a_high)
    k = length / (length - 1.0)
    inv_l = 1.0 / length

    b0_const = k * emin_a
    b0_coeff = [0.0] * (m_val + 1)
    for d in range(1, min(length, m_val + 1)):
        if d <= length - 1:
            b0_coeff[d] = k * (2.0 / (length * length)) * (length - d)

    q0 = [0.0] * (m_val + 1)
    p0 = [[0.0] * (m_val + 1) for _ in range(m_val + 1)]

    for y in range(1, m_val + 1):
        lt_low = a_low
        lt_high = min(a_high, y - 1)
        sum_lt_a = _arith_sum(lt_low, lt_high)

        if lt_low <= lt_high:
            j_lo = y - lt_high
            j_hi = y - lt_low
            for j in range(j_lo, j_hi + 1):
                if 1 <= j <= m_val:
                    p0[y][j] += inv_l

        gt_low = max(a_low, y + 1)
        gt_high = a_high
        count_gt = max(0, gt_high - gt_low + 1)
        base_gt = count_gt * y

        if gt_low <= gt_high:
            j_lo = gt_low - y
            j_hi = gt_high - y
            for j in range(j_lo, j_hi + 1):
                if 1 <= j <= m_val:
                    p0[y][j] += inv_l

        eq = a_low <= y <= a_high
        q = (sum_lt_a + base_gt + (y if eq else 0.0)) * inv_l
        if eq:
            q += b0_const * inv_l
            for d in range(1, min(length, m_val + 1)):
                if d <= length - 1:
                    p0[y][d] += b0_coeff[d] * inv_l

        q0[y] = q

    pref_q = [0.0] * (m_val + 1)
    s = 0.0
    for y in range(1, m_val + 1):
        s += q0[y]
        pref_q[y] = s

    pref_p = [[0.0] * (m_val + 1) for _ in range(m_val + 1)]
    for j in range(1, m_val + 1):
        s = 0.0
        col = pref_p[j]
        for y in range(1, m_val + 1):
            s += p0[y][j]
            col[y] = s

    w = [0.0] * (m_val + 1)
    for d in range(1, min(length, m_val + 1)):
        if d <= length - 1:
            w[d] = length - d

    sum_w_q = 0.0
    for d in range(1, min(length, m_val + 1)):
        if d <= length - 1:
            sum_w_q += w[d] * q0[d]

    const_b1 = k * emin_a + k * (1.0 / (length * length)) * sum_w_q

    b1 = [0.0] * (m_val + 1)
    for j in range(1, m_val + 1):
        ss = 0.0
        for d in range(1, min(length, m_val + 1)):
            if d <= length - 1:
                ss += w[d] * p0[d][j]
        b1[j] = k * (1.0 / (length * length)) * ss

    a_mat = [[0.0] * m_val for _ in range(m_val)]
    b_mat_vec = [0.0] * m_val

    for t in range(1, m_val + 1):
        lt_low = a_low
        lt_high = min(a_high, t - 1)
        sum_lt_a = _arith_sum(lt_low, lt_high)

        gt_low = max(a_low, t + 1)
        gt_high = a_high
        count_gt = max(0, gt_high - gt_low + 1)
        base_gt = count_gt * t

        eq = a_low <= t <= a_high
        const1 = (sum_lt_a + base_gt + (t if eq else 0.0)) * inv_l

        if gt_low <= gt_high:
            y_lo = gt_low - t
            y_hi = gt_high - t
            q_gt = pref_q[y_hi] - (pref_q[y_lo - 1] if y_lo > 1 else 0.0)
            for j in range(1, m_val + 1):
                p_gt = pref_p[j][y_hi] - (pref_p[j][y_lo - 1] if y_lo > 1 else 0.0)
                a_mat[t - 1][j - 1] -= inv_l * p_gt
        else:
            q_gt = 0.0

        rhs = const1 + inv_l * q_gt + (inv_l * const_b1 if eq else 0.0)
        b_mat_vec[t - 1] = rhs
        a_mat[t - 1][t - 1] += 1.0

        if eq:
            for j in range(1, m_val + 1):
                a_mat[t - 1][j - 1] -= inv_l * b1[j]

    sol = _gauss_solve([row[:] for row in a_mat], b_mat_vec[:])

    c1 = [0.0] * (m_val + 1)
    for j in range(1, m_val + 1):
        c1[j] = sol[j - 1]

    ss = 0.0
    for d in range(1, length):
        ss += (length - d) * 2.0 * c1[d]
    b0 = k * (emin_a + ss / (length * length))

    return c1, b0


def _compute_c1_iterative(
    n: int, m: int, max_iter: int = 2000, tol: float = 1e-12
) -> Tuple[List[float], float]:
    length = m - n + 1
    a_low = n + 5
    a_high = m + 5
    m_val = a_high

    emin_a = _expected_min_consecutive(a_low, a_high)
    k = length / (length - 1.0)

    def compute_b0(c1_arr: List[float]) -> float:
        ss = 0.0
        for d in range(1, length):
            ss += (length - d) * 2.0 * c1_arr[d]
        return k * (emin_a + ss / (length * length))

    def compute_b1(c0_arr: List[float]) -> float:
        ss = 0.0
        for d in range(1, length):
            ss += (length - d) * c0_arr[d]
        return k * (emin_a + ss / (length * length))

    def prefix(arr: List[float]) -> List[float]:
        p = [0.0] * (m_val + 1)
        s_val = 0.0
        for i in range(1, m_val + 1):
            s_val += arr[i]
            p[i] = s_val
        return p

    inv_l = 1.0 / length
    mean_a = (a_low + a_high) / 2.0

    c1 = [0.0] * (m_val + 1)
    c0 = [0.0] * (m_val + 1)
    for x in range(1, m_val + 1):
        c1[x] = mean_a + min(mean_a, x)
        c0[x] = mean_a + x

    w_factor = 1.15

    for _ in range(max_iter):
        pref1 = prefix(c1)
        b0 = compute_b0(c1)
        new_c0 = [0.0] * (m_val + 1)
        for x in range(1, m_val + 1):
            lt_low = a_low
            lt_high = min(a_high, x - 1)
            sum_lt_a = _arith_sum(lt_low, lt_high)
            sum_lt_c = 0.0
            if lt_low <= lt_high:
                y_lo = x - lt_high
                y_hi = x - lt_low
                sum_lt_c = pref1[y_hi] - (pref1[y_lo - 1] if y_lo > 1 else 0.0)

            gt_low = max(a_low, x + 1)
            gt_high = a_high
            count_gt = max(0, gt_high - gt_low + 1)
            base_gt = count_gt * x
            sum_gt_c = 0.0
            if gt_low <= gt_high:
                y_lo = gt_low - x
                y_hi = gt_high - x
                sum_gt_c = pref1[y_hi] - (pref1[y_lo - 1] if y_lo > 1 else 0.0)

            eq = a_low <= x <= a_high
            tot = (
                sum_lt_a
                + sum_lt_c
                + base_gt
                + sum_gt_c
                + (x + b0 if eq else 0.0)
            )
            new_c0[x] = tot * inv_l

        for x in range(1, m_val + 1):
            c0[x] = c0[x] + w_factor * (new_c0[x] - c0[x])

        pref0 = prefix(c0)
        b1 = compute_b1(c0)
        new_c1 = [0.0] * (m_val + 1)
        for x in range(1, m_val + 1):
            lt_low = a_low
            lt_high = min(a_high, x - 1)
            sum_lt_a = _arith_sum(lt_low, lt_high)

            gt_low = max(a_low, x + 1)
            gt_high = a_high
            count_gt = max(0, gt_high - gt_low + 1)
            base_gt = count_gt * x
            sum_gt_c = 0.0
            if gt_low <= gt_high:
                y_lo = gt_low - x
                y_hi = gt_high - x
                sum_gt_c = pref0[y_hi] - (pref0[y_lo - 1] if y_lo > 1 else 0.0)

            eq = a_low <= x <= a_high
            tot = sum_lt_a + base_gt + sum_gt_c + (x + b1 if eq else 0.0)
            new_c1[x] = tot * inv_l

        err = 0.0
        for x in range(1, m_val + 1):
            v = c1[x] + w_factor * (new_c1[x] - c1[x])
            if not isfinite(v):
                raise RuntimeError("Diverged")
            err = max(err, abs(v - c1[x]))
            c1[x] = v

        if err < tol:
            b0 = compute_b0(c1)
            return c1, b0

    raise RuntimeError("No convergence")


def _expected_game(m: int, n: int) -> float:
    length = m - n + 1
    if length >= 25:
        try:
            c1, b0 = _compute_c1_iterative(n, m)
        except Exception:
            c1, b0 = _compute_c1_direct(n, m)
    else:
        c1, b0 = _compute_c1_direct(n, m)

    emin0 = _expected_min_consecutive(n, m)
    s_val = b0 * (1.0 / length)
    denom = length * length
    for d in range(1, length):
        prob = 2.0 * (length - d) / denom
        s_val += prob * c1[d]

    return emin0 + s_val


def solve(k_bound: int = 100) -> str:
    """Compute S(k_bound) as a formatted float with 2 decimal places."""
    total = 0.0
    for m in range(2, k_bound + 1):
        for n in range(1, m):
            total += _expected_game(m, n)
    return f"{total:.2f}"


if __name__ == "__main__":
    print(solve())
