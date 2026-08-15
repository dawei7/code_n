"""Project Euler Problem 719: Number Splitting.

Find T(10^12), the sum of all S-numbers n <= 10^12, where an S-number is a perfect square n
whose decimal representation can be split into 2 or more numbers adding up to sqrt(n).
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p719_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p719_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdbool.h>

static bool check_split(int64_t num, int64_t target, int parts_count) {
    if (num == target && parts_count > 0) return true;
    if (num < target) return false;
    
    int64_t mod = 10;
    while (mod < num) {
        int64_t head = num / mod;
        int64_t tail = num % mod;
        if (tail <= target) {
            if (check_split(head, target - tail, parts_count + 1)) return true;
        }
        mod *= 10;
    }
    return false;
}

int64_t solve_c(int64_t limit) {
    int64_t total = 0;
    for (int64_t k = 2; k <= limit; ++k) {
        int r = k % 9;
        if (r == 0 || r == 1) {
            int64_t n = k * k;
            if (check_split(n, k, 0)) {
                total += n;
            }
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
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 1_000_000_000_000) -> int:
    """Compute T(N) using digital root modulo 9 filtering and recursive suffix partition matching."""
    limit = int(n**0.5)
    if limit <= 100:

        def check_split_py(num: int, target: int, parts: int) -> bool:
            if num == target and parts > 0:
                return True
            if num < target:
                return False
            m = 10
            while m < num:
                head = num // m
                tail = num % m
                if tail <= target:
                    if check_split_py(head, target - tail, parts + 1):
                        return True
                m *= 10
            return False

        total = 0
        for k in range(2, limit + 1):
            if k % 9 in (0, 1):
                sq = k * k
                if check_split_py(sq, k, 0):
                    total += sq
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
