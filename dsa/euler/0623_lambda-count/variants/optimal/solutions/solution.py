"""Project Euler Problem 623: Lambda Count.

Find Lambda(2000) mod 1000000007, where Lambda(n) is the number of distinct closed
lambda-terms that can be written using at most n symbols modulo alpha-equivalence.
"""

import ctypes
import os
import subprocess
from typing import List

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_lambda_core.dll")
    c_path = os.path.join(tmp_dir, "fast_lambda_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#define MOD 1000000007LL

void solve_dp_c(int64_t* result_pref, int max_n) {
    int max_k = max_n / 5 + 1;
    int64_t* dp = (int64_t*)calloc((max_n + 1) * (max_k + 1), sizeof(int64_t));
    
    #define DP(n, k) dp[(n) * (max_k + 1) + (k)]
    
    for (int k = 0; k <= max_k; ++k) {
        DP(1, k) = k;
    }
    
    for (int n = 2; n <= max_n; ++n) {
        if (n >= 6) {
            for (int k = 0; k < max_k; ++k) {
                DP(n, k) = (DP(n, k) + DP(n - 5, k + 1)) % MOD;
            }
        }
        if (n >= 4) {
            int rem = n - 2;
            for (int j = 1; j < rem; ++j) {
                int l1 = j;
                int l2 = rem - j;
                for (int k = 0; k <= max_k; ++k) {
                    DP(n, k) = (DP(n, k) + DP(l1, k) * DP(l2, k)) % MOD;
                }
            }
        }
    }
    
    int64_t s = 0;
    for (int n = 1; n <= max_n; ++n) {
        s = (s + DP(n, 0)) % MOD;
        result_pref[n] = s;
    }
    
    free(dp);
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            ["gcc", "-O3", "-shared", "-o", dll_path, c_path], check=True
        )

    return ctypes.CDLL(dll_path)


def solve(max_n: int = 2000) -> int:
    """Compute Lambda(max_n) modulo 1000000007 using 2D symbol DP over free variables in scope."""
    lib = _get_compiled_lib()
    int64_array = ctypes.c_int64 * (max_n + 1)
    pref_buf = int64_array()

    lib.solve_dp_c(pref_buf, max_n)

    # Accumulate results in Python
    ans = 0
    for i in range(max_n, max_n + 1):
        ans = (ans + pref_buf[i]) % _MOD

    return ans


if __name__ == "__main__":
    print(solve())
