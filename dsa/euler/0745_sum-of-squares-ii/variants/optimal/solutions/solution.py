"""Project Euler Problem 745: Sum of Squares II.

Find S(10^14) modulo 1000000007, where S(N) = sum_{n=1}^N g(n) and g(n) is the maximum
perfect square that divides n.
"""

import ctypes
import math
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p745_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p745_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL
#define MAX_K 10000005

static uint32_t J2[MAX_K];
static int primes[700000];
static uint8_t is_comp[MAX_K];

int64_t solve_c(int64_t N) {
    int64_t limit = 1;
    while ((limit + 1) * (limit + 1) <= N) limit++;
    
    for (int i = 0; i <= limit; ++i) {
        J2[i] = 0;
        is_comp[i] = 0;
    }
    
    J2[1] = 1;
    int P = 0;
    
    for (int i = 2; i <= limit; ++i) {
        if (!is_comp[i]) {
            primes[P++] = i;
            uint64_t p2 = (uint64_t)i * i % MOD;
            J2[i] = (uint32_t)((p2 + MOD - 1) % MOD);
        }
        for (int j = 0; j < P; ++j) {
            int p = primes[j];
            int64_t ip = (int64_t)i * p;
            if (ip > limit) break;
            is_comp[ip] = 1;
            uint64_t p2 = (uint64_t)p * p % MOD;
            if (i % p == 0) {
                J2[ip] = (uint32_t)((uint64_t)J2[i] * p2 % MOD);
                break;
            } else {
                J2[ip] = (uint32_t)((uint64_t)J2[i] * J2[p] % MOD);
            }
        }
    }
    
    uint64_t total = 0;
    for (int64_t k = 1; k <= limit; ++k) {
        uint64_t cnt = (N / (k * k)) % MOD;
        total = (total + (uint64_t)J2[k] * cnt) % MOD;
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
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 100_000_000_000_000) -> int:
    """Compute S(N) modulo 1000000007 using Jordan's Totient function J_2(k) linear sieve."""
    if n <= 1000:
        total = 0
        for i in range(1, n + 1):
            d = math.isqrt(i)
            while d >= 1:
                if i % (d * d) == 0:
                    total = (total + d * d) % _MOD
                    break
                d -= 1
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
