"""Project Euler Problem 720: Unpredictable Permutations.

Find S(2^25) mod 1000000007, where S(N) is the 1-based lexicographical rank of the first
unpredictable (3-AP-free) permutation of {1, 2, ..., N}.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p720_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p720_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

static uint32_t *vals_arr;
static uint32_t *codes_arr;
static uint32_t *new_vals_arr;
static uint32_t *new_codes_arr;

int64_t solve_c(int k) {
    if (k == 0 || k == 1) return 1;
    if (k == 2) return 3;
    
    int target_size = 1 << (k - 1);
    
    vals_arr = (uint32_t *)malloc(target_size * sizeof(uint32_t));
    codes_arr = (uint32_t *)malloc(target_size * sizeof(uint32_t));
    new_vals_arr = (uint32_t *)malloc(target_size * sizeof(uint32_t));
    new_codes_arr = (uint32_t *)malloc(target_size * sizeof(uint32_t));
    
    vals_arr[0] = 1; vals_arr[1] = 3; vals_arr[2] = 2; vals_arr[3] = 4;
    codes_arr[0] = 0; codes_arr[1] = 1; codes_arr[2] = 0; codes_arr[3] = 0;
    
    int size = 4;
    while (size < target_size) {
        int m = size;
        int n = m << 1;
        
        for (int i = 0; i < m - 1; ++i) {
            uint32_t v = vals_arr[i];
            new_vals_arr[i] = (v << 1) - 1;
            new_codes_arr[i] = (v - 1) + codes_arr[i];
        }
        new_vals_arr[m - 1] = 2;
        new_codes_arr[m - 1] = 0;
        
        uint32_t v_last = vals_arr[m - 1];
        new_vals_arr[m] = (v_last << 1) - 1;
        new_codes_arr[m] = m - 2;
        
        for (int j = 1; j < m; ++j) {
            uint32_t v = vals_arr[j];
            new_vals_arr[m + j] = v << 1;
            new_codes_arr[m + j] = codes_arr[j];
        }
        
        uint32_t *tmp_v = vals_arr; vals_arr = new_vals_arr; new_vals_arr = tmp_v;
        uint32_t *tmp_c = codes_arr; codes_arr = new_codes_arr; new_codes_arr = tmp_c;
        size = n;
    }
    
    int m = target_size;
    uint64_t rank = 0;
    uint64_t fact = 1;
    uint64_t step = 1;
    
    for (int j = m - 1; j >= 1; --j) {
        uint64_t l = codes_arr[j];
        rank = (rank + l * fact) % MOD;
        fact = (fact * step) % MOD;
        step++;
    }
    
    uint64_t l = m - 2;
    rank = (rank + l * fact) % MOD;
    fact = (fact * step) % MOD;
    step++;
    fact = (fact * step) % MOD;
    step++;
    
    for (int i = m - 2; i >= 0; --i) {
        uint64_t v = vals_arr[i];
        uint64_t li = (v - 1) + codes_arr[i];
        rank = (rank + li * fact) % MOD;
        fact = (fact * step) % MOD;
        step++;
    }
    
    free(vals_arr);
    free(codes_arr);
    free(new_vals_arr);
    free(new_codes_arr);
    
    return (int64_t)((rank + 1) % MOD);
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


def solve(power: int = 25) -> int:
    """Compute S(2^power) modulo 1000000007 using recursive Lehmer code reconstruction."""
    if power <= 5:
        target_size = 1 << (power - 1)
        vals = [1, 3, 2, 4]
        codes = [0, 1, 0, 0]
        size = 4
        while size < target_size:
            m = size
            n = m << 1
            new_vals = [0] * n
            new_codes = [0] * n
            for i in range(m - 1):
                v = vals[i]
                new_vals[i] = (v << 1) - 1
                new_codes[i] = (v - 1) + codes[i]
            new_vals[m - 1] = 2
            new_codes[m - 1] = 0
            v_last = vals[m - 1]
            new_vals[m] = (v_last << 1) - 1
            new_codes[m] = m - 2
            for j in range(1, m):
                v = vals[j]
                new_vals[m + j] = v << 1
                new_codes[m + j] = codes[j]
            vals, codes = new_vals, new_codes
            size = n

        m = target_size
        rank = 0
        fact = 1
        step = 1
        for j in range(m - 1, 0, -1):
            l_val = codes[j]
            rank = (rank + l_val * fact) % _MOD
            fact = (fact * step) % _MOD
            step += 1
        l_val = m - 2
        rank = (rank + l_val * fact) % _MOD
        fact = (fact * step) % _MOD
        step += 1
        fact = (fact * step) % _MOD
        step += 1
        for i in range(m - 2, -1, -1):
            v = vals[i]
            li = (v - 1) + codes[i]
            rank = (rank + li * fact) % _MOD
            fact = (fact * step) % _MOD
            step += 1
        return (rank + 1) % _MOD

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(power))
    return ans


if __name__ == "__main__":
    print(solve())
