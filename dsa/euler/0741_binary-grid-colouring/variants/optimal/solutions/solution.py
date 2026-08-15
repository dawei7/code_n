"""Project Euler Problem 741: Binary Grid Colouring.

Find g(7^7) + g(8^8) modulo 1000000007, where g(n) is the number of 0-1 n x n grids
with exactly two 1s in every row and column, unique up to rotations and reflections (D4).
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007
_INV2 = (_MOD + 1) // 2
_INV8 = pow(8, _MOD - 2, _MOD)


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p741_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p741_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL
#define INV2 500000004ULL
#define INV8 125000001ULL

static inline uint64_t pow_mod(uint64_t base, uint64_t exp) {
    uint64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % MOD);
        base = (uint64_t)((__int128)base * base % MOD);
        exp >>= 1;
    }
    return res;
}

static void f_diag_fact(int64_t n, uint64_t *f_n, uint64_t *diag, uint64_t *fact_n) {
    if (n == 0) { *f_n = 1; *diag = 1; *fact_n = 1; return; }
    
    uint64_t fact = 1;
    uint64_t h_im2 = 1;
    uint64_t h_im1 = 0;
    
    uint64_t d0 = 1, d1 = 0, d2 = 1, d3 = 4;
    
    for (int64_t i = 1; i <= n; ++i) {
        fact = (uint64_t)((__int128)fact * i % MOD);
        
        if (i >= 2) {
            uint64_t k = i - 1;
            uint64_t h_i = ((k % MOD) * h_im1 + ((k % MOD) * INV2 % MOD) * h_im2) % MOD;
            h_im2 = h_im1;
            h_im1 = h_i;
        }
        
        if (n >= 4 && i >= 4) {
            uint64_t k = i - 1;
            uint64_t km = k % MOD;
            uint64_t term1 = (2 * km * d3) % MOD;
            uint64_t term2 = (km * ((k - 2) % MOD)) % MOD;
            term2 = (uint64_t)((__int128)term2 * d2 % MOD);
            uint64_t term3 = (km * ((k - 1) % MOD)) % MOD;
            term3 = (uint64_t)((__int128)term3 * ((k - 2) % MOD) % MOD);
            term3 = (uint64_t)((__int128)term3 * d0 % MOD);
            uint64_t new_d = (term1 + MOD - term2 + MOD - (uint64_t)((__int128)term3 * INV2 % MOD)) % MOD;
            d0 = d1; d1 = d2; d2 = d3; d3 = new_d;
        }
    }
    
    *fact_n = fact;
    *f_n = (uint64_t)((__int128)fact * h_im1 % MOD);
    if (n == 0) *diag = 1;
    else if (n == 1) *diag = 0;
    else if (n == 2) *diag = 1;
    else if (n == 3) *diag = 4;
    else *diag = d3;
}

static inline uint64_t fix_axis(int64_t n, uint64_t fact_n) {
    if (n & 1) return 0;
    return (uint64_t)((__int128)fact_n * pow_mod(INV2, n / 2) % MOD);
}

static uint64_t fix_r90(int64_t n) {
    if (n & 1) return 0;
    int64_t m = n / 2;
    if (m == 0) return 1;
    if (m == 1) return 1;
    if (m == 2) return 2;
    
    uint64_t b0 = 1, b1 = 1, b2 = 2;
    for (int64_t i = 2; i < m; ++i) {
        uint64_t im = i % MOD;
        uint64_t val = (uint64_t)((__int128)(2 * im + 1) * b2 + MOD - (uint64_t)((__int128)im * b1 % MOD) + (uint64_t)((__int128)(2 * im * ((i - 1) % MOD) % MOD) * b0 % MOD)) % MOD;
        b0 = b1; b1 = b2; b2 = val;
    }
    return b2;
}

static uint64_t fix_r180(int64_t n) {
    if (n == 0) return 1;
    if ((n & 1) == 0) {
        int64_t m = n / 2;
        if (m == 0) return 1;
        if (m == 1) return 1;
        uint64_t j_prev = 1, j_curr = 1;
        uint64_t fact = 1;
        for (int64_t i = 1; i < m; ++i) {
            uint64_t im = i % MOD;
            fact = (uint64_t)((__int128)fact * im % MOD);
            uint64_t j_next = ((4 * im + 1) * j_curr + (4 * im % MOD) * j_prev) % MOD;
            j_prev = j_curr; j_curr = j_next;
        }
        uint64_t fact_m = (uint64_t)((__int128)fact * (m % MOD) % MOD);
        return (uint64_t)((__int128)fact_m * j_curr % MOD);
    }
    
    int64_t m = (n - 1) / 2;
    if (m == 0) return 0;
    
    uint64_t fact = 1;
    uint64_t t = 0;
    uint64_t j_prev = 1, j_curr = 1;
    for (int64_t i = 1; i <= m; ++i) {
        uint64_t im = i % MOD;
        fact = (uint64_t)((__int128)fact * im % MOD);
        t = ((4 * im % MOD) * t + (2 * im % MOD) * j_prev) % MOD;
        if (i < m) {
            uint64_t j_next = ((4 * im + 1) * j_curr + (4 * im % MOD) * j_prev) % MOD;
            j_prev = j_curr; j_curr = j_next;
        }
    }
    return (uint64_t)((__int128)fact * t % MOD);
}

uint64_t g_c(int64_t n) {
    uint64_t f_n, diag, fact_n;
    f_diag_fact(n, &f_n, &diag, &fact_n);
    uint64_t axis = fix_axis(n, fact_n);
    uint64_t r180 = fix_r180(n);
    uint64_t r90 = fix_r90(n);
    
    uint64_t total = (f_n + r180 + 2 * r90 + 2 * axis + 2 * diag) % MOD;
    return (uint64_t)((__int128)total * INV8 % MOD);
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
    lib.g_c.restype = ctypes.c_uint64
    lib.g_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n1: int = 823543, n2: int = 16777216) -> int:
    """Compute (g(7^7) + g(8^8)) mod 1000000007 using Burnside Lemma D4 orbital counting."""
    lib = _get_compiled_lib()
    res = 0
    for n in (n1, n2):
        val = int(lib.g_c(n))
        res = (res + val) % _MOD
    return res


if __name__ == "__main__":
    print(solve())
