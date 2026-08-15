
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

static int primes[700000];
static int num_primes = 0;
static uint8_t is_comp[10000005 / 8 + 1];

static inline int get_comp(int i) {
    return (is_comp[i >> 3] >> (i & 7)) & 1;
}

static inline void set_comp(int i) {
    is_comp[i >> 3] |= (1 << (i & 7));
}

static inline int64_t isqrt_i64(int64_t n) {
    if (n <= 0) return 0;
    int64_t r = (int64_t)sqrt((double)n);
    while ((r + 1) * (r + 1) <= n) r++;
    while (r * r > n) r--;
    return r;
}

static inline int64_t D_func(int64_t x) {
    if (x <= 0) return 0;
    int64_t s = isqrt_i64(x);
    int64_t total = 0;
    for (int64_t a = 1; a <= s; ++a) {
        total += x / a;
    }
    return 2 * total - s * s;
}

static int64_t N_target;
static int64_t total_ans;

static void dfs(int p_idx, int64_t cur_val, int64_t cur_h) {
    int64_t rem = N_target / cur_val;
    total_ans += cur_h * D_func(rem);
    
    for (int i = p_idx; i < num_primes; ++i) {
        int64_t p = primes[i];
        int64_t p2 = p * p;
        if (p2 > rem) break;
        
        int64_t pe = p2;
        int64_t h_e = 1;
        
        while (pe <= rem) {
            dfs(i + 1, cur_val * pe, cur_h * h_e);
            if (pe > rem / p) break;
            pe *= p;
            h_e <<= 1;
        }
    }
}

int64_t solve_c(int64_t N) {
    N_target = N;
    total_ans = 0;
    
    int limit = (int)isqrt_i64(N);
    for (int i = 0; i <= limit / 8 + 1; ++i) is_comp[i] = 0;
    num_primes = 0;
    for (int p = 2; p * p <= limit; ++p) {
        if (!get_comp(p)) {
            for (int j = p * p; j <= limit; j += p) {
                set_comp(j);
            }
        }
    }
    for (int p = 2; p <= limit; ++p) {
        if (!get_comp(p)) {
            primes[num_primes++] = p;
        }
    }
    
    dfs(0, 1, 1);
    return total_ans;
}
