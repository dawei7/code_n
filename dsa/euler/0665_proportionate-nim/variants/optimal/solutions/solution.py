"""Project Euler Problem 665: Proportionate Nim.

Find f(10^7), where f(M) is the sum of n + m for all losing positions (n, m) with n <= m and n + m <= M.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_prop_nim_core.dll")
    c_path = os.path.join(tmp_dir, "fast_prop_nim_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

static inline int dsu_find(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static inline void dsu_mark(int* parent, int x) {
    if (parent[x] == x) {
        parent[x] = dsu_find(parent, x + 1);
    }
}

int64_t solve_c(int64_t M) {
    int64_t half = M / 2;
    int max_coord = (int)(M * 1.25) + 100;
    
    int* coord_parent = (int*)malloc((max_coord + 2) * sizeof(int));
    int* diff_parent = (int*)malloc((max_coord + 2) * sizeof(int));
    for (int i = 0; i <= max_coord + 1; ++i) {
        coord_parent[i] = i;
        diff_parent[i] = i;
    }
    
    int v_min = -2 * max_coord;
    int v_offset = -v_min;
    int v_len = 3 * max_coord + 1;
    int* v_parent = (int*)malloc((v_len + 2) * sizeof(int));
    for (int i = 0; i <= v_len + 1; ++i) {
        v_parent[i] = i;
    }
    
    dsu_mark(coord_parent, 0);
    dsu_mark(diff_parent, 0);
    dsu_mark(v_parent, 0 + v_offset);
    
    int64_t total = 0;
    int a = 1;
    
    while (1) {
        a = dsu_find(coord_parent, a);
        if (a > half) break;
        
        int b = a + 1;
        int d = 0, v1 = 0, v2 = 0;
        
        while (1) {
            b = dsu_find(coord_parent, b);
            
            d = b - a;
            if (diff_parent[d] != d) {
                int nd = dsu_find(diff_parent, d);
                b = a + nd;
                continue;
            }
            
            v1 = b - 2 * a;
            int i1 = v1 + v_offset;
            if (v_parent[i1] != i1) {
                int ni = dsu_find(v_parent, i1);
                int next_v = ni - v_offset;
                b = 2 * a + next_v;
                continue;
            }
            
            v2 = a - 2 * b;
            int i2 = v2 + v_offset;
            if (v_parent[i2] != i2) {
                b++;
                continue;
            }
            
            break;
        }
        
        dsu_mark(coord_parent, a);
        dsu_mark(coord_parent, b);
        dsu_mark(diff_parent, d);
        dsu_mark(v_parent, v1 + v_offset);
        dsu_mark(v_parent, v2 + v_offset);
        
        if (a + b <= M) {
            total += (int64_t)(a + b);
        }
    }
    
    free(coord_parent);
    free(diff_parent);
    free(v_parent);
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


def solve(m_limit: int = 10_000_000) -> int:
    """Compute f(M) using the greedy successor-DSU algorithm for Proportionate Nim."""
    if m_limit <= 1000:
        coord_parent = list(range(int(m_limit * 1.5) + 100))
        diff_parent = list(range(int(m_limit * 1.5) + 100))
        v_offset = 2 * len(coord_parent)
        v_parent = list(range(4 * len(coord_parent)))

        def find_p(p, x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        def mark_p(p, x):
            if p[x] == x:
                p[x] = find_p(p, x + 1)

        mark_p(coord_parent, 0)
        mark_p(diff_parent, 0)
        mark_p(v_parent, 0 + v_offset)

        total = 0
        a = 1
        half = m_limit // 2
        while True:
            a = find_p(coord_parent, a)
            if a > half:
                break
            b = a + 1
            while True:
                b = find_p(coord_parent, b)
                d = b - a
                if diff_parent[d] != d:
                    b = a + find_p(diff_parent, d)
                    continue
                v1 = b - 2 * a
                i1 = v1 + v_offset
                if v_parent[i1] != i1:
                    b = 2 * a + find_p(v_parent, i1) - v_offset
                    continue
                v2 = a - 2 * b
                i2 = v2 + v_offset
                if v_parent[i2] != i2:
                    b += 1
                    continue
                break

            mark_p(coord_parent, a)
            mark_p(coord_parent, b)
            mark_p(diff_parent, d)
            mark_p(v_parent, v1 + v_offset)
            mark_p(v_parent, v2 + v_offset)

            if a + b <= m_limit:
                total += a + b
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(m_limit))
    return ans


if __name__ == "__main__":
    print(solve())
