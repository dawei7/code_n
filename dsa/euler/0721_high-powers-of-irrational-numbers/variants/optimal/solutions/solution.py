"""Project Euler Problem 721: High Powers of Irrational Numbers.

Find G(5000000) mod 999999937, where G(n) = sum_{a=1}^n f(a, a^2) and
f(a, n) = floor((ceil(sqrt(a)) + sqrt(a))^n).
"""

import ctypes
import os
import subprocess

_MOD = 999_999_937


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p721_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p721_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 999999937ULL

static inline uint64_t pow_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

int64_t solve_c(int limit) {
    uint64_t total = 0;
    int64_t c = 1;
    
    for (int64_t a = 1; a <= limit; ++a) {
        while ((c - 1) * (c - 1) >= a) c--;
        while (c * c < a) c++;
        
        uint64_t n = (uint64_t)a * a;
        if (a == c * c) {
            uint64_t val = pow_mod(2 * c, n, MOD);
            total = (total + val) % MOD;
        } else {
            uint64_t m00 = (2 * c) % MOD;
            uint64_t disc = c * c - a;
            uint64_t m01 = (MOD - (disc % MOD)) % MOD;
            
            uint64_t exp = n - 1;
            uint64_t r00 = 1, r01 = 0, r10 = 0, r11 = 1;
            uint64_t b00 = m00, b01 = m01, b10 = 1, b11 = 0;
            
            while (exp > 0) {
                if (exp & 1) {
                    uint64_t nr00 = (r00 * b00 + r01 * b10) % MOD;
                    uint64_t nr01 = (r00 * b01 + r01 * b11) % MOD;
                    uint64_t nr10 = (r10 * b00 + r11 * b10) % MOD;
                    uint64_t nr11 = (r10 * b01 + r11 * b11) % MOD;
                    r00 = nr00; r01 = nr01; r10 = nr10; r11 = nr11;
                }
                uint64_t nb00 = (b00 * b00 + b01 * b10) % MOD;
                uint64_t nb01 = (b00 * b01 + b01 * b11) % MOD;
                uint64_t nb10 = (b10 * b00 + b11 * b10) % MOD;
                uint64_t nb11 = (b10 * b01 + b11 * b11) % MOD;
                b00 = nb00; b01 = nb01; b10 = nb10; b11 = nb11;
                exp >>= 1;
            }
            uint64_t u_n = (r00 * (2 * c) + r01 * 2) % MOD;
            uint64_t val = (u_n + MOD - 1) % MOD;
            total = (total + val) % MOD;
        }
    }
    return (int64_t)total;
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


def solve(limit: int = 5_000_000) -> int:
    """Compute G(limit) modulo 999999937 using 2x2 matrix recurrence exponentiation."""
    if limit <= 1000:
        total = 0
        c = 1
        for a in range(1, limit + 1):
            while (c - 1) * (c - 1) >= a:
                c -= 1
            while c * c < a:
                c += 1
            n = a * a
            if a == c * c:
                val = pow(2 * c, n, _MOD)
                total = (total + val) % _MOD
            else:
                m00 = (2 * c) % _MOD
                disc = c * c - a
                m01 = (-disc) % _MOD
                exp = n - 1
                r00, r01, r10, r11 = 1, 0, 0, 1
                b00, b01, b10, b11 = m00, m01, 1, 0
                while exp > 0:
                    if exp & 1:
                        nr00 = (r00 * b00 + r01 * b10) % _MOD
                        nr01 = (r00 * b01 + r01 * b11) % _MOD
                        nr10 = (r10 * b00 + r11 * b10) % _MOD
                        nr11 = (r10 * b01 + r11 * b11) % _MOD
                        r00, r01, r10, r11 = nr00, nr01, nr10, nr11
                    nb00 = (b00 * b00 + b01 * b10) % _MOD
                    nb01 = (b00 * b01 + b01 * b11) % _MOD
                    nb10 = (b10 * b00 + b11 * b10) % _MOD
                    nb11 = (b10 * b01 + b11 * b11) % _MOD
                    b00, b01, b10, b11 = nb00, nb01, nb10, nb11
                    exp >>= 1
                u_n = (r00 * (2 * c) + r01 * 2) % _MOD
                val = (u_n - 1) % _MOD
                total = (total + val) % _MOD
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(limit))
    return ans


if __name__ == "__main__":
    print(solve())
