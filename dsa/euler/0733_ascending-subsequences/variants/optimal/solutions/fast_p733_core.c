
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000007ULL
#define MAX_VAL 10000025

static uint32_t tree_cnt[5][MAX_VAL];
static uint64_t tree_sum[5][MAX_VAL];

static inline void add_cnt(int L, int idx, uint32_t val) {
    for (; idx < MAX_VAL; idx += idx & -idx) {
        uint32_t cur = tree_cnt[L][idx] + val;
        if (cur >= MOD) cur -= MOD;
        tree_cnt[L][idx] = cur;
    }
}

static inline uint32_t query_cnt(int L, int idx) {
    uint32_t res = 0;
    for (; idx > 0; idx -= idx & -idx) {
        res += tree_cnt[L][idx];
        if (res >= MOD) res -= MOD;
    }
    return res;
}

static inline void add_sum(int L, int idx, uint64_t val) {
    for (; idx < MAX_VAL; idx += idx & -idx) {
        tree_sum[L][idx] = (tree_sum[L][idx] + val) % MOD;
    }
}

static inline uint64_t query_sum(int L, int idx) {
    uint64_t res = 0;
    for (; idx > 0; idx -= idx & -idx) {
        res = (res + tree_sum[L][idx]) % MOD;
    }
    return res;
}

int64_t solve_c(int n) {
    for (int L = 1; L <= 4; ++L) {
        for (int i = 0; i < MAX_VAL; ++i) {
            tree_cnt[L][i] = 0;
            tree_sum[L][i] = 0;
        }
    }
    
    uint64_t cur_a = 153;
    uint64_t mod_a = 10000019;
    
    uint64_t total_s4 = 0;
    
    for (int i = 1; i <= n; ++i) {
        int x = (int)cur_a;
        
        uint32_t c3 = query_cnt(3, x - 1);
        uint64_t s3 = query_sum(3, x - 1);
        uint64_t s4 = (s3 + (__int128)c3 * x) % MOD;
        total_s4 = (total_s4 + s4) % MOD;
        
        uint32_t c2 = query_cnt(2, x - 1);
        uint64_t s2 = query_sum(2, x - 1);
        uint64_t s3_new = (s2 + (__int128)c2 * x) % MOD;
        
        uint32_t c1 = query_cnt(1, x - 1);
        uint64_t s1 = query_sum(1, x - 1);
        uint64_t s2_new = (s1 + (__int128)c1 * x) % MOD;
        
        add_cnt(1, x, 1);
        add_sum(1, x, x % MOD);
        
        if (c1 > 0) {
            add_cnt(2, x, c1);
            add_sum(2, x, s2_new);
        }
        
        if (c2 > 0) {
            add_cnt(3, x, c2);
            add_sum(3, x, s3_new);
        }
        
        cur_a = (cur_a * 153) % mod_a;
    }
    return (int64_t)total_s4;
}
