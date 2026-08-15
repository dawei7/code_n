"""Project Euler Problem 686: Powers of Two.

Find p(123, 678910), the 678910-th smallest value of j such that the base 10 representation
of 2^j begins with the digits 123.
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p686_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p686_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdio.h>
#include <math.h>
#include <stdint.h>

int64_t solve_c(int64_t L, int64_t n) {
    double alpha = log10(2.0);
    double scale = pow(10.0, floor(log10((double)L)));
    double low = log10((double)L / scale);
    double high = log10(((double)L + 1.0) / scale);
    
    int64_t count = 0;
    int64_t j = 0;
    double frac = 0.0;
    
    while (count < n) {
        j++;
        frac += alpha;
        if (frac >= 1.0) frac -= 1.0;
        
        if (frac >= low && frac < high) {
            count++;
            if (count == n) return j;
        }
    }
    return j;
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


def solve(l_prefix: int = 123, n: int = 678_910) -> int:
    """Find the n-th smallest j such that 2^j begins with the digits of l_prefix."""
    if n <= 100:
        alpha = math.log10(2.0)
        scale = 10 ** int(math.log10(l_prefix))
        low = math.log10(l_prefix / scale)
        high = math.log10((l_prefix + 1) / scale)
        count = 0
        j = 0
        frac = 0.0
        while count < n:
            j += 1
            frac += alpha
            if frac >= 1.0:
                frac -= 1.0
            if low <= frac < high:
                count += 1
                if count == n:
                    return j

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(l_prefix, n))
    return ans


if __name__ == "__main__":
    print(solve())
