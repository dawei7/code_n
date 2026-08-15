#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

#define MOD 1000000007LL

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static inline int64_t power_mod(int64_t base, int64_t exp) {
    int64_t res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

static inline int64_t mod_inv(int64_t n) {
    return power_mod(n, MOD - 2);
}

typedef struct {
    uint64_t bits[13]; // 800 bits = 13 x 64-bit words
} Bitmask800;

static inline void mask_set_bit(Bitmask800* m, int bit) {
    m->bits[bit >> 6] |= (1ULL << (bit & 63));
}

static inline void mask_or(Bitmask800* dest, const Bitmask800* a, const Bitmask800* b) {
    for (int i = 0; i < 13; i++) {
        dest->bits[i] = a->bits[i] | b->bits[i];
    }
}

static inline int mask_popcount(const Bitmask800* m) {
    int count = 0;
    for (int i = 0; i < 13; i++) {
        count += __builtin_popcountll(m->bits[i]);
    }
    return count;
}

typedef struct {
    int64_t weight;
    Bitmask800 mask;
} Choice;

static Choice small_choices[9][15];
static int num_choices[9];

static int64_t large_w[30][100];
static int large_count[30];

static int64_t pow2[850];
static int64_t inv2[850];
static int64_t ans_sum = 0;

static int primes[200];
static int num_primes = 0;

static void dfs_small(int idx, int64_t cur_w, const Bitmask800* cur_mask, int N) {
    if (idx == 9) {
        int covered = mask_popcount(cur_mask);
        int64_t large_factor = 1;

        // Extract the 27-bit prefix from cur_mask->bits[0] (positions 1..27)
        uint64_t prefix = cur_mask->bits[0];

        for (int lim = 1; lim <= 27; lim++) {
            if (large_count[lim] == 0) continue;
            // Count 0-bits in prefix at positions 1..lim
            uint64_t sub = (prefix >> 1) & ((1ULL << lim) - 1);
            int uncovered = lim - __builtin_popcountll(sub);
            int64_t inv_val = inv2[uncovered];

            for (int i = 0; i < large_count[lim]; i++) {
                int64_t term = (1 + large_w[lim][i] * inv_val) % MOD;
                large_factor = (large_factor * term) % MOD;
            }
        }

        int64_t total_term = (cur_w * pow2[N - covered]) % MOD;
        total_term = (total_term * large_factor) % MOD;
        ans_sum = (ans_sum + total_term) % MOD;
        return;
    }

    for (int i = 0; i < num_choices[idx]; i++) {
        Bitmask800 next_mask;
        mask_or(&next_mask, cur_mask, &small_choices[idx][i].mask);
        dfs_small(idx + 1, (cur_w * small_choices[idx][i].weight) % MOD, &next_mask, N);
    }
}

EXPORT int64_t compute_lcm_sum(int N) {
    // 1. Sieve primes up to N
    num_primes = 0;
    char is_p[850];
    memset(is_p, 1, sizeof(is_p));
    for (int p = 2; p * p <= N; p++) {
        if (is_p[p]) {
            for (int i = p * p; i <= N; i += p) is_p[i] = 0;
        }
    }
    for (int p = 2; p <= N; p++) {
        if (is_p[p]) primes[num_primes++] = p;
    }

    int64_t P_N = 1;
    for (int i = 0; i < num_primes; i++) {
        int p = primes[i];
        int kp = (int)(log(N) / log(p) + 1e-9);
        P_N = (P_N * power_mod(p, kp)) % MOD;
    }

    for (int i = 0; i <= N + 5; i++) {
        pow2[i] = power_mod(2, i);
        inv2[i] = mod_inv(pow2[i]);
    }

    // 2. Small primes (first 9 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23)
    for (int s = 0; s < 9; s++) {
        int p = primes[s];
        int kp = (int)(log(N) / log(p) + 1e-9);
        num_choices[s] = kp + 1;

        // j = 0
        small_choices[s][0].weight = 1;
        memset(&small_choices[s][0].mask, 0, sizeof(Bitmask800));

        int pk = 1;
        for (int step = 0; step < kp; step++) pk *= p;

        int p_pow = p;
        int p_prev = 1;
        for (int j = 1; j <= kp; j++) {
            int phi_val = p_pow - p_prev;
            int64_t w = ((-(int64_t)phi_val % MOD + MOD) % MOD * mod_inv(pk)) % MOD;
            small_choices[s][j].weight = w;

            memset(&small_choices[s][j].mask, 0, sizeof(Bitmask800));
            for (int m = p_pow; m <= N; m += p_pow) {
                mask_set_bit(&small_choices[s][j].mask, m);
            }
            p_prev = p_pow;
            p_pow *= p;
        }
    }

    // 3. Large primes (p > 28)
    memset(large_count, 0, sizeof(large_count));
    for (int i = 9; i < num_primes; i++) {
        int p = primes[i];
        int lim = N / p;
        int64_t w_p = ((-(int64_t)(p - 1) % MOD + MOD) % MOD * mod_inv(p)) % MOD;
        large_w[lim][large_count[lim]++] = w_p;
    }

    ans_sum = 0;
    Bitmask800 init_mask;
    memset(&init_mask, 0, sizeof(Bitmask800));
    dfs_small(0, 1, &init_mask, N);

    int64_t ans = (P_N * ans_sum) % MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
