"""Project Euler Problem 726: Falling Bottles.

Find S(10^4) mod 1000000033, where S(n) = sum_{k=1}^n f(k) and f(n) is the number of ways
to remove all bottles from an n-layer triangular stack under recursive collapsing rules.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_033


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p726_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p726_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000033ULL

static inline uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

static uint64_t inv_odd[20005];

int64_t solve_c(int n) {
    for (int k = 1; k <= n; ++k) {
        inv_odd[k] = pow_mod(2 * k - 1, MOD - 2, MOD);
    }
    
    uint64_t cur_f = 1;
    uint64_t total = 1;
    uint64_t curN = 1;
    uint64_t pow2 = 2;
    uint64_t mers_prefix = 1;
    uint64_t odd_inv_prefix = 1;
    
    for (int layer = 2; layer <= n; ++layer) {
        uint64_t start = curN + 1;
        uint64_t end = curN + layer;
        for (uint64_t x = start; x <= end; ++x) {
            cur_f = (uint64_t)((__int128)cur_f * (x % MOD) % MOD);
        }
        curN = end;
        
        pow2 = (pow2 * 2) % MOD;
        mers_prefix = (uint64_t)((__int128)mers_prefix * (pow2 + MOD - 1) % MOD);
        odd_inv_prefix = (uint64_t)((__int128)odd_inv_prefix * inv_odd[layer] % MOD);
        
        cur_f = (uint64_t)((__int128)cur_f * mers_prefix % MOD);
        cur_f = (uint64_t)((__int128)cur_f * odd_inv_prefix % MOD);
        
        total = (total + cur_f) % MOD;
    }
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


def solve(n: int = 10_000, mod: int = _MOD) -> int:
    """Compute S(n) modulo 1000000033 using closed product factorizations and prefix multipliers."""
    if n <= 3:
        inv_odd = [0] * (n + 1)
        for k in range(1, n + 1):
            inv_odd[k] = pow(2 * k - 1, mod - 2, mod)

        cur_f = 1
        total = 1
        cur_n = 1
        pow2 = 2
        mers_prefix = 1
        odd_inv_prefix = 1

        for layer in range(2, n + 1):
            start = cur_n + 1
            end = cur_n + layer
            for x in range(start, end + 1):
                cur_f = (cur_f * x) % mod
            cur_n = end

            pow2 = (pow2 * 2) % mod
            mers_prefix = (mers_prefix * (pow2 - 1)) % mod
            odd_inv_prefix = (odd_inv_prefix * inv_odd[layer]) % mod

            cur_f = (cur_f * mers_prefix) % mod
            cur_f = (cur_f * odd_inv_prefix) % mod

            total = (total + cur_f) % mod
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
