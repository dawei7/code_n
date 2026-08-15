"""Project Euler Problem 657: Incomplete Words.

Find I(10^7, 10^12) mod 1000000007, where I(alpha, n) is the number of incomplete words
over an alphabet of alpha letters with length <= n.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_inc_words_core.dll")
    c_path = os.path.join(tmp_dir, "fast_inc_words_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007LL

static inline int64_t pow_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int64_t solve_c(int64_t alpha, int64_t n) {
    int64_t* inv = (int64_t*)malloc((alpha + 1) * sizeof(int64_t));
    inv[1] = 1;
    for (int i = 2; i <= alpha; ++i) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }
    
    int64_t total = 0;
    int64_t comb = 1;
    int64_t exp_n_plus_1 = n + 1;
    
    for (int64_t j = 0; j < alpha; ++j) {
        int64_t term;
        if (j == 0) {
            term = 1;
        } else if (j == 1) {
            term = (n + 1) % MOD;
        } else {
            term = ((pow_mod(j, exp_n_plus_1) - 1 + MOD) % MOD) * inv[j - 1] % MOD;
        }
        
        int64_t signed_term = (comb * term) % MOD;
        if ((alpha - 1 - j) & 1) {
            total = (total - signed_term + MOD) % MOD;
        } else {
            total = (total + signed_term) % MOD;
        }
        
        comb = ((comb * ((alpha - j) % MOD)) % MOD) * inv[j + 1] % MOD;
    }
    
    free(inv);
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
    lib.solve_c.argtypes = [ctypes.c_int64, ctypes.c_int64]
    return lib


def solve(alpha: int = 10_000_000, n: int = 1_000_000_000_000) -> int:
    """Compute I(alpha, n) modulo 1000000007 using the inclusion-exclusion geometric series identity."""
    if alpha <= 10:
        total = 0
        comb = 1
        for j in range(alpha):
            if j == 0:
                term = 1
            elif j == 1:
                term = (n + 1) % _MOD
            else:
                term = (
                    (pow(j, n + 1, _MOD) - 1)
                    * pow(j - 1, _MOD - 2, _MOD)
                    % _MOD
                )
            signed_term = (comb * term) % _MOD
            if (alpha - 1 - j) % 2 == 1:
                total = (total - signed_term + _MOD) % _MOD
            else:
                total = (total + signed_term) % _MOD
            comb = (
                (comb * (alpha - j))
                % _MOD
                * pow(j + 1, _MOD - 2, _MOD)
                % _MOD
            )
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(alpha, n))
    return ans


if __name__ == "__main__":
    print(solve())
