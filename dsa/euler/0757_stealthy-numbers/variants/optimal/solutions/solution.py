"""Project Euler Problem 757: Stealthy Numbers.

Find the number of stealthy numbers not exceeding 10^14. A number N is stealthy
if ab = cd = N and a + b = c + d + 1, which corresponds to N = x(x+1)y(y+1).
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p757_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p757_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

static uint64_t arr[120000000];
static uint64_t tmp_arr[120000000];

static void radix_sort_u64(uint64_t *a, uint64_t *tmp, size_t n) {
    size_t count[256];
    for (int shift = 0; shift < 64; shift += 8) {
        for (int i = 0; i < 256; ++i) count[i] = 0;
        for (size_t i = 0; i < n; ++i) count[(a[i] >> shift) & 0xFF]++;
        size_t total = 0;
        for (int i = 0; i < 256; ++i) {
            size_t old = count[i];
            count[i] = total;
            total += old;
        }
        for (size_t i = 0; i < n; ++i) {
            tmp[count[(a[i] >> shift) & 0xFF]++] = a[i];
        }
        uint64_t *swp = a; a = tmp; tmp = swp;
    }
}

int64_t solve_c(int64_t M) {
    size_t count = 0;
    
    for (int64_t x = 1; ; ++x) {
        int64_t xx = x * (x + 1);
        if ((__int128)xx * xx > M) break;
        
        for (int64_t y = x; ; ++y) {
            int64_t yy = y * (y + 1);
            if ((__int128)xx * yy > M) break;
            arr[count++] = (uint64_t)xx * yy;
        }
    }
    
    radix_sort_u64(arr, tmp_arr, count);
    
    if (count == 0) return 0;
    size_t unique = 1;
    for (size_t i = 1; i < count; ++i) {
        if (arr[i] != arr[i - 1]) unique++;
    }
    return (int64_t)unique;
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


def solve(limit: int = 100_000_000_000_000) -> int:
    """Compute number of stealthy numbers <= limit using x(x+1)y(y+1) parameterization."""
    if limit <= 1_000_000:
        stealthy = set()
        x = 1
        while x * (x + 1) * x * (x + 1) <= limit:
            xx = x * (x + 1)
            y = x
            while True:
                val = xx * y * (y + 1)
                if val > limit:
                    break
                stealthy.add(val)
                y += 1
            x += 1
        return len(stealthy)

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
