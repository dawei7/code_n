"""Project Euler Problem 716: Grid Graphs.

Find C(10000, 20000) mod 1000000007, where C(H, W) is the sum of the number of strongly connected
components across all 2^(H+W) grid digraph orientations on an H x W lattice.
"""

_MOD = 1_000_000_007


def solve(h: int = 10_000, w: int = 20_000, mod: int = _MOD) -> int:
    """Compute C(H, W) modulo 1000000007 using closed-form symmetric SCC polynomial reduction."""
    pow2h = 1
    for _ in range(h):
        pow2h = (pow2h * 2) % mod

    pow2w = 1
    for _ in range(w):
        pow2w = (pow2w * 2) % mod

    pow2hw = (pow2h * pow2w) % mod

    term1 = (9 * pow2hw) % mod
    term2 = (2 * (h % mod) * (w % mod)) % mod
    term2 = (term2 * ((pow2h + pow2w + 1) % mod)) % mod

    term3 = (-8 * ((w % mod) * pow2h + (h % mod) * pow2w)) % mod
    term4 = (-10 * (pow2h + pow2w)) % mod
    term5 = (10 * ((h + w + 1) % mod)) % mod

    ans = (term1 + term2 + term3 + term4 + term5) % mod
    return ans


if __name__ == "__main__":
    print(solve())
