"""Project Euler Problem 614: Special Partitions 2.

Find sum_{i=1}^{10^7} P(i) mod 1000000007, where P(n) is the number of partitions
of n into distinct parts where all even parts are divisible by 4.
"""

import ctypes
import os
import subprocess
from typing import List, Tuple

_MOD = 1_000_000_007


def _get_pentagonal_sparse(limit: int) -> List[Tuple[int, int]]:
    terms: List[Tuple[int, int]] = []
    k = 1
    while True:
        p1 = k * (3 * k - 1) // 2
        p2 = k * (3 * k + 1) // 2
        sign = -1 if (k & 1) else 1
        if p1 <= limit:
            terms.append((p1, sign))
        if p2 <= limit:
            terms.append((p2, sign))
        if p1 > limit and p2 > limit:
            break
        k += 1
    terms.sort()
    return terms


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_poly_core.dll")
    c_path = os.path.join(tmp_dir, "fast_poly_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#define MOD 1000000007LL

void poly_mul_sparse_c(int64_t* res, const int64_t* poly_dense, const int32_t* powers, const int32_t* signs, int num_terms, int limit) {
    for (int i = 0; i <= limit; ++i) res[i] = poly_dense[i];
    for (int t = 0; t < num_terms; ++t) {
        int p = powers[t];
        int s = signs[t];
        if (s == 1) {
            for (int i = p; i <= limit; ++i) {
                res[i] += poly_dense[i - p];
                if (res[i] >= MOD) res[i] -= MOD;
            }
        } else {
            for (int i = p; i <= limit; ++i) {
                res[i] -= poly_dense[i - p];
                if (res[i] < 0) res[i] += MOD;
            }
        }
    }
}

void poly_div_sparse_c(int64_t* F, const int64_t* num_dense, const int32_t* powers, const int32_t* signs, int num_terms, int limit) {
    for (int n = 0; n <= limit; ++n) {
        int64_t v = num_dense[n];
        for (int t = 0; t < num_terms; ++t) {
            int p = powers[t];
            if (p > n) break;
            int s = signs[t];
            if (s == 1) {
                v -= F[n - p];
            } else {
                v += F[n - p];
            }
        }
        v %= MOD;
        if (v < 0) v += MOD;
        F[n] = v;
    }
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            ["gcc", "-O3", "-shared", "-o", dll_path, c_path], check=True
        )

    return ctypes.CDLL(dll_path)


def solve(n: int = 10_000_000) -> int:
    """Compute sum_{i=1}^n P(i) mod 1000000007 using the generating function F(x) = phi(x^2)^2 phi(x^8) / (phi(x) phi(x^4)^2)."""
    p_x = _get_pentagonal_sparse(n)
    p_x2 = [(2 * p, s) for p, s in _get_pentagonal_sparse(n // 2)]
    p_x4 = [(4 * p, s) for p, s in _get_pentagonal_sparse(n // 4)]
    p_x8 = [(8 * p, s) for p, s in _get_pentagonal_sparse(n // 8)]

    lib = _get_compiled_lib()

    int64_array = ctypes.c_int64 * (n + 1)
    int32_array = ctypes.c_int32

    def make_sparse_c(terms: List[Tuple[int, int]]):
        num = len(terms)
        p_arr = (int32_array * num)(*[t[0] for t in terms])
        s_arr = (int32_array * num)(*[t[1] for t in terms])
        return p_arr, s_arr, num

    num_buf = int64_array()
    num_buf[0] = 1
    temp_buf = int64_array()

    for terms in [p_x2, p_x2, p_x8]:
        p_arr, s_arr, cnt = make_sparse_c(terms)
        lib.poly_mul_sparse_c(temp_buf, num_buf, p_arr, s_arr, cnt, n)
        for i in range(n + 1):
            num_buf[i] = temp_buf[i]

    f_buf = int64_array()
    p_arr, s_arr, cnt = make_sparse_c(p_x)
    lib.poly_div_sparse_c(f_buf, num_buf, p_arr, s_arr, cnt, n)

    for _ in range(2):
        p_arr, s_arr, cnt = make_sparse_c(p_x4)
        for i in range(n + 1):
            temp_buf[i] = f_buf[i]
        lib.poly_div_sparse_c(f_buf, temp_buf, p_arr, s_arr, cnt, n)

    total_sum = sum(f_buf[1 : n + 1]) % _MOD
    return total_sum


if __name__ == "__main__":
    print(solve())
