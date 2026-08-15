"""Project Euler Problem 412: Gnomon Numbering.

Find LC(10000, 5000) mod 76543217, where LC(m, n) is the number of standard Young tableaux
of an m x m square grid with top-right n x n corner removed.
"""

MOD = 76543217


def solve(m_val: int = 10000, n_val: int = 5000, mod: int = MOD) -> int:
    """Compute LC(m_val, n_val) mod mod using the Frame-Robinson-Thrall Hook Length formula."""
    k_val = m_val - n_val
    max_small = 2 * m_val - 1

    fac = [1] * (max_small + 1)
    for i in range(1, max_small + 1):
        fac[i] = (fac[i - 1] * i) % mod

    invfac = [1] * (max_small + 1)
    invfac[max_small] = pow(fac[max_small], mod - 2, mod)
    for i in range(max_small, 0, -1):
        invfac[i - 1] = (invfac[i] * i) % mod

    v_a = 1
    for i in range(1, n_val):
        v_a = (v_a * fac[i]) % mod

    v_b = 1
    for i in range(1, k_val):
        v_b = (v_b * fac[i]) % mod

    v_ab = 1
    for t in range(k_val):
        v_ab = (v_ab * fac[2 * n_val + t]) % mod
        v_ab = (v_ab * invfac[n_val + t]) % mod

    d_inv = 1
    for a in range(k_val, m_val):
        d_inv = (d_inv * invfac[a]) % mod
    for b in range(m_val + n_val, 2 * m_val):
        d_inv = (d_inv * invfac[b]) % mod

    # Dynamic factorial of total cell count N = m^2 - n^2
    total_cells = m_val * m_val - n_val * n_val
    total_fact = 1
    for i in range(2, total_cells + 1):
        total_fact = (total_fact * i) % mod

    res = total_fact
    res = (res * v_a) % mod
    res = (res * v_b) % mod
    res = (res * v_ab) % mod
    res = (res * d_inv) % mod

    return res


if __name__ == "__main__":
    print(solve())
