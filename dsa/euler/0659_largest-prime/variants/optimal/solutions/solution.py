"""Project Euler Problem 659: Largest Prime.

Find the last 18 digits of sum_{k=1}^10000000 P(k), where P(k) is the largest prime
that divides any two successive terms of the sequence n^2 + k^2.
"""

import ctypes
import os
import subprocess

_MOD = 10**18


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_lpf_core.dll")
    c_path = os.path.join(tmp_dir, "fast_lpf_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000000000000000ULL

uint64_t solve_c(int64_t limit) {
    int64_t* f = (int64_t*)malloc((limit + 1) * sizeof(int64_t));
    int64_t* maxelem = (int64_t*)calloc(limit + 1, sizeof(int64_t));
    
    for (int64_t x = 0; x <= limit; ++x) {
        f[x] = 4 * x * x + 1;
    }
    
    for (int64_t x = 1; x <= limit; ++x) {
        int64_t div = f[x];
        if (div > 1) {
            int64_t curr1 = x % div;
            while (curr1 <= limit) {
                if (f[curr1] % div == 0) {
                    if (div > maxelem[curr1]) maxelem[curr1] = div;
                    while (f[curr1] % div == 0) {
                        f[curr1] /= div;
                    }
                }
                curr1 += div;
            }
            
            int64_t curr2 = (div - (x % div)) % div;
            while (curr2 <= limit) {
                if (f[curr2] % div == 0) {
                    if (div > maxelem[curr2]) maxelem[curr2] = div;
                    while (f[curr2] % div == 0) {
                        f[curr2] /= div;
                    }
                }
                curr2 += div;
            }
        }
    }
    
    uint64_t total = 0;
    for (int64_t x = 1; x <= limit; ++x) {
        total = (total + (uint64_t)maxelem[x]) % MOD;
    }
    
    free(f);
    free(maxelem);
    return total;
}
"""
        with open(c_path, "w", encoding="utf-8") as fp:
            fp.write(c_code)

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
    lib.solve_c.restype = ctypes.c_uint64
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(limit: int = 10_000_000) -> str:
    """Compute the sum of P(k) mod 10^18 for k <= limit using the quadratic polynomial sieve on 4k^2 + 1."""
    if limit <= 100:
        f = [4 * x * x + 1 for x in range(limit + 1)]
        maxelem = [0] * (limit + 1)
        for x in range(1, len(f)):
            div = f[x]
            if div > 1:
                curr1 = x % div
                while curr1 <= limit:
                    if f[curr1] % div == 0:
                        maxelem[curr1] = max(maxelem[curr1], div)
                        while f[curr1] % div == 0:
                            f[curr1] //= div
                    curr1 += div

                curr2 = (-x) % div
                while curr2 <= limit:
                    if f[curr2] % div == 0:
                        maxelem[curr2] = max(maxelem[curr2], div)
                        while f[curr2] % div == 0:
                            f[curr2] //= div
                    curr2 += div
        total = sum(maxelem) % _MOD
        return f"{total:018d}"

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return f"{ans:018d}"


if __name__ == "__main__":
    print(solve())
