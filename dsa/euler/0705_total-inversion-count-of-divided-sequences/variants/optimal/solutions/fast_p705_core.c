
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL

static const int I_mat[10][10] = {
    {0,0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,0,0},
    {0,1,1,1,1,1,1,1,1,1},
    {0,1,2,1,2,1,2,1,2,1},
    {0,2,3,3,3,2,4,2,3,3},
    {0,1,2,2,3,1,3,1,3,2},
    {0,3,5,4,6,4,6,3,6,4},
    {0,1,2,2,3,2,4,1,3,2},
    {0,3,5,5,6,4,8,4,6,5},
    {0,2,4,3,5,3,6,3,6,3}
};

static const uint64_t k_arr[10] = {0, 1, 2, 2, 3, 2, 4, 2, 4, 3};
static const uint64_t w_arr[10] = {0, 1, 500000004, 500000004, 333333336, 500000004, 250000002, 500000004, 250000002, 333333336};

static uint8_t is_comp[100000005 / 8 + 1];

static inline int get_comp(int i) {
    return (is_comp[i >> 3] >> (i & 7)) & 1;
}

static inline void set_comp(int i) {
    is_comp[i >> 3] |= (1 << (i & 7));
}

int64_t solve_c(int limit) {
    for (int i = 0; i <= limit / 8 + 1; ++i) is_comp[i] = 0;
    set_comp(0);
    set_comp(1);
    for (int p = 2; p * p < limit; ++p) {
        if (!get_comp(p)) {
            for (int j = p * p; j < limit; j += p) {
                set_comp(j);
            }
        }
    }
    
    uint64_t W[10] = {0};
    uint64_t K_prod = 1;
    uint64_t S_sum = 0;
    
    char buf[16];
    
    for (int p = 2; p < limit; ++p) {
        if (!get_comp(p)) {
            int len = 0;
            int tmp = p;
            while (tmp > 0) {
                int d = tmp % 10;
                tmp /= 10;
                if (d > 0) {
                    buf[len++] = d;
                }
            }
            for (int idx = len - 1; idx >= 0; --idx) {
                int v = buf[idx];
                uint64_t wv = w_arr[v];
                
                uint64_t sum_u = 0;
                for (int u = 1; u <= 9; ++u) {
                    sum_u = (sum_u + (uint64_t)I_mat[u][v] * W[u]) % MOD;
                }
                
                S_sum = (S_sum + wv * sum_u) % MOD;
                W[v] = (W[v] + wv) % MOD;
                K_prod = (K_prod * k_arr[v]) % MOD;
            }
        }
    }
    
    uint64_t ans = (S_sum * K_prod) % MOD;
    return (int64_t)ans;
}
