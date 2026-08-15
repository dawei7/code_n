"""Project Euler Problem 641: A Long Row of Dice.

Find f(10^36), where f(n) is the number of dice showing 1 after turning every k-th die
for k = 2, ..., n.
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_dice_core.dll")
    c_path = os.path.join(tmp_dir, "fast_dice_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define SEG_SIZE 2000000

int64_t solve_c(int64_t n_exp) {
    int64_t max_b = 1000000000LL;
    
    int64_t sqrt_max = (int64_t)sqrt((double)max_b) + 10;
    uint8_t* is_p = (uint8_t*)malloc(sqrt_max + 1);
    for (int i = 0; i <= sqrt_max; ++i) is_p[i] = 1;
    is_p[0] = is_p[1] = 0;
    
    int* primes = (int*)malloc(sqrt_max * sizeof(int));
    int num_primes = 0;
    for (int i = 2; i <= sqrt_max; ++i) {
        if (is_p[i]) {
            primes[num_primes++] = i;
            for (int j = i * i; j <= sqrt_max; j += i) is_p[j] = 0;
        }
    }
    free(is_p);
    
    int32_t* rem = (int32_t*)malloc(SEG_SIZE * sizeof(int32_t));
    int8_t* mu = (int8_t*)malloc(SEG_SIZE * sizeof(int8_t));
    
    int64_t total = 0;
    
    for (int64_t low = 1; low <= max_b; low += SEG_SIZE) {
        int64_t high = low + SEG_SIZE - 1;
        if (high > max_b) high = max_b;
        int len = high - low + 1;
        
        for (int i = 0; i < len; ++i) {
            rem[i] = (int32_t)(low + i);
            mu[i] = 1;
        }
        
        for (int p_idx = 0; p_idx < num_primes; ++p_idx) {
            int p = primes[p_idx];
            int64_t p2 = (int64_t)p * p;
            
            int64_t start2 = ((low + p2 - 1) / p2) * p2;
            for (int64_t j = start2; j <= high; j += p2) {
                mu[j - low] = 0;
            }
            
            int64_t start = ((low + p - 1) / p) * p;
            for (int64_t j = start; j <= high; j += p) {
                int idx = j - low;
                if (mu[idx] != 0) {
                    mu[idx] = -mu[idx];
                    rem[idx] /= p;
                }
            }
        }
        
        for (int i = 0; i < len; ++i) {
            if (mu[i] != 0) {
                if (rem[i] > 1) {
                    mu[i] = -mu[i];
                }
                if (mu[i] == 1) {
                    int64_t b = low + i;
                    int64_t b2 = b * b;
                    int64_t val = 1000000000000000000LL / b2;
                    int64_t r = (int64_t)cbrt((double)val);
                    while ((r + 1) * (r + 1) * (r + 1) <= val) r++;
                    while (r * r * r > val) r--;
                    total += r;
                }
            }
        }
    }
    
    free(rem);
    free(mu);
    free(primes);
    
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
    lib.solve_c.argtypes = [ctypes.c_int64]
    return lib


def solve(n: int = 10**36) -> int:
    """Compute f(n) using segmented Mobius sieve on squarefree components b with mu(b)=1."""
    if n <= 10**8:
        b_max = int(n**0.25)
        mu = [0] * (b_max + 1)
        mu[1] = 1
        primes = []
        is_p = [True] * (b_max + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, b_max + 1):
            if is_p[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > b_max:
                    break
                is_p[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0
                    break
                mu[i * p] = -mu[i]

        ans = 0
        for b in range(1, b_max + 1):
            if mu[b] == 1:
                x = n // (b**4)
                r6 = int(x ** (1 / 6))
                while (r6 + 1) ** 6 <= x:
                    r6 += 1
                while r6**6 > x:
                    r6 -= 1
                ans += r6
        return ans

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(36))
    return ans


if __name__ == "__main__":
    print(solve())
