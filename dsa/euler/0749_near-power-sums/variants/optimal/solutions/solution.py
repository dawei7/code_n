"""Project Euler Problem 749: Near Power Sums.

Find S(16), the sum of all near power sum numbers of 16 digits or less.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p749_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p749_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SOLS 100000

static uint64_t pows[10][80];
static int counts[10];
static uint64_t pow10[20];
static uint64_t found_sols[MAX_SOLS];
static int found_count = 0;

static inline void check_candidate(uint64_t n, int L) {
    if (n < pow10[L - 1] || n >= pow10[L]) return;
    
    int temp_counts[10] = {0};
    uint64_t temp = n;
    int len = 0;
    while (temp > 0) {
        temp_counts[temp % 10]++;
        temp /= 10;
        len++;
    }
    while (len < L) {
        temp_counts[0]++;
        len++;
    }
    
    for (int i = 0; i < 10; ++i) {
        if (temp_counts[i] != counts[i]) return;
    }
    
    for (int i = 0; i < found_count; ++i) {
        if (found_sols[i] == n) return;
    }
    found_sols[found_count++] = n;
}

static void check_counts(int L) {
    int max_d = 0;
    for (int i = 9; i >= 1; --i) {
        if (counts[i] > 0) {
            max_d = i;
            break;
        }
    }
    if (max_d == 0) return;
    
    uint64_t low_bound = (L > 1) ? pow10[L - 1] : 0;
    uint64_t high_bound = pow10[L] - 1;
    
    for (int k = 1; k < 70; ++k) {
        uint64_t p_sum = 0;
        bool overflow = false;
        for (int i = 1; i <= 9; ++i) {
            if (counts[i] > 0) {
                uint64_t term = pows[i][k];
                if (UINT64_MAX / counts[i] < term) {
                    overflow = true;
                    break;
                }
                uint64_t prod = counts[i] * term;
                if (UINT64_MAX - p_sum < prod) {
                    overflow = true;
                    break;
                }
                p_sum += prod;
            }
        }
        if (overflow || p_sum > high_bound + 1) break;
        
        if (p_sum >= low_bound + 1) {
            check_candidate(p_sum - 1, L);
        }
        if (p_sum + 1 <= high_bound) {
            check_candidate(p_sum + 1, L);
        }
    }
}

static void search_multiset(int d, int remaining, int L) {
    if (d == 9) {
        counts[9] = remaining;
        check_counts(L);
        return;
    }
    for (int c = 0; c <= remaining; ++c) {
        counts[d] = c;
        search_multiset(d + 1, remaining - c, L);
    }
}

uint64_t solve_c(int D_max) {
    pow10[0] = 1;
    for (int i = 1; i <= 18; ++i) pow10[i] = pow10[i - 1] * 10;
    
    for (int i = 0; i <= 9; ++i) {
        pows[i][0] = 1;
        for (int k = 1; k < 70; ++k) {
            pows[i][k] = pows[i][k - 1] * i;
        }
    }
    
    found_count = 0;
    for (int L = 1; L <= D_max; ++L) {
        search_multiset(0, L, L);
    }
    
    uint64_t total = 0;
    for (int i = 0; i < found_count; ++i) {
        total += found_sols[i];
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
    lib.solve_c.restype = ctypes.c_uint64
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(d_max: int = 16) -> int:
    """Compute S(d_max) using multiset digit power sum search."""
    if d_max <= 2:
        found = set()
        for n in range(1, 100):
            digits = [int(ch) for ch in str(n)]
            for k in range(1, 10):
                p_sum = sum(d**k for d in digits)
                if p_sum == n - 1 or p_sum == n + 1:
                    found.add(n)
        return sum(found)

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(d_max))
    return ans


if __name__ == "__main__":
    print(solve())
