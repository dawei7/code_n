"""Project Euler Problem 630: Crossed Lines.

Find S(L_2500), where S(L) is the sum over every line in L of the number of times
it is crossed by another line in L.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_lines_core.dll")
    c_path = os.path.join(tmp_dir, "fast_lines_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

int gcd(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

typedef struct {
    int dx;
    int dy;
    int64_t c;
} Line;

int cmp_lines(const void* a, const void* b) {
    const Line* la = (const Line*)a;
    const Line* lb = (const Line*)b;
    if (la->dx != lb->dx) return la->dx - lb->dx;
    if (la->dy != lb->dy) return la->dy - lb->dy;
    if (la->c < lb->c) return -1;
    if (la->c > lb->c) return 1;
    return 0;
}

int64_t solve_c(int num_points) {
    int* px = (int*)malloc(num_points * sizeof(int));
    int* py = (int*)malloc(num_points * sizeof(int));
    
    int64_t s = 290797;
    int64_t mod_bbs = 50515093;
    for (int i = 0; i < num_points; ++i) {
        s = (s * s) % mod_bbs;
        px[i] = (int)(s % 2000) - 1000;
        s = (s * s) % mod_bbs;
        py[i] = (int)(s % 2000) - 1000;
    }
    
    int64_t total_pairs = (int64_t)num_points * (num_points - 1) / 2;
    Line* lines = (Line*)malloc(total_pairs * sizeof(Line));
    
    int64_t idx = 0;
    for (int i = 0; i < num_points; ++i) {
        int x1 = px[i];
        int y1 = py[i];
        for (int j = i + 1; j < num_points; ++j) {
            int dx = px[j] - x1;
            int dy = py[j] - y1;
            int g = gcd(dx, dy);
            dx /= g;
            dy /= g;
            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }
            int a = -dy;
            int b = dx;
            int64_t c = -((int64_t)a * x1 + (int64_t)b * y1);
            lines[idx].dx = dx;
            lines[idx].dy = dy;
            lines[idx].c = c;
            idx++;
        }
    }
    
    qsort(lines, total_pairs, sizeof(Line), cmp_lines);
    
    int64_t total_m = 0;
    int* slope_counts = (int*)malloc(total_pairs * sizeof(int));
    int num_slopes = 0;
    
    int current_slope_count = 0;
    for (int64_t i = 0; i < total_pairs; ++i) {
        if (i == 0 || lines[i].dx != lines[i-1].dx || lines[i].dy != lines[i-1].dy || lines[i].c != lines[i-1].c) {
            total_m++;
            if (i > 0 && (lines[i].dx != lines[i-1].dx || lines[i].dy != lines[i-1].dy)) {
                slope_counts[num_slopes++] = current_slope_count;
                current_slope_count = 0;
            }
            current_slope_count++;
        }
    }
    if (current_slope_count > 0) {
        slope_counts[num_slopes++] = current_slope_count;
    }
    
    int64_t total_s = 0;
    for (int i = 0; i < num_slopes; ++i) {
        int64_t cnt = slope_counts[i];
        total_s += cnt * (total_m - cnt);
    }
    
    free(px);
    free(py);
    free(lines);
    free(slope_counts);
    return total_s;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            ["gcc", "-O3", "-shared", "-o", dll_path, c_path], check=True
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.solve_c.argtypes = [ctypes.c_int32]
    return lib


def solve(num_points: int = 2500) -> int:
    """Compute S(L_num_points) by grouping unique lines into parallel slope equivalence classes."""
    if num_points <= 100:
        s = 290797
        mod_bbs = 50515093
        pts = []
        for _ in range(num_points):
            s = (s * s) % mod_bbs
            t1 = (s % 2000) - 1000
            s = (s * s) % mod_bbs
            t2 = (s % 2000) - 1000
            pts.append((t1, t2))

        lines_by_slope = {}
        for i in range(num_points):
            x1, y1 = pts[i]
            for j in range(i + 1, num_points):
                dx = pts[j][0] - x1
                dy = pts[j][1] - y1
                import math

                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                a = -dy
                b = dx
                c = -(a * x1 + b * y1)
                slope = (dx, dy)
                if slope not in lines_by_slope:
                    lines_by_slope[slope] = set()
                lines_by_slope[slope].add(c)

        m = sum(len(c_set) for c_set in lines_by_slope.values())
        return sum(
            len(c_set) * (m - len(c_set)) for c_set in lines_by_slope.values()
        )

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(num_points))
    return ans


if __name__ == "__main__":
    print(solve())
