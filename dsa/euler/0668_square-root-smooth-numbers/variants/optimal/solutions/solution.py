"""Project Euler Problem 668: Square Root Smooth Numbers.

Find the number of square root smooth numbers not exceeding 10^10, where a positive integer
is square root smooth if all its prime factors are strictly less than its square root.
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_smooth_core.dll")
    c_path = os.path.join(tmp_dir, "fast_smooth_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

int64_t solve_c(int64_t N) {
    int64_t sqrtN = (int64_t)sqrt(N);
    int64_t num_vals = 2 * sqrtN;
    
    int64_t* V = (int64_t*)malloc(num_vals * sizeof(int64_t));
    int64_t* S = (int64_t*)malloc(num_vals * sizeof(int64_t));
    
    for (int64_t i = 1; i <= sqrtN; ++i) {
        V[i - 1] = N / i;
        S[i - 1] = V[i - 1] - 1;
    }
    for (int64_t i = sqrtN + 1; i <= 2 * sqrtN; ++i) {
        V[i - 1] = 2 * sqrtN - i + 1;
        S[i - 1] = V[i - 1] - 1;
    }
    
    for (int64_t p = 2; p <= sqrtN; ++p) {
        if (S[2 * sqrtN - p] > S[2 * sqrtN - (p - 1)]) {
            int64_t sp = S[2 * sqrtN - (p - 1)];
            int64_t p2 = p * p;
            
            for (int64_t i = 0; i < num_vals; ++i) {
                int64_t v = V[i];
                if (v < p2) break;
                
                int64_t div = v / p;
                int64_t idx = (div <= sqrtN) ? (2 * sqrtN - div) : (N / div - 1);
                S[i] -= (S[idx] - sp);
            }
        }
    }
    
    int64_t non_smooth = 0;
    for (int64_t k = 1; k <= sqrtN; ++k) {
        int64_t pi_Nk = S[k - 1];
        int64_t pi_k_minus_1 = (k == 1) ? 0 : S[2 * sqrtN - (k - 1)];
        non_smooth += (pi_Nk - pi_k_minus_1);
    }
    
    int64_t ans = N - non_smooth;
    free(V);
    free(S);
    return ans;
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


def solve(limit: int = 10_000_000_000) -> int:
    """Compute the number of square root smooth numbers <= limit using the sublinear Lucy_Hedgehog prime counting sieve."""
    if limit <= 1000:
        sqrt_n = math.isqrt(limit)
        v_list = [limit // i for i in range(1, sqrt_n + 1)] + list(
            range(sqrt_n, 0, -1)
        )
        s_map = {v: v - 1 for v in v_list}
        s_map[0] = 0

        for p in range(2, sqrt_n + 1):
            if s_map[p] > s_map[p - 1]:
                sp = s_map[p - 1]
                p2 = p * p
                for v in v_list:
                    if v < p2:
                        break
                    s_map[v] -= s_map[v // p] - sp

        non_smooth = 0
        for k in range(1, sqrt_n + 1):
            non_smooth += s_map[limit // k] - s_map[k - 1]
        return limit - non_smooth

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
