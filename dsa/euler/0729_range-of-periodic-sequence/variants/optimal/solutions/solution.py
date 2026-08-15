"""Project Euler Problem 729: Range of Periodic Sequence.

Find S(25) rounded to 4 decimal places, where S(P) is the sum of the ranges (max - min)
of all real periodic sequences satisfying a_{n+1} = a_n - 1/a_n with period <= P.
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p729_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p729_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

static int a[30];
static double total_sum;
static int cur_n;

static inline void handle_one_necklace() {
    double x = 0.0;
    for (int iter = 0; iter < 4; ++iter) {
        double y = x;
        double dy = 1.0;
        for (int i = 1; i <= cur_n; ++i) {
            double s = sqrt(y * y + 4.0);
            if (a[i] == 0) {
                dy *= 0.5 * (1.0 + y / s);
                y = 0.5 * (y + s);
            } else {
                dy *= 0.5 * (1.0 - y / s);
                y = 0.5 * (y - s);
            }
        }
        double next_x = x - (y - x) / (dy - 1.0);
        if (fabs(next_x - x) <= 1e-15 * (1.0 + fabs(next_x))) {
            x = next_x;
            break;
        }
        x = next_x;
    }
    
    double y = x;
    double mn = y;
    double mx = y;
    for (int i = 1; i < cur_n; ++i) {
        double s = sqrt(y * y + 4.0);
        if (a[i] == 0) {
            y = 0.5 * (y + s);
        } else {
            y = 0.5 * (y - s);
        }
        if (y < mn) mn = y;
        if (y > mx) mx = y;
    }
    total_sum += cur_n * (mx - mn);
}

static void rec(int t, int p) {
    if (t > cur_n) {
        if (p == cur_n) {
            handle_one_necklace();
        }
        return;
    }
    a[t] = a[t - p];
    rec(t + 1, p);
    if (a[t - p] == 0) {
        a[t] = 1;
        rec(t + 1, t);
    }
}

double solve_c(int P) {
    total_sum = 0.0;
    for (int n = 2; n <= P; ++n) {
        cur_n = n;
        rec(1, 1);
    }
    return total_sum;
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
    lib.solve_c.restype = ctypes.c_double
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(p: int = 25) -> str:
    """Compute S(P) rounded to 4 decimal places using binary Lyndon word generation and Newton-Raphson inverse cycle fixed point evaluation."""
    if p <= 3:
        total = 0.0
        for n in range(2, p + 1):
            a = [0] * (n + 1)

            def handle(cur_n: int) -> float:
                x = 0.0
                for _ in range(4):
                    y = x
                    dy = 1.0
                    for i in range(1, cur_n + 1):
                        s = math.sqrt(y * y + 4.0)
                        if a[i] == 0:
                            dy *= 0.5 * (1.0 + y / s)
                            y = 0.5 * (y + s)
                        else:
                            dy *= 0.5 * (1.0 - y / s)
                            y = 0.5 * (y - s)
                    next_x = x - (y - x) / (dy - 1.0)
                    x = next_x
                y = x
                mn = y
                mx = y
                for i in range(1, cur_n):
                    s = math.sqrt(y * y + 4.0)
                    if a[i] == 0:
                        y = 0.5 * (y + s)
                    else:
                        y = 0.5 * (y - s)
                    if y < mn:
                        mn = y
                    if y > mx:
                        mx = y
                return cur_n * (mx - mn)

            def rec_py(t: int, p_len: int, cur_n: int) -> None:
                nonlocal total
                if t > cur_n:
                    if p_len == cur_n:
                        total += handle(cur_n)
                    return
                a[t] = a[t - p_len]
                rec_py(t + 1, p_len, cur_n)
                if a[t - p_len] == 0:
                    a[t] = 1
                    rec_py(t + 1, t, cur_n)

            rec_py(1, 1, n)
        return f"{total:.4f}"

    lib = _get_compiled_lib()
    ans = float(lib.solve_c(p))
    return f"{ans:.4f}"


if __name__ == "__main__":
    print(solve())
