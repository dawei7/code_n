"""Project Euler Problem 705: Total Inversion Count of Divided Sequences.

Find F(10^8) mod 1000000007, the total inversion count across all divided sequences
generated from the prime digit stream G(10^8).
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p705_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p705_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

static const int I_mat[10][10] = {
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,1,1,1,1,1,1,1,1,1},
    {0,1,2,1,2,1,2,1,2,1},
    {0,2,3,3,3,2,4,2,3,3},
    {0,1,2,2,3,1,3,1,3,2},
    {0,3,5,4,6,4,6,3,6,4},
    {0,1,2,2,3,2,4,1,3,2},
    {0,3,5,5,6,4,8,4,6,5},
    {0,2,4,3,5,3,6,3,6,3}
};

static const uint64_t k_arr[10] = {0, 1, 2, 2, 3, 2, 4, 2, 4, 3};
static const uint64_t w_arr[10] = {0, 1, 500000004, 500000004, 333333336, 500000004, 250000002, 500000004, 250000002, 333333336};

static uint8_t is_comp[100000005 / 8 + 1];

static inline int get_comp(int i) {
    return (is_comp[i >> 3] >> (i & 7)) & 1;
}

static inline void set_comp(int i) {
    is_comp[i >> 3] |= (1 << (i & 7));
}

int64_t solve_c(int limit) {
    for (int i = 0; i <= limit / 8 + 1; ++i) is_comp[i] = 0;
    set_comp(0);
    set_comp(1);
    for (int p = 2; p * p < limit; ++p) {
        if (!get_comp(p)) {
            for (int j = p * p; j < limit; j += p) {
                set_comp(j);
            }
        }
    }
    
    uint64_t W[10] = {0};
    uint64_t K_prod = 1;
    uint64_t S_sum = 0;
    
    char buf[16];
    
    for (int p = 2; p < limit; ++p) {
        if (!get_comp(p)) {
            int len = 0;
            int tmp = p;
            while (tmp > 0) {
                int d = tmp % 10;
                tmp /= 10;
                if (d > 0) {
                    buf[len++] = d;
                }
            }
            for (int idx = len - 1; idx >= 0; --idx) {
                int v = buf[idx];
                uint64_t wv = w_arr[v];
                
                uint64_t sum_u = 0;
                for (int u = 1; u <= 9; ++u) {
                    sum_u = (sum_u + (uint64_t)I_mat[u][v] * W[u]) % MOD;
                }
                
                S_sum = (S_sum + wv * sum_u) % MOD;
                W[v] = (W[v] + wv) % MOD;
                K_prod = (K_prod * k_arr[v]) % MOD;
            }
        }
    }
    
    uint64_t ans = (S_sum * K_prod) % MOD;
    return (int64_t)ans;
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
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(limit: int = 100_000_000) -> int:
    """Find F(limit) mod 1000000007 using linearity of expectation on prime digit streams."""
    if limit <= 100:
        divs = {
            1: [1],
            2: [1, 2],
            3: [1, 3],
            4: [1, 2, 4],
            5: [1, 5],
            6: [1, 2, 3, 6],
            7: [1, 7],
            8: [1, 2, 4, 8],
            9: [1, 3, 9],
        }
        mod = 1_000_000_007
        i_mat = [[0] * 10 for _ in range(10)]
        for u in range(1, 10):
            for v in range(1, 10):
                cnt = 0
                for x in divs[u]:
                    for y in divs[v]:
                        if x > y:
                            cnt += 1
                i_mat[u][v] = cnt
        k_arr = [0] + [len(divs[i]) for i in range(1, 10)]
        w_arr = [0] + [pow(k_arr[i], mod - 2, mod) for i in range(1, 10)]

        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(limit**0.5) + 1):
            if is_prime[p]:
                for j in range(p * p, limit, p):
                    is_prime[j] = False

        w_acc = [0] * 10
        k_prod = 1
        s_sum = 0

        for p in range(2, limit):
            if is_prime[p]:
                digits = [int(ch) for ch in str(p) if ch != "0"]
                for v in digits:
                    wv = w_arr[v]
                    sum_u = sum(i_mat[u][v] * w_acc[u] for u in range(1, 10)) % mod
                    s_sum = (s_sum + wv * sum_u) % mod
                    w_acc[v] = (w_acc[v] + wv) % mod
                    k_prod = (k_prod * k_arr[v]) % mod

        return (s_sum * k_prod) % mod

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
