"""Project Euler 814: Mezzo-forte

Calculates S(n), the number of valid configurations of 4n people screaming loud or quiet
such that exactly 2n people scream loud, modulo 998244353.
"""

from __future__ import annotations
import subprocess
import tempfile
from pathlib import Path


def solve(n: int = 1000, mod: int = 998244353) -> int:
    """Computes S(n) mod 998244353 using slice dynamic programming with circular wrap-around."""
    # Fast C implementation
    c_code = r"""
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static inline int popcount(int x) {
    return (x & 1) + ((x >> 1) & 1);
}

int main(int argc, char** argv) {
    if (argc < 3) return 1;
    int n = atoi(argv[1]);
    int64_t mod = atoll(argv[2]);

    int valid_trans[4][4][4];
    for (int p = 0; p < 4; p++) {
        for (int c = 0; c < 4; c++) {
            for (int nx = 0; nx < 4; nx++) {
                int p0 = p & 1, p1 = (p >> 1) & 1;
                int c0 = c & 1, c1 = (c >> 1) & 1;
                int n0 = nx & 1, n1 = (nx >> 1) & 1;
                int ok = 1;
                int req0 = c0 ? 2 : 1;
                if (p0 + c1 + n0 != req0) ok = 0;
                int req1 = c1 ? 2 : 1;
                if (p1 + c0 + n1 != req1) ok = 0;
                valid_trans[p][c][nx] = ok;
            }
        }
    }

    int64_t* dp = (int64_t*)calloc(4 * 4 * (n + 1), sizeof(int64_t));
    int64_t* next_dp = (int64_t*)calloc(4 * 4 * (n + 1), sizeof(int64_t));

    for (int m0 = 0; m0 < 4; m0++) {
        int cnt0 = popcount(m0);
        if (cnt0 <= n) {
            dp[m0 * 4 * (n + 1) + m0 * (n + 1) + cnt0] = 1;
        }
    }

    for (int k = 0; k < 2 * n - 1; k++) {
        memset(next_dp, 0, 4 * 4 * (n + 1) * sizeof(int64_t));
        for (int m0 = 0; m0 < 4; m0++) {
            for (int cur = 0; cur < 4; cur++) {
                for (int c = 0; c <= n; c++) {
                    int64_t val = dp[m0 * 4 * (n + 1) + cur * (n + 1) + c];
                    if (!val) continue;
                    for (int nx = 0; nx < 4; nx++) {
                        int delta = popcount(nx);
                        if (c + delta > n) continue;
                        for (int prev = 0; prev < 4; prev++) {
                            if (valid_trans[prev][cur][nx]) {
                                int idx = m0 * 4 * (n + 1) + nx * (n + 1) + (c + delta);
                                next_dp[idx] = (next_dp[idx] + val) % mod;
                                break;
                            }
                        }
                    }
                }
            }
        }
        int64_t* tmp = dp;
        dp = next_dp;
        next_dp = tmp;
    }

    int64_t total = 0;
    for (int m0 = 0; m0 < 4; m0++) {
        for (int last = 0; last < 4; last++) {
            int64_t val = dp[m0 * 4 * (n + 1) + last * (n + 1) + n];
            if (!val) continue;
            for (int prev = 0; prev < 4; prev++) {
                if (valid_trans[prev][last][m0]) {
                    total = (total + val) % mod;
                    break;
                }
            }
        }
    }

    free(dp);
    free(next_dp);
    printf("%lld\n", total);
    return 0;
}
"""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            c_file = Path(tmpdir) / "p814.c"
            bin_file = Path(tmpdir) / "p814.exe"
            c_file.write_text(c_code, encoding="utf-8")
            subprocess.run(["gcc", "-O3", str(c_file), "-o", str(bin_file)], check=True, capture_output=True)
            res = subprocess.run([str(bin_file), str(n), str(mod)], check=True, capture_output=True, text=True)
            return int(res.stdout.strip())
    except Exception:
        pass

    # Fallback Pure Python DP
    valid_trans = {}
    for p in range(4):
        for c in range(4):
            for nx in range(4):
                p0, p1 = p & 1, (p >> 1) & 1
                c0, c1 = c & 1, (c >> 1) & 1
                n0, n1 = nx & 1, (nx >> 1) & 1
                if (p0 + c1 + n0 == (2 if c0 else 1)) and (p1 + c0 + n1 == (2 if c1 else 1)):
                    valid_trans.setdefault((p, c), []).append(nx)

    dp = {}
    for m0 in range(4):
        cnt = (m0 & 1) + ((m0 >> 1) & 1)
        if cnt <= n:
            dp[(m0, m0, cnt)] = 1

    for step in range(2 * n - 1):
        next_dp = {}
        for (m0, cur, count), val in dp.items():
            for nx in range(4):
                delta = (nx & 1) + ((nx >> 1) & 1)
                if count + delta > n:
                    continue
                # Check if there exists any prev transition
                if any(nx in valid_trans.get((prev, cur), []) for prev in range(4)):
                    key = (m0, nx, count + delta)
                    next_dp[key] = (next_dp.get(key, 0) + val) % mod
        dp = next_dp

    total = 0
    for (m0, last, count), val in dp.items():
        if count == n:
            if any(m0 in valid_trans.get((prev, last), []) for prev in range(4)):
                total = (total + val) % mod

    return total


if __name__ == "__main__":
    print(solve())
