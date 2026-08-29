"""Project Euler Problem 490: Jumping Frog.

Find S(10^14) mod 10^9, where S(L) = sum_{n=1..L} f(n)^3,
and f(n) is the number of Hamiltonian paths from 1 to n with step sizes <= 3.
"""

from typing import List

MOD = 10**9
F_INIT = [1, 1, 1, 2, 6, 14, 28, 56]


def _build_companion_matrix(mod: int) -> List[List[int]]:
    coeff = [2, -1, 2, 1, 1, 0, -1, -1]
    matrix_a = [[0] * 8 for _ in range(8)]
    matrix_a[0] = [(c % mod) for c in coeff]
    for i in range(1, 8):
        matrix_a[i][i - 1] = 1
    return matrix_a


def _mat_mul8(
    matrix_a: List[List[int]], matrix_b: List[List[int]], mod: int
) -> List[List[int]]:
    res = [[0] * 8 for _ in range(8)]
    for i in range(8):
        ai = matrix_a[i]
        for k in range(8):
            aik = ai[k]
            if aik:
                bk = matrix_b[k]
                for j in range(8):
                    res[i][j] = (res[i][j] + aik * bk[j]) % mod
    return res


def _tensor_from_vec(v: List[int], mod: int) -> List[int]:
    tensor = [0] * 512
    vv = [x % mod for x in v]
    for i in range(8):
        vi = vv[i]
        for j in range(8):
            vij = (vi * vv[j]) % mod
            base = i * 64 + j * 8
            for k in range(8):
                tensor[base + k] = (vij * vv[k]) % mod
    return tensor


def _tensor_transform(
    matrix_m: List[List[int]], tensor_t: List[int], mod: int
) -> List[int]:
    u_tensor = [0] * 512
    for j in range(8):
        for k in range(8):
            base_jk = j * 8 + k
            for i in range(8):
                row = matrix_m[i]
                s = 0
                for p in range(8):
                    s += row[p] * tensor_t[p * 64 + base_jk]
                u_tensor[i * 64 + base_jk] = s % mod

    v_tensor = [0] * 512
    for i in range(8):
        ioff = i * 64
        for k in range(8):
            for j in range(8):
                row = matrix_m[j]
                s = 0
                for q in range(8):
                    s += row[q] * u_tensor[ioff + q * 8 + k]
                v_tensor[ioff + j * 8 + k] = s % mod

    w_tensor = [0] * 512
    for i in range(8):
        ioff = i * 64
        for j in range(8):
            joff = ioff + j * 8
            for k in range(8):
                row = matrix_m[k]
                s = 0
                for r in range(8):
                    s += row[r] * v_tensor[joff + r]
                w_tensor[joff + k] = s % mod

    return w_tensor


def _sum_cubes_from_state(
    u: List[int], length: int, matrix_a: List[List[int]], mod: int
) -> int:
    if length <= 0:
        return 0

    blocks_p = []
    blocks_t = []
    p_mat = [row[:] for row in matrix_a]
    t_tensor = _tensor_from_vec(u, mod)
    m = 1

    while m <= length:
        blocks_p.append(p_mat)
        blocks_t.append(t_tensor)
        pt = _tensor_transform(p_mat, t_tensor, mod)
        t_tensor = [(t_tensor[i] + pt[i]) % mod for i in range(512)]
        p_mat = _mat_mul8(p_mat, p_mat, mod)
        m <<= 1

    q_mat = [[0] * 8 for _ in range(8)]
    for i in range(8):
        q_mat[i][i] = 1

    acc = [0] * 512
    bit = 0
    rem = length
    while rem:
        if rem & 1:
            contrib = _tensor_transform(q_mat, blocks_t[bit], mod)
            acc = [(acc[i] + contrib[i]) % mod for i in range(512)]
            q_mat = _mat_mul8(q_mat, blocks_p[bit], mod)
        rem >>= 1
        bit += 1

    return acc[0]


def solve(limit_l: int = 10**14, mod: int = MOD) -> int:
    """Compute S(L) mod mod using order-8 linear recurrence tensor doubling."""
    if limit_l <= 0:
        return 0
    if limit_l <= 8:
        return sum((F_INIT[i] ** 3) % mod for i in range(limit_l)) % mod

    prefix = sum((F_INIT[i] ** 3) % mod for i in range(7)) % mod
    u_state = [
        F_INIT[7],
        F_INIT[6],
        F_INIT[5],
        F_INIT[4],
        F_INIT[3],
        F_INIT[2],
        F_INIT[1],
        F_INIT[0],
    ]
    matrix_a = _build_companion_matrix(mod)
    tail = _sum_cubes_from_state(u_state, limit_l - 7, matrix_a, mod)
    return (prefix + tail) % mod


if __name__ == "__main__":
    print(solve())
