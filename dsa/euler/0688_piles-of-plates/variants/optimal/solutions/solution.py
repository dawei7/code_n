"""Project Euler Problem 688: Piles of Plates.

Find S(10^16) mod 1000000007, where f(n, k) is the maximum number of plates in the smallest pile
when stacking n plates into k distinct-sized piles, F(n) = sum_{k>=1} f(n, k), and S(N) = sum_{n=1}^N F(n).
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p688_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p688_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <math.h>

#define MOD 1000000007LL

int64_t solve_c(int64_t N) {
    int64_t max_k = (int64_t)((sqrt(8.0 * (double)N + 1.0) - 1.0) / 2.0);
    int64_t total = 0;
    
    for (int64_t k = 1; k <= max_k; ++k) {
        int64_t Tk = k * (k + 1) / 2;
        int64_t L = N - Tk;
        if (L < 0) break;
        
        int64_t q = L / k;
        int64_t r = L % k;
        
        int64_t q_mod = q % MOD;
        int64_t k_mod = k % MOD;
        int64_t r_mod = r % MOD;
        
        int64_t term1;
        if (q % 2 == 0) {
            term1 = (k_mod * ((q / 2) % MOD)) % MOD * ((q + 1) % MOD) % MOD;
        } else {
            term1 = (k_mod * q_mod) % MOD * (((q + 1) / 2) % MOD) % MOD;
        }
        
        int64_t term2 = (r_mod + 1) % MOD * ((q_mod + 1) % MOD) % MOD;
        
        total = (total + term1 + term2) % MOD;
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
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 10_000_000_000_000_000) -> int:
    """Compute S(N) modulo 1000000007."""
    if n <= 1000:
        total = 0
        max_k = int(((8 * n + 1) ** 0.5 - 1) / 2)
        for k in range(1, max_k + 1):
            tk = k * (k + 1) // 2
            l_val = n - tk
            if l_val < 0:
                break
            q = l_val // k
            r = l_val % k
            term1 = (k * q * (q + 1) // 2) % _MOD
            term2 = ((r + 1) * (q + 1)) % _MOD
            total = (total + term1 + term2) % _MOD
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
