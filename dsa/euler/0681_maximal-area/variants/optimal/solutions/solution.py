"""Project Euler Problem 681: Maximal Area.

Find SP(10^6), the sum of a+b+c+d over all choices a <= b <= c <= d for which the maximal area
M(a, b, c, d) of a cyclic quadrilateral is a positive integer <= 10^6.
"""

import ctypes
import math
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p681_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p681_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

static int spf[1000005];

void init_spf(int n) {
    for (int i = 0; i <= n; ++i) spf[i] = i;
    for (int i = 2; i * i <= n; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= n; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

typedef struct {
    int p;
    int e;
} Factor;

static int factorize(int n, Factor* fac) {
    int cnt = 0;
    while (n > 1) {
        int p = spf[n];
        int e = 0;
        while (n % p == 0) {
            n /= p;
            e++;
        }
        fac[cnt].p = p;
        fac[cnt].e = e;
        cnt++;
    }
    return cnt;
}

static int64_t divs[50000];
static int dlen = 0;

static void gen_divs(Factor* fac, int n_fac, int idx, int64_t cur, int64_t k) {
    if (idx == n_fac) {
        divs[dlen++] = cur;
        return;
    }
    int p = fac[idx].p;
    int max_e = 2 * fac[idx].e;
    int64_t pw = 1;
    for (int e = 0; e <= max_e; ++e) {
        if (cur > k / pw) break;
        gen_divs(fac, n_fac, idx + 1, cur * pw, k);
        if (e < max_e) pw *= p;
    }
}

static int cmp_int64(const void* a, const void* b) {
    int64_t va = *(const int64_t*)a;
    int64_t vb = *(const int64_t*)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int64_t solve_c(int n) {
    init_spf(n);
    int64_t total = 0;
    Factor fac[16];
    
    for (int k = 1; k <= n; ++k) {
        int64_t k2 = (int64_t)k * k;
        int n_fac = factorize(k, fac);
        dlen = 0;
        gen_divs(fac, n_fac, 0, 1, k);
        qsort(divs, dlen, sizeof(int64_t), cmp_int64);
        
        for (int ti = 0; ti < dlen; ++ti) {
            int64_t T = divs[ti];
            if (T * T > k) break;
            
            int64_t k2_div_T = k2 / T;
            
            for (int wi = ti; wi < dlen; ++wi) {
                int64_t W = divs[wi];
                if (W * W * W > k2_div_T) break;
                if (k2_div_T % W != 0) continue;
                
                int64_t R = k2_div_T / W;
                int64_t vmax = (int64_t)sqrt(R);
                if (vmax < W) break;
                if (vmax > k) vmax = k;
                
                int64_t S = W + T;
                int64_t disc = S * S + 4 * R;
                int64_t root = (int64_t)sqrt(disc);
                int64_t vmin = (root - S) / 2 + 1;
                if (vmin < W) vmin = W;
                if (vmin > vmax) continue;
                
                int lo = wi, hi = dlen - 1, start_vi = dlen;
                while (lo <= hi) {
                    int mid = lo + (hi - lo) / 2;
                    if (divs[mid] >= vmin) {
                        start_vi = mid;
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                }
                
                for (int vi = start_vi; vi < dlen; ++vi) {
                    int64_t V = divs[vi];
                    if (V > vmax) break;
                    if (R % V != 0) continue;
                    
                    int64_t U = R / V;
                    int64_t p = U + V + S;
                    if ((p & 1) == 0) {
                        total += p;
                    }
                }
            }
        }
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
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(n: int = 1_000_000) -> int:
    """Compute SP(n) using Brahmagupta 4-factor square decomposition and divisor sieve."""
    if n <= 100:
        spf = list(range(n + 1))
        for i in range(2, int(n**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        total = 0
        for k in range(1, n + 1):
            k2 = k * k
            # factorize k
            temp = k
            fac = []
            while temp > 1:
                p = spf[temp]
                e = 0
                while temp % p == 0:
                    temp //= p
                    e += 1
                fac.append((p, e))

            divs = [1]
            for p, e in fac:
                cur = []
                pk = 1
                for _ in range(2 * e + 1):
                    for d in divs:
                        if d * pk <= k:
                            cur.append(d * pk)
                    pk *= p
                divs = list(set(cur))
            divs.sort()

            dlen = len(divs)
            for ti in range(dlen):
                T = divs[ti]
                if T * T > k:
                    break
                k2_div_T = k2 // T
                for wi in range(ti, dlen):
                    W = divs[wi]
                    if W * W * W > k2_div_T:
                        break
                    if k2_div_T % W != 0:
                        continue
                    R = k2_div_T // W
                    vmax = math.isqrt(R)
                    if vmax < W:
                        break
                    vmax = min(vmax, k)
                    S = W + T
                    disc = S * S + 4 * R
                    vmin = (math.isqrt(disc) - S) // 2 + 1
                    vmin = max(vmin, W)
                    if vmin > vmax:
                        continue
                    for vi in range(wi, dlen):
                        V = divs[vi]
                        if V < vmin:
                            continue
                        if V > vmax:
                            break
                        if R % V != 0:
                            continue
                        U = R // V
                        p = U + V + S
                        if p % 2 == 0:
                            total += p
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
