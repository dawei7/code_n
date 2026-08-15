"""Project Euler Problem 750: Optimal Card Stacking.

Find G(976), the minimal total horizontal drag distance to arrange the cards into a single
increasing consecutive sequence.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p750_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p750_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

static int pos[1005];
static int dp[1005][1005];

int64_t solve_c(int N) {
    int mod = N + 1;
    for (int i = 0; i <= N; ++i) pos[i] = 0;
    
    int x = 1;
    for (int i = 1; i <= N; ++i) {
        x = (int)(((int64_t)x * 3) % mod);
        if (x == 0 || x > N || pos[x] != 0) return -1;
        pos[x] = i;
    }
    for (int v = 1; v <= N; ++v) {
        if (pos[v] == 0) return -1;
    }
    
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            dp[i][j] = 0;
        }
    }
    
    for (int r = 2; r <= N; ++r) {
        int pr = pos[r];
        for (int l = r - 1; l >= 1; --l) {
            int best = 1000000000;
            for (int k = l; k < r; ++k) {
                int d = pos[k] - pr;
                if (d < 0) d = -d;
                int val = dp[l][k] + dp[k + 1][r] + d;
                if (val < best) best = val;
            }
            dp[l][r] = best;
        }
    }
    
    return dp[1][N];
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


def solve(n: int = 976) -> int:
    """Compute G(N) using interval dynamic programming."""
    if n <= 16:
        mod = n + 1
        pos = [0] * (n + 1)
        x = 1
        for i in range(1, n + 1):
            x = (x * 3) % mod
            pos[x] = i

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for r in range(2, n + 1):
            pr = pos[r]
            for l in range(r - 1, 0, -1):
                best = 10**9
                for k in range(l, r):
                    d = abs(pos[k] - pr)
                    val = dp[l][k] + dp[k + 1][r] + d
                    if val < best:
                        best = val
                dp[l][r] = best
        return dp[1][n]

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
