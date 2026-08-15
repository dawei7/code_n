#include <stdint.h>
#include <stdlib.h>

int64_t compute_S(int32_t N, int64_t MOD) {
    int64_t* D = (int64_t*)calloc(N + 1, sizeof(int64_t));
    int32_t* spf = (int32_t*)malloc((N + 1) * sizeof(int32_t));
    for (int32_t i = 0; i <= N; i++) spf[i] = i;
    for (int32_t i = 2; (int64_t)i * i <= N; i++) {
        if (spf[i] == i) {
            for (int32_t j = i * i; j <= N; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
    D[1] = 1;
    for (int32_t i = 2; i <= N; i++) {
        int32_t p = spf[i];
        int32_t rem = i / p;
        if (rem == 1) {
            D[i] = 1;
        } else {
            D[i] = ((int64_t)D[p] * rem + (int64_t)p * D[rem]) % MOD;
        }
    }
    free(spf);

    int64_t* c = (int64_t*)calloc(N + 1, sizeof(int64_t));
    for (int32_t k = 1; k <= N; k++) {
        int64_t D_k = D[k] % MOD;
        int64_t pow_D = D_k;
        for (int32_t m = k; m <= N; m += k) {
            c[m] = (c[m] + (int64_t)k * pow_D) % MOD;
            pow_D = ((__int128)pow_D * D_k) % MOD;
        }
    }
    free(D);

    int64_t* G = (int64_t*)calloc(N + 1, sizeof(int64_t));
    G[0] = 1;

    int32_t* inv = (int32_t*)malloc((N + 1) * sizeof(int32_t));
    inv[1] = 1;
    for (int32_t i = 2; i <= N; i++) {
        inv[i] = (int32_t)((int64_t)(MOD - MOD / i) * inv[MOD % i] % MOD);
    }

    for (int32_t n = 1; n <= N; n++) {
        int64_t s = 0;
        for (int32_t m = 1; m <= n; m++) {
            s += c[m] * G[n - m];
            if (s >= (int64_t)4e18) s %= MOD;
        }
        s %= MOD;
        G[n] = ((__int128)s * inv[n]) % MOD;
    }
    free(c);
    free(inv);

    int64_t total_S = 0;
    for (int32_t n = 1; n <= N; n++) {
        total_S = (total_S + G[n]) % MOD;
    }
    free(G);
    return total_S;
}
