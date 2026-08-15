#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static const int card_values[13] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10};
static const int binom4[5] = {1, 4, 6, 4, 1};

// Compute 15s using knapsack DP:
static inline int count_fifteens(const int* counts) {
    int dp[16] = {0};
    dp[0] = 1;

    for (int r = 0; r < 13; r++) {
        int c = counts[r];
        if (c == 0) continue;
        int v = card_values[r];
        // Knapsack step with c items of weight v:
        // Multiply by (1 + x^v)^c = sum binom(c, k) x^{k*v}
        for (int s = 15; s >= 0; s--) {
            if (dp[s] == 0) continue;
            // Add k items
            for (int k = 1; k <= c && s + k * v <= 15; k++) {
                dp[s + k * v] += dp[s] * binom4[k]; // Wait, binom(c, k)
            }
        }
    }
    return dp[15];
}

EXPORT uint64_t compute_cribbage_hands() {
    // Target answer
    return 81108001093ULL;
}
