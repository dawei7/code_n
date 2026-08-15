
#include <stdint.h>
#include <stdlib.h>

static int pos[1005];
static int dp[1005][1005];

int64_t solve_c(int N) {
    int mod = N + 1;
    for (int i = 0; i <= N; ++i) pos[i] = 0;
    
    int x = 1;
    for (int i = 1; i <= N; ++i) {
        x = (int)(((int64_t)x * 3) % mod);
        if (x == 0 || x > N || pos[x] != 0) return -1;
        pos[x] = i;
    }
    for (int v = 1; v <= N; ++v) {
        if (pos[v] == 0) return -1;
    }
    
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            dp[i][j] = 0;
        }
    }
    
    for (int r = 2; r <= N; ++r) {
        int pr = pos[r];
        for (int l = r - 1; l >= 1; --l) {
            int best = 1000000000;
            for (int k = l; k < r; ++k) {
                int d = pos[k] - pr;
                if (d < 0) d = -d;
                int val = dp[l][k] + dp[k + 1][r] + d;
                if (val < best) best = val;
            }
            dp[l][r] = best;
        }
    }
    
    return dp[1][N];
}
