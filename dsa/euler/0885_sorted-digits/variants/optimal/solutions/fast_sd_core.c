#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 1123455689LL

static int64_t fact[30];
static int64_t R[30];
static int64_t total_ans = 0;

static void dfs(int digit, int rem_n, int* counts, int64_t current_mult) {
    if (digit == 9) {
        counts[9] = rem_n;
        int64_t mult = current_mult / fact[rem_n];

        int64_t f_val = 0;
        int s_d = 0;
        for (int d = 9; d >= 1; d--) {
            s_d += counts[d];
            f_val = (f_val + R[s_d]) % MOD;
        }

        total_ans = (total_ans + (mult % MOD) * f_val) % MOD;
        return;
    }

    for (int c = 0; c <= rem_n; c++) {
        counts[digit] = c;
        dfs(digit + 1, rem_n - c, counts, current_mult / fact[c]);
    }
}

EXPORT int64_t compute_S(int n) {
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;

    int64_t r_val = 0;
    R[0] = 0;
    for (int k = 1; k <= n; k++) {
        r_val = (r_val * 10 + 1) % MOD;
        R[k] = r_val;
    }

    total_ans = 0;
    int counts[10];
    dfs(0, n, counts, fact[n]);

    return total_ans;
}
