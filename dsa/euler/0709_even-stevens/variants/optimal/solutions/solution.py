"""Project Euler Problem 709: Even Stevens.

Find f(24680) mod 1020202009, the number of valid plastic bag packings with even capacities
(the 24680-th Euler zig-zag number A_n).
"""

import ctypes
import os
import subprocess

_MOD = 1_020_202_009


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p709_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p709_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MAX_N 25000

static uint32_t row[MAX_N + 1];
static uint32_t new_row[MAX_N + 1];

uint32_t solve_c(int n, uint32_t mod) {
    row[0] = 1;
    for (int i = 1; i <= n; ++i) {
        if (i & 1) {
            new_row[0] = 0;
            for (int j = 1; j <= i; ++j) {
                uint32_t v = new_row[j - 1] + row[j - 1];
                if (v >= mod) v -= mod;
                new_row[j] = v;
            }
        } else {
            new_row[i] = 0;
            for (int j = i - 1; j >= 0; --j) {
                uint32_t v = new_row[j + 1] + row[j];
                if (v >= mod) v -= mod;
                new_row[j] = v;
            }
        }
        for (int j = 0; j <= i; ++j) {
            row[j] = new_row[j];
        }
    }
    return (n & 1) ? row[n] : row[0];
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
    lib.solve_c.restype = ctypes.c_uint32
    lib.solve_c.argtypes = [ctypes.c_int, ctypes.c_uint32]
    return lib


def solve(n: int = 24_680, mod: int = _MOD) -> int:
    """Compute f(n) mod mod using the Seidel-Entringer boustrophedon triangle."""
    if n <= 100:
        row = [1]
        for i in range(1, n + 1):
            new_row = [0] * (i + 1)
            if i % 2 == 1:
                new_row[0] = 0
                for j in range(1, i + 1):
                    new_row[j] = (new_row[j - 1] + row[j - 1]) % mod
            else:
                new_row[i] = 0
                for j in range(i - 1, -1, -1):
                    new_row[j] = (new_row[j + 1] + row[j]) % mod
            row = new_row
        return row[-1] if n % 2 == 1 else row[0]

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n, mod))
    return ans


if __name__ == "__main__":
    print(solve())
