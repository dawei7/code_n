#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 1111124111LL

EXPORT int64_t compute_F(int N) {
    // 1. Precompute c_m = (-1)^{m-1} F_m mod MOD for m <= N:
    int64_t* c = (int64_t*)malloc((N + 1) * sizeof(int64_t));
    c[0] = 0;
    if (N >= 1) c[1] = 1;
    if (N >= 2) c[2] = (MOD - 1); // (-1)^1 * F_2 = -1

    int64_t f_prev = 1, f_curr = 1;
    for (int m = 3; m <= N; m++) {
        int64_t f_next = (f_prev + f_curr) % MOD;
        f_prev = f_curr;
        f_curr = f_next;
        if (m % 2 == 1) {
            c[m] = f_curr;
        } else {
            c[m] = (MOD - f_curr) % MOD;
        }
    }

    // 2. Compute H_k = sum_{v | k} c_{k/v} mod MOD:
    int64_t* H = (int64_t*)calloc(N + 1, sizeof(int64_t));
    for (int d = 1; d <= N; d++) {
        int64_t c_d = c[d];
        if (c_d == 0) continue;
        for (int k = d; k <= N; k += d) {
            H[k] = (H[k] + c_d) % MOD;
        }
    }

    // 3. Compute F(n) via convolution F(n) = sum_{k=1}^n F(n - k) * H(k) mod MOD:
    int64_t* F = (int64_t*)calloc(N + 1, sizeof(int64_t));
    F[0] = 1;

    for (int n = 1; n <= N; n++) {
        __int128 sum = 0;
        // Inner loop
        for (int k = 1; k <= n; k++) {
            sum += (int64_t)F[n - k] * H[k];
        }
        F[n] = (int64_t)(sum % MOD);
    }

    int64_t ans = F[N];

    free(c);
    free(H);
    free(F);

    return ans;
}
