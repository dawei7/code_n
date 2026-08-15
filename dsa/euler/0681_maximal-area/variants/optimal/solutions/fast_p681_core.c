
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
