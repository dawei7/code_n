"""Project Euler Problem 683: The Chase II.

Find G(500), the expected amount that the winner will receive in The Chase II game,
giving the answer in scientific notation rounded to 9 significant digits.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p683_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p683_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static double A[505][505];
static double aug1[505][506];
static double aug2[505][506];
static double e1[505];

static const double p_d[5] = {1.0/9.0, 2.0/9.0, 3.0/9.0, 2.0/9.0, 1.0/9.0};
static const int deltas[5] = {-2, -1, 0, 1, 2};

double solve_round_c(int m) {
    int dim = m - 1;
    for (int i = 0; i < dim; ++i) {
        for (int j = 0; j < dim; ++j) {
            A[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
    
    for (int i = 0; i < dim; ++i) {
        int d = i + 1;
        for (int k = 0; k < 5; ++k) {
            int nxt = (d + deltas[k]) % m;
            if (nxt < 0) nxt += m;
            if (nxt != 0) {
                A[i][nxt - 1] -= p_d[k];
            }
        }
    }
    
    for (int i = 0; i < dim; ++i) {
        for (int j = 0; j < dim; ++j) {
            aug1[i][j] = A[i][j];
        }
        aug1[i][dim] = 1.0;
    }
    
    for (int i = 0; i < dim; ++i) {
        int max_r = i;
        for (int r = i + 1; r < dim; ++r) {
            if (fabs(aug1[r][i]) > fabs(aug1[max_r][i])) max_r = r;
        }
        for (int c = i; c <= dim; ++c) {
            double tmp = aug1[i][c];
            aug1[i][c] = aug1[max_r][c];
            aug1[max_r][c] = tmp;
        }
        double pivot = aug1[i][i];
        for (int c = i; c <= dim; ++c) aug1[i][c] /= pivot;
        for (int r = 0; r < dim; ++r) {
            if (r != i) {
                double factor = aug1[r][i];
                for (int c = i; c <= dim; ++c) {
                    aug1[r][c] -= factor * aug1[i][c];
                }
            }
        }
    }
    for (int i = 0; i < dim; ++i) e1[i] = aug1[i][dim];
    
    for (int i = 0; i < dim; ++i) {
        for (int j = 0; j < dim; ++j) {
            aug2[i][j] = A[i][j];
        }
        aug2[i][dim] = 2.0 * e1[i] - 1.0;
    }
    
    for (int i = 0; i < dim; ++i) {
        int max_r = i;
        for (int r = i + 1; r < dim; ++r) {
            if (fabs(aug2[r][i]) > fabs(aug2[max_r][i])) max_r = r;
        }
        for (int c = i; c <= dim; ++c) {
            double tmp = aug2[i][c];
            aug2[i][c] = aug2[max_r][c];
            aug2[max_r][c] = tmp;
        }
        double pivot = aug2[i][i];
        for (int c = i; c <= dim; ++c) aug2[i][c] /= pivot;
        for (int r = 0; r < dim; ++r) {
            if (r != i) {
                double factor = aug2[r][i];
                for (int c = i; c <= dim; ++c) {
                    aug2[r][c] -= factor * aug2[i][c];
                }
            }
        }
    }
    
    double sum = 0.0;
    for (int i = 0; i < dim; ++i) sum += aug2[i][dim];
    return sum / m;
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
    lib.solve_round_c.restype = ctypes.c_double
    lib.solve_round_c.argtypes = [ctypes.c_int]
    return lib


def solve(n: int = 500) -> str:
    """Compute G(n) in scientific notation rounded to 9 significant digits."""
    lib = _get_compiled_lib()
    total = 0.0
    for m in range(2, n + 1):
        total += float(lib.solve_round_c(m))

    formatted = f"{total:.8e}".replace("+0", "").replace("+", "")
    return formatted


if __name__ == "__main__":
    print(solve())
