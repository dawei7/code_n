"""Project Euler Problem 662: Fibonacci Paths.

Find F(10000, 10000) mod 1000000007, where F(W, H) is the number of lattice paths
from (0, 0) to (W, H) whose step Euclidean lengths are Fibonacci numbers.
"""

import ctypes
import math
import os
import subprocess
from typing import List, Tuple

_MOD = 1_000_000_007


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_fib_paths_core.dll")
    c_path = os.path.join(tmp_dir, "fast_fib_paths_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007

int solve_c(int W, int H, int num_moves, int* moves_x, int* moves_y) {
    int stride = H + 1;
    int total_cells = (W + 1) * stride;
    int* dp = (int*)calloc(total_cells, sizeof(int));
    dp[0] = 1;
    
    for (int w = 0; w <= W; ++w) {
        int w_offset = w * stride;
        for (int h = 0; h <= H; ++h) {
            int cur_val = dp[w_offset + h];
            if (cur_val == 0) continue;
            
            for (int m = 0; m < num_moves; ++m) {
                int nw = w + moves_x[m];
                int nh = h + moves_y[m];
                if (nw <= W && nh <= H) {
                    int idx = nw * stride + nh;
                    dp[idx] += cur_val;
                    if (dp[idx] >= MOD) dp[idx] -= MOD;
                }
            }
        }
    }
    
    int ans = dp[W * stride + H];
    free(dp);
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
    lib.solve_c.restype = ctypes.c_int32
    lib.solve_c.argtypes = [
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.POINTER(ctypes.c_int32),
        ctypes.POINTER(ctypes.c_int32),
    ]
    return lib


def _generate_moves(w: int, h: int) -> List[Tuple[int, int]]:
    max_dist = math.isqrt(w * w + h * h)
    fibs = [1, 2]
    while True:
        nxt = fibs[-1] + fibs[-2]
        if nxt > max_dist:
            break
        fibs.append(nxt)

    moves = []
    for f in fibs:
        f2 = f * f
        for x in range(f + 1):
            y2 = f2 - x * x
            y = math.isqrt(y2)
            if y * y == y2 and y <= h and x <= w and (x > 0 or y > 0):
                moves.append((x, y))

    return sorted(set(moves))


def solve(w: int = 10000, h: int = 10000) -> int:
    """Compute F(W, H) modulo 1000000007 using 2D lattice push DP over Pythagorean Fibonacci step vectors."""
    moves = _generate_moves(w, h)

    if w <= 10 and h <= 10:
        stride = h + 1
        dp = [0] * ((w + 1) * stride)
        dp[0] = 1
        for cw in range(w + 1):
            w_off = cw * stride
            for ch in range(h + 1):
                val = dp[w_off + ch]
                if val == 0:
                    continue
                for mx, my in moves:
                    nw = cw + mx
                    nh = ch + my
                    if nw <= w and nh <= h:
                        idx = nw * stride + nh
                        dp[idx] = (dp[idx] + val) % _MOD
        return dp[w * stride + h]

    lib = _get_compiled_lib()
    num_moves = len(moves)
    arr_x = (ctypes.c_int32 * num_moves)(*[m[0] for m in moves])
    arr_y = (ctypes.c_int32 * num_moves)(*[m[1] for m in moves])
    ans = int(lib.solve_c(w, h, num_moves, arr_x, arr_y))
    return ans


if __name__ == "__main__":
    print(solve())
