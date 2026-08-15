
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MOD 1000000007ULL

static int64_t count_tuples_c(int64_t N, int m, int64_t min_val) {
    if (m == 1) {
        if (min_val > N) return 0;
        return N - min_val + 1;
    }
    if (m == 2) {
        int64_t r = (int64_t)sqrt((double)N);
        while ((r + 1) * (r + 1) <= N) r++;
        while (r * r > N) r--;
        if (min_val > r) return 0;
        int64_t tot = 0;
        for (int64_t y = min_val; y <= r; ++y) {
            tot += (N / y - y + 1);
        }
        return tot;
    }
    
    int64_t total = 0;
    int64_t y = min_val;
    while (1) {
        int64_t p = 1;
        for (int i = 0; i < m; ++i) {
            if (N / y < p) { p = N + 1; break; }
            p *= y;
        }
        if (p > N) break;
        total += count_tuples_c(N / y, m - 1, y);
        y++;
    }
    return total;
}

int64_t solve_c(int64_t N, int64_t K) {
    int64_t total = K % MOD;
    int m = 1;
    while ((1ULL << m) <= (uint64_t)N) {
        int64_t c = count_tuples_c(N, m, 2);
        int64_t weight = (K - m + 1) % MOD;
        total = (total + (__int128)(c % MOD) * weight) % MOD;
        m++;
    }
    return total;
}
