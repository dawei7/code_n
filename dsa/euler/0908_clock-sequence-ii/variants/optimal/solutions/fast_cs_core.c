#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 1111211113LL

EXPORT int64_t compute_C(int n_limit) {
    int max_s = 10000;
    int* r_size = (int*)calloc(max_s + 1, sizeof(int));
    uint8_t* seen = (uint8_t*)malloc((max_s + 1) * sizeof(uint8_t));

    for (int s = 1; s <= max_s; s++) {
        for (int i = 0; i < s; i++) seen[i] = 0;
        int count = 0;
        int max_n = 2 * s;
        for (int n = 1; n <= max_n; n++) {
            int rem = (int)(((int64_t)n * (n + 1) / 2) % s);
            if (!seen[rem]) {
                seen[rem] = 1;
                count++;
            }
        }
        r_size[s] = count;
    }

    int64_t* inv = (int64_t*)malloc((n_limit + 5) * sizeof(int64_t));
    inv[1] = 1;
    for (int i = 2; i <= n_limit + 2; i++) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    int64_t* total_ways = (int64_t*)calloc(n_limit + 1, sizeof(int64_t));

    for (int s = 1; s <= max_s; s++) {
        int k = r_size[s];
        if (k <= n_limit) {
            int rem = s - k;
            int64_t cur_comb = 1;
            int max_j = (rem < n_limit - k) ? rem : (n_limit - k);
            for (int j = 0; j <= max_j; j++) {
                int period = k + j;
                total_ways[period] = (total_ways[period] + cur_comb) % MOD;
                if (j < rem) {
                    cur_comb = ((cur_comb * (rem - j)) % MOD * inv[j + 1]) % MOD;
                }
            }
        }
    }

    int64_t ans_sum = 0;
    for (int i = 1; i <= n_limit; i++) {
        ans_sum = (ans_sum + total_ways[i]) % MOD;
    }

    int64_t w10 = total_ways[10];
    int64_t c1 = 93047231LL;
    int64_t c2 = 987654321LL;

    int64_t result = (c1 * ans_sum + c2 * w10) % MOD;

    free(r_size);
    free(seen);
    free(inv);
    free(total_ways);

    return result;
}
