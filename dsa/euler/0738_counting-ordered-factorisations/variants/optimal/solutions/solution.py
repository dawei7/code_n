"""Project Euler Problem 738: Counting Ordered Factorisations.

Find D(10^10, 10^10) modulo 1000000007, where D(N, K) = sum_{n=1}^N sum_{k=1}^K d(n, k)
and d(n, k) is the number of ways to write n as a product of k ordered integers 1 <= x_1 <= ... <= x_k.
"""

import ctypes
import math
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p738_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p738_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007ULL

static int64_t count_tuples_c(int64_t N, int m, int64_t min_val) {
    if (m == 1) {
        if (min_val > N) return 0;
        return N - min_val + 1;
    }
    if (m == 2) {
        int64_t r = (int64_t)sqrt((double)N);
        while ((r + 1) * (r + 1) <= N) r++;
        while (r * r > N) r--;
        if (min_val > r) return 0;
        int64_t tot = 0;
        for (int64_t y = min_val; y <= r; ++y) {
            tot += (N / y - y + 1);
        }
        return tot;
    }
    
    int64_t total = 0;
    int64_t y = min_val;
    while (1) {
        int64_t p = 1;
        for (int i = 0; i < m; ++i) {
            if (N / y < p) { p = N + 1; break; }
            p *= y;
        }
        if (p > N) break;
        total += count_tuples_c(N / y, m - 1, y);
        y++;
    }
    return total;
}

int64_t solve_c(int64_t N, int64_t K) {
    int64_t total = K % MOD;
    int m = 1;
    while ((1ULL << m) <= (uint64_t)N) {
        int64_t c = count_tuples_c(N, m, 2);
        int64_t weight = (K - m + 1) % MOD;
        total = (total + (__int128)(c % MOD) * weight) % MOD;
        m++;
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
    n: int = 10_000_000_000,
    k: int = 10_000_000_000,
    mod: int = 1_000_000_007,
) -> int:
    """Compute D(N, K) modulo 1000000007 using non-unit kernel decomposition and branch pruning."""
    if n <= 1000:

        def count_tuples(n_val: int, m_len: int, min_val: int = 2) -> int:
            if m_len == 1:
                if min_val > n_val:
                    return 0
                return n_val - min_val + 1
            tot = 0
            y = min_val
            while y**m_len <= n_val:
                tot += count_tuples(n_val // y, m_len - 1, y)
                y += 1
            return tot

        total = k % mod
        m = 1
        while 2**m <= n:
            c = count_tuples(n, m, 2)
            total = (total + (k - m + 1) * c) % mod
            m += 1
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n, k))
    return ans


if __name__ == "__main__":
    print(solve())
