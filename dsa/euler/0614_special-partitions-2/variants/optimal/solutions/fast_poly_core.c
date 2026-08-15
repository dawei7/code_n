
#include <stdint.h>
#define MOD 1000000007LL

void poly_mul_sparse_c(int64_t* res, const int64_t* poly_dense, const int32_t* powers, const int32_t* signs, int num_terms, int limit) {
    for (int i = 0; i <= limit; ++i) res[i] = poly_dense[i];
    for (int t = 0; t < num_terms; ++t) {
        int p = powers[t];
        int s = signs[t];
        if (s == 1) {
            for (int i = p; i <= limit; ++i) {
                res[i] += poly_dense[i - p];
                if (res[i] >= MOD) res[i] -= MOD;
            }
        } else {
            for (int i = p; i <= limit; ++i) {
                res[i] -= poly_dense[i - p];
                if (res[i] < 0) res[i] += MOD;
            }
        }
    }
}

void poly_div_sparse_c(int64_t* F, const int64_t* num_dense, const int32_t* powers, const int32_t* signs, int num_terms, int limit) {
    for (int n = 0; n <= limit; ++n) {
        int64_t v = num_dense[n];
        for (int t = 0; t < num_terms; ++t) {
            int p = powers[t];
            if (p > n) break;
            int s = signs[t];
            if (s == 1) {
                v -= F[n - p];
            } else {
                v += F[n - p];
            }
        }
        v %= MOD;
        if (v < 0) v += MOD;
        F[n] = v;
    }
}
