"""Project Euler Problem 700: Eulercoin.

Find the sum of all Eulercoins in the sequence 1504170715041707n mod 4503599627370517
(record minimal values strictly smaller than all previous values).
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p700_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p700_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

int64_t solve_c(int64_t a, int64_t m) {
    int64_t total = 0;
    int64_t cur_min = m;
    int64_t v = 0;
    int64_t threshold = 20000000;
    
    while (1) {
        v += a;
        if (v >= m) v -= m;
        if (v < cur_min) {
            cur_min = v;
            total += v;
            if (cur_min < threshold) break;
        }
    }
    
    int64_t last_forward = cur_min;
    
    int64_t t = 0, newt = 1;
    int64_t r = m, newr = a;
    while (newr != 0) {
        int64_t q = r / newr;
        int64_t tmp = t - q * newt; t = newt; newt = tmp;
        tmp = r - q * newr; r = newr; newr = tmp;
    }
    if (t < 0) t += m;
    int64_t inv_a = t;
    
    int64_t min_n = m;
    for (int64_t val = 1; val < last_forward; ++val) {
        int64_t n_v = (int64_t)(((unsigned __int128)val * inv_a) % m);
        if (n_v < min_n) {
            min_n = n_v;
            total += val;
        }
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
    lib.solve_c.argtypes = [ctypes.c_int64, ctypes.c_int64]
    return lib


def solve(
    a: int = 1504170715041707, m: int = 4503599627370517, num_coins: int = -1
) -> int:
    """Find the sum of all Eulercoins using bidirectional modular stepping."""
    if num_coins > 0:
        total = 0
        cur_min = m
        v = 0
        count = 0
        while count < num_coins:
            v = (v + a) % m
            if v < cur_min:
                cur_min = v
                total += v
                count += 1
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(a, m))
    return ans


if __name__ == "__main__":
    print(solve())
