"""Project Euler Problem 713: Turan's Water Heating System.

Find L(10^7), where L(N) is the sum of T(N, m) for 2 <= m <= N, and T(N, m) is the minimum
number of pair tests required to guarantee at least one working pair among m working fuses.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p713_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p713_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

int64_t solve_c(int64_t N) {
    int64_t total = 0;
    for (int64_t k = 1; k < N; ++k) {
        int64_t q = N / k;
        int64_t r = N % k;
        int64_t intra = r * (q + 1) * q / 2 + (k - r) * q * (q - 1) / 2;
        total += intra;
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


def solve(n: int = 10_000_000) -> int:
    """Compute L(N) using Turan graph intra-component pair count formula."""
    if n <= 1000:
        total = 0
        for k in range(1, n):
            q = n // k
            r = n % k
            intra = r * (q + 1) * q // 2 + (k - r) * q * (q - 1) // 2
            total += intra
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
