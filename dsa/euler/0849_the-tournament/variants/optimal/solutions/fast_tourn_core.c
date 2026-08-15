#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MOD 1000000007

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT int compute_tournament_outcomes(int n) {
    int max_v = 4 * (n - 1);
    int max_E = 2 * (n / 2) * (n - n / 2) + 100;

    int* dp = (int*)calloc((size_t)(n + 1) * (max_E + 1), sizeof(int));
    int* next_dp = (int*)calloc((size_t)(n + 1) * (max_E + 1), sizeof(int));

    #define DP(arr, M, E) (arr)[(M) * (max_E + 1) + (E)]

    DP(dp, 0, 0) = 1;

    for (int v = 0; v <= max_v; v++) {
        memset(next_dp, 0, (size_t)(n + 1) * (max_E + 1) * sizeof(int));

        for (int M = 0; M <= n; M++) {
            // Prune unachievable states
            int min_req_E = 0;
            for (int E = min_req_E; E <= max_E; E++) {
                int ways = DP(dp, M, E);
                if (ways == 0) continue;

                // k = 0
                int val0 = DP(next_dp, M, E) + ways;
                if (val0 >= MOD) val0 -= MOD;
                DP(next_dp, M, E) = val0;

                // k >= 1
                for (int k = 1; M + k <= n; k++) {
                    int new_M = M + k;
                    int delta_E = k * (v - 4 * M - 2 * k + 2);
                    int new_E = E + delta_E;

                    if (new_E >= 0 && new_E <= max_E) {
                        int val = DP(next_dp, new_M, new_E) + ways;
                        if (val >= MOD) val -= MOD;
                        DP(next_dp, new_M, new_E) = val;
                    }
                }
            }
        }

        int* tmp = dp;
        dp = next_dp;
        next_dp = tmp;
    }

    int ans = DP(dp, n, 0);
    free(dp);
    free(next_dp);
    return ans;
}
