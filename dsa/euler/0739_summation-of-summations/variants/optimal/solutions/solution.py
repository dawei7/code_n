"""Project Euler Problem 739: Summation of Summations.

Find f(10^8) modulo 1000000007, where f(n) is the final term obtained from repeated
prefix summations starting from the Lucas sequence of length n.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p739_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p739_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

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

static inline uint64_t inv_mod(uint64_t n) {
    return pow_mod(n, MOD - 2);
}

static uint32_t L[100000005];

int64_t solve_c(int n) {
    if (n <= 1) return 0;
    
    L[1] = 1;
    L[2] = 3;
    for (int k = 3; k <= n; ++k) {
        uint32_t val = L[k - 1] + L[k - 2];
        if (val >= MOD) val -= MOD;
        L[k] = val;
    }
    
    uint64_t inv_n_minus_1 = inv_mod(n - 1);
    
    uint32_t *inv_arr = (uint32_t *)malloc((n + 5) * sizeof(uint32_t));
    inv_arr[1] = 1;
    for (int i = 2; i <= n; ++i) {
        inv_arr[i] = (uint32_t)((uint64_t)(MOD - MOD / i) * inv_arr[MOD % i] % MOD);
    }
    
    uint64_t total = 0;
    uint64_t B_j = 1;
    
    for (int j = 0; j <= n - 2; ++j) {
        int k = n - j;
        uint64_t coeff = (uint64_t)(n - j - 1) * inv_n_minus_1 % MOD;
        coeff = (uint64_t)((__int128)coeff * B_j % MOD);
        
        uint64_t term = (uint64_t)((__int128)coeff * L[k] % MOD);
        total = (total + term) % MOD;
        
        uint64_t num = n + j - 1;
        uint64_t den_inv = inv_arr[j + 1];
        B_j = (uint64_t)((__int128)B_j * (num % MOD) % MOD * den_inv % MOD);
    }
    
    free(inv_arr);
    return (int64_t)total;
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
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(n: int = 100_000_000) -> int:
    """Compute f(n) modulo 1000000007 using Catalan ballot triangle coefficients on Lucas sequence."""
    if n <= 100:
        lucas = [0, 1, 3]
        for _ in range(3, n + 1):
            lucas.append((lucas[-1] + lucas[-2]) % _MOD)

        row = lucas[1:]
        for _ in range(n - 1):
            new_row = []
            cur = 0
            for val in row[1:]:
                cur = (cur + val) % _MOD
                new_row.append(cur)
            row = new_row
        return row[0]

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
