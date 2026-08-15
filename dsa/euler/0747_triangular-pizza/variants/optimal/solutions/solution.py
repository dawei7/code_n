"""Project Euler Problem 747: Triangular Pizza.

Find Psi(10^8) modulo 1000000007, where Psi(m) = sum_{n=3}^m psi(n) and psi(n) is the number
of ways to cut a triangular pizza into n equal-area triangular pieces from an interior point.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p747_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p747_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007ULL

static inline int64_t isqrt_64(int64_t n) {
    if (n <= 0) return 0;
    int64_t x = (int64_t)sqrt((double)n);
    while ((x + 1) * (x + 1) <= n) x++;
    while (x * x > n) x--;
    return x;
}

static uint64_t easy_prefix_c(int64_t m) {
    if (m < 3) return 0;
    uint64_t m_mod = m % MOD;
    uint64_t m2 = (uint64_t)((__int128)m_mod * m_mod % MOD);
    uint64_t m3 = (uint64_t)((__int128)m2 * m_mod % MOD);
    
    uint64_t num = (m3 + 15 * m2 + MOD - (52 * m_mod % MOD) + 36) % MOD;
    uint64_t inv6 = 166666668ULL;
    return (uint64_t)((__int128)num * inv6 % MOD);
}

static int64_t min_n_and_sq(int64_t x, int64_t y, int *sq) {
    int64_t four_d = 4 * x * (x + 1) * y * (y + 1);
    int64_t r = isqrt_64(four_d);
    if (r * r == four_d) {
        *sq = 1;
        return 2 * x * y + x + y + 1 + r;
    } else {
        *sq = 0;
        return 2 * x * y + x + y + 1 + r + 1;
    }
}

static int64_t y_max_for_x_c(int64_t m, int64_t x) {
    if (4 * x > m - 1) return x - 1;
    int64_t hi = (m - 1) / (4 * x) + 2;
    if (hi < x) hi = x;
    int64_t lo = x;
    int64_t ok = x - 1;
    while (lo <= hi) {
        int64_t mid = lo + (hi - lo) / 2;
        int sq;
        int64_t n_min = min_n_and_sq(x, mid, &sq);
        if (n_min <= m) {
            ok = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ok;
}

static uint64_t hard_prefix_c(int64_t m) {
    if (m < 3) return 0;
    int64_t k = (m - 1) / 4;
    if (k <= 0) return 0;
    int64_t x_max = isqrt_64(k);
    
    uint64_t total = 0;
    for (int64_t x = 1; x <= x_max; ++x) {
        int64_t y_max = y_max_for_x_c(m, x);
        if (y_max < x) continue;
        
        int64_t A = x * (x + 1);
        int64_t y = x;
        int64_t yy1 = y * (y + 1);
        int64_t two_xy = 2 * x * y;
        
        while (y <= y_max) {
            int64_t four_d = (A * yy1) << 2;
            int64_t r = isqrt_64(four_d);
            int sq = (r * r == four_d) ? 1 : 0;
            int64_t ceil2 = sq ? r : (r + 1);
            int64_t n_min = two_xy + x + y + 1 + ceil2;
            if (n_min <= m) {
                int64_t cnt = 2 * (m - n_min + 1) - sq;
                uint64_t add = (x == y) ? cnt : (cnt << 1);
                total += add;
                if (total >= (MOD << 20)) total %= MOD;
            }
            yy1 += (y << 1) + 2;
            y++;
            two_xy += (x << 1);
        }
    }
    return total % MOD;
}

uint64_t Psi_c(int64_t m) {
    uint64_t easy = easy_prefix_c(m);
    uint64_t hard = hard_prefix_c(m);
    return (easy + 3 * hard) % MOD;
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
    lib.Psi_c.restype = ctypes.c_uint64
    lib.Psi_c.argtypes = [ctypes.c_int64]
    return lib


def solve(m: int = 100_000_000) -> int:
    """Compute Psi(m) modulo 1000000007 using hyperbolic skeleton decomposition."""
    if m <= 1000:
        easy = (m**3 + 15 * m**2 - 52 * m + 36) // 6 if m >= 3 else 0
        k = (m - 1) // 4
        x_max = int(k**0.5) if k > 0 else 0
        hard = 0
        for x in range(1, x_max + 1):
            A = x * (x + 1)
            y = x
            while True:
                four_d = 4 * A * y * (y + 1)
                r = int(four_d**0.5)
                sq = 1 if r * r == four_d else 0
                ceil2 = r if sq else r + 1
                n_min = 2 * x * y + x + y + 1 + ceil2
                if n_min > m:
                    break
                cnt = 2 * (m - n_min + 1) - sq
                hard += cnt if x == y else 2 * cnt
                y += 1
        return (easy + 3 * hard) % _MOD

    lib = _get_compiled_lib()
    ans = int(lib.Psi_c(m))
    return ans


if __name__ == "__main__":
    print(solve())
