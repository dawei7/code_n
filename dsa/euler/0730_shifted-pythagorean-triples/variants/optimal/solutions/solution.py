"""Project Euler Problem 730: Shifted Pythagorean Triples.

Find S(100, 10^8), where S(m, n) = sum_{k=0}^m P_k(n) and P_k(n) is the number of primitive
k-shifted Pythagorean triples 1 <= p <= q <= r with p^2 + q^2 + k = r^2 and p + q + r <= n.
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p730_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p730_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

static inline int gcd(int a, int b) {
    while (b) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

typedef struct {
    int p, q, r;
} Triple;

static Triple roots[105][500];
static int roots_count[105];

static inline bool is_root(int p, int q, int r) {
    int a1 = -2 * p - q + 2 * r;
    int b1 = p + 2 * q - 2 * r;
    int c1 = -2 * p - 2 * q + 3 * r;
    if (a1 > 0 && b1 > 0 && c1 > 0 && a1 <= b1 && b1 <= c1) return false;
    
    int a2 = p + 2 * q - 2 * r;
    int b2 = -2 * p - q + 2 * r;
    int c2 = -2 * p - 2 * q + 3 * r;
    if (a2 > 0 && b2 > 0 && c2 > 0 && a2 <= b2 && b2 <= c2) return false;
    
    int a3 = 2 * p + q - 2 * r;
    int b3 = p + 2 * q - 2 * r;
    int c3 = -2 * p - 2 * q + 3 * r;
    if (a3 > 0 && b3 > 0 && c3 > 0 && a3 <= b3 && b3 <= c3) return false;
    
    return true;
}

void generate_roots_c(int max_k) {
    for (int k = 0; k <= max_k; ++k) roots_count[k] = 0;
    
    roots[0][0] = (Triple){3, 4, 5};
    roots_count[0] = 1;
    
    int r_max = (5 * max_k + 1) / 2 + 10;
    for (int r = 1; r <= r_max; ++r) {
        int rr = r * r;
        for (int p = 1; p <= r; ++p) {
            int pp = p * p;
            for (int q = p; q <= r; ++q) {
                int k = rr - pp - q * q;
                if (k >= 1 && k <= max_k) {
                    if (gcd(p, gcd(q, r)) == 1) {
                        if (is_root(p, q, r)) {
                            roots[k][roots_count[k]++] = (Triple){p, q, r};
                        }
                    }
                }
            }
        }
    }
}

static Triple stack[1000000];

static inline int64_t count_from_roots(int64_t n, int k) {
    int top = 0;
    for (int i = 0; i < roots_count[k]; ++i) {
        stack[top++] = roots[k][i];
    }
    
    int64_t cnt = 0;
    while (top > 0) {
        Triple t = stack[--top];
        int64_t p = t.p;
        int64_t q = t.q;
        int64_t r = t.r;
        
        if (p + q + r > n) continue;
        cnt++;
        
        int64_t p1 = -2 * p + q + 2 * r;
        int64_t q1 = -p + 2 * q + 2 * r;
        int64_t r1 = -2 * p + 2 * q + 3 * r;
        int64_t s1 = -5 * p + 5 * q + 7 * r;
        if (s1 <= n) stack[top++] = (Triple){p1, q1, r1};
        
        int64_t p2 = p - 2 * q + 2 * r;
        int64_t q2 = 2 * p - q + 2 * r;
        int64_t r2 = 2 * p - 2 * q + 3 * r;
        int64_t s2 = 5 * p - 5 * q + 7 * r;
        if (s2 <= n && !(p2 == p1 && q2 == q1 && r2 == r1)) {
            stack[top++] = (Triple){p2, q2, r2};
        }
        
        int64_t p3 = 2 * p + q + 2 * r;
        int64_t q3 = p + 2 * q + 2 * r;
        int64_t r3 = 2 * p + 2 * q + 3 * r;
        int64_t s3 = 5 * p + 5 * q + 7 * r;
        if (s3 <= n && !((p3 == p1 && q3 == q1 && r3 == r1) || (p3 == p2 && q3 == q2 && r3 == r2))) {
            stack[top++] = (Triple){p3, q3, r3};
        }
    }
    return cnt;
}

int64_t solve_c(int max_k, int64_t n) {
    generate_roots_c(max_k);
    int64_t total = 0;
    for (int k = 0; k <= max_k; ++k) {
        total += count_from_roots(n, k);
    }
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
    lib.solve_c.argtypes = [ctypes.c_int, ctypes.c_int64]
    return lib


def solve(m: int = 100, n: int = 100_000_000) -> int:
    """Compute S(m, n) using Berggren Lorentz tree generation from fundamental shifted roots."""
    if n <= 10_000:
        # Pure Python fallback
        def is_root(p: int, q: int, r: int) -> bool:
            for m_inv in (
                ((-2, -1, 2), (1, 2, -2), (-2, -2, 3)),
                ((1, 2, -2), (-2, -1, 2), (-2, -2, 3)),
                ((2, 1, -2), (1, 2, -2), (-2, -2, 3)),
            ):
                a = m_inv[0][0] * p + m_inv[0][1] * q + m_inv[0][2] * r
                b = m_inv[1][0] * p + m_inv[1][1] * q + m_inv[1][2] * r
                c = m_inv[2][0] * p + m_inv[2][1] * q + m_inv[2][2] * r
                if a > 0 and b > 0 and c > 0 and a <= b <= c:
                    return False
            return True

        roots = [[] for _ in range(m + 1)]
        roots[0] = [(3, 4, 5)]
        r_max = (5 * m + 1) // 2 + 10
        for r in range(1, r_max + 1):
            rr = r * r
            for p in range(1, r + 1):
                pp = p * p
                for q in range(p, r + 1):
                    k = rr - pp - q * q
                    if 1 <= k <= m:
                        if math.gcd(p, math.gcd(q, r)) == 1:
                            if is_root(p, q, r):
                                roots[k].append((p, q, r))

        total = 0
        for k in range(m + 1):
            stack = list(roots[k])
            cnt = 0
            while stack:
                p, q, r = stack.pop()
                if p + q + r > n:
                    continue
                cnt += 1
                p1 = -2 * p + q + 2 * r
                q1 = -p + 2 * q + 2 * r
                r1 = -2 * p + 2 * q + 3 * r
                s1 = -5 * p + 5 * q + 7 * r
                if s1 <= n:
                    stack.append((p1, q1, r1))

                p2 = p - 2 * q + 2 * r
                q2 = 2 * p - q + 2 * r
                r2 = 2 * p - 2 * q + 3 * r
                s2 = 5 * p - 5 * q + 7 * r
                if s2 <= n and not (p2 == p1 and q2 == q1 and r2 == r1):
                    stack.append((p2, q2, r2))

                p3 = 2 * p + q + 2 * r
                q3 = p + 2 * q + 2 * r
                r3 = 2 * p + 2 * q + 3 * r
                s3 = 5 * p + 5 * q + 7 * r
                if s3 <= n and not (
                    (p3 == p1 and q3 == q1 and r3 == r1)
                    or (p3 == p2 and q3 == q2 and r3 == r2)
                ):
                    stack.append((p3, q3, r3))
            total += cnt
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(m, n))
    return ans


if __name__ == "__main__":
    print(solve())
