
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

static int64_t dist[25000000];

int64_t solve_c(int p_val) {
    int64_t A = 1;
    int64_t B = 1;
    int64_t C = 1;
    for (int i = 0; i < p_val; ++i) {
        A *= 17;
        B *= 19;
        C *= 23;
    }
    
    int64_t cur_rem = 0;
    for (int64_t j = 0; j < A; ++j) {
        dist[cur_rem] = j * B;
        cur_rem += B;
        if (cur_rem >= A) cur_rem %= A;
    }
    
    cur_rem = 0;
    for (int pass = 0; pass < 2; ++pass) {
        for (int64_t j = 0; j < A; ++j) {
            int64_t nxt_rem = cur_rem + C;
            if (nxt_rem >= A) nxt_rem %= A;
            if (dist[cur_rem] + C < dist[nxt_rem]) {
                dist[nxt_rem] = dist[cur_rem] + C;
            }
            cur_rem = nxt_rem;
        }
    }
    
    __int128 S = (__int128)A + B + C;
    __int128 base_unreachable = S * (S - 1) / 2;
    
    __int128 g_count = 0;
    __int128 sigma_sum = 0;
    
    for (int64_t r = 0; r < A; ++r) {
        int64_t d_r = dist[r];
        int64_t k_r = (d_r - r) / A;
        g_count += k_r;
        __int128 term = (__int128)k_r * r + (__int128)A * (k_r - 1) * k_r / 2;
        sigma_sum += term;
    }
    
    __int128 total = base_unreachable + sigma_sum + S * g_count;
    uint64_t ans = (uint64_t)(total % MOD);
    return (int64_t)ans;
}
