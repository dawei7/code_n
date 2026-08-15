"""Project Euler Problem 628: Open Chess Positions.

Find f(10^8) mod 1008691207, where f(n) is the number of open chess positions
on an n x n board with n non-attacking pawns.
"""

import ctypes
import os
import subprocess

_MOD = 1_008_691_207


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_chess_core.dll")
    c_path = os.path.join(tmp_dir, "fast_chess_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#define MOD 1008691207LL

int64_t solve_c(int64_t n) {
    int64_t fact = 1;
    int64_t sum_fact = 1;
    for (int64_t k = 1; k < n; ++k) {
        fact = (fact * k) % MOD;
        sum_fact += fact;
        if (sum_fact >= MOD) sum_fact -= MOD;
    }
    int64_t ans = ((n - 3) % MOD * sum_fact + 2) % MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            ["gcc", "-O3", "-shared", "-o", dll_path, c_path], check=True
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 100_000_000) -> int:
    """Compute f(n) modulo 1008691207 using the left-factorial closed formula f(n) = (n - 3) * !n + 2."""
    if n <= 1000:
        fact = 1
        sum_fact = 1
        for k in range(1, n):
            fact = (fact * k) % _MOD
            sum_fact = (sum_fact + fact) % _MOD
        return (((n - 3) % _MOD) * sum_fact + 2) % _MOD

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
