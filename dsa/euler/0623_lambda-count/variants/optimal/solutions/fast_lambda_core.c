
#include <stdint.h>
#include <stdlib.h>
#define MOD 1000000007LL

void solve_dp_c(int64_t* result_pref, int max_n) {
    int max_k = max_n / 5 + 1;
    int64_t* dp = (int64_t*)calloc((max_n + 1) * (max_k + 1), sizeof(int64_t));
    
    #define DP(n, k) dp[(n) * (max_k + 1) + (k)]
    
    for (int k = 0; k <= max_k; ++k) {
        DP(1, k) = k;
    }
    
    for (int n = 2; n <= max_n; ++n) {
        if (n >= 6) {
            for (int k = 0; k < max_k; ++k) {
                DP(n, k) = (DP(n, k) + DP(n - 5, k + 1)) % MOD;
            }
        }
        if (n >= 4) {
            int rem = n - 2;
            for (int j = 1; j < rem; ++j) {
                int l1 = j;
                int l2 = rem - j;
                for (int k = 0; k <= max_k; ++k) {
                    DP(n, k) = (DP(n, k) + DP(l1, k) * DP(l2, k)) % MOD;
                }
            }
        }
    }
    
    int64_t s = 0;
    for (int n = 1; n <= max_n; ++n) {
        s = (s + DP(n, 0)) % MOD;
        result_pref[n] = s;
    }
    
    free(dp);
}
