"""Project Euler Problem 638: Weighted Lattice Paths.

Calculate sum_{k=1}^7 C(10^k + k, 10^k + k, k) mod 1000000007, where C(a, b, k)
is the weighted area sum over lattice paths from (0, 0) to (a, b).
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_qlattice_core.dll")
    c_path = os.path.join(tmp_dir, "fast_qlattice_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#define MOD 1000000007LL

int64_t pow_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int64_t c_val_c(int64_t N, int64_t k) {
    if (k == 1) {
        int64_t num = 1, den = 1;
        for (int64_t i = 1; i <= N; ++i) {
            num = (num * ((N + i) % MOD)) % MOD;
            den = (den * (i % MOD)) % MOD;
        }
        return (num * pow_mod(den, MOD - 2)) % MOD;
    }
    
    int64_t num = 1, den = 1;
    int64_t curr_k = 1;
    for (int64_t j = 1; j <= N; ++j) {
        curr_k = (curr_k * k) % MOD;
        den = (den * (curr_k - 1)) % MOD;
    }
    for (int64_t j = N + 1; j <= 2 * N; ++j) {
        curr_k = (curr_k * k) % MOD;
        num = (num * (curr_k - 1)) % MOD;
    }
    return (num * pow_mod(den, MOD - 2)) % MOD;
}

int64_t solve_c() {
    int64_t total = 0;
    int64_t p10 = 10;
    for (int64_t k = 1; k <= 7; ++k) {
        int64_t N = p10 + k;
        int64_t val = c_val_c(N, k);
        total = (total + val) % MOD;
        p10 *= 10;
    }
    return total;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            [
                "gcc",
                "-O3",
                "-shared",
                "-static",
                "-static-libgcc",
                "-o",
                dll_path,
                c_path,
            ],
            check=True,
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.c_val_c.restype = ctypes.c_int64
    lib.c_val_c.argtypes = [ctypes.c_int64, ctypes.c_int64]
    return lib


def solve(max_k: int = 7) -> int:
    """Compute sum_{k=1}^max_k C(10^k + k, 10^k + k, k) mod 1000000007 using Gaussian q-binomials."""
    lib = _get_compiled_lib()
    if max_k == 7:
        return int(lib.solve_c())

    total = 0
    p10 = 10
    for k in range(1, max_k + 1):
        n_val = p10 + k
        val = int(lib.c_val_c(n_val, k))
        total = (total + val) % _MOD
        p10 *= 10

    return total


if __name__ == "__main__":
    print(solve())
