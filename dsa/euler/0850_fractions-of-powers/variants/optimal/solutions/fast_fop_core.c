#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static int primes[500000];
static int num_primes = 0;
static char is_p[6000005];

static void sieve(int limit) {
    memset(is_p, 1, sizeof(char) * (limit + 1));
    is_p[0] = is_p[1] = 0;
    for (int p = 2; p * p <= limit; p++) {
        if (is_p[p]) {
            for (int i = p * p; i <= limit; i += p) is_p[i] = 0;
        }
    }
    num_primes = 0;
    for (int p = 2; p <= limit; p++) {
        if (is_p[p]) primes[num_primes++] = p;
    }
}

static inline int64_t ipow(int64_t base, int exp) {
    int64_t res = 1;
    while (exp > 0) {
        if (exp & 1) res *= base;
        base *= base;
        exp >>= 1;
    }
    return res;
}

static int64_t G_infty = 0;
static int64_t target_N = 0;

static void dfs_powerful(int idx, int64_t cur_d, int64_t cur_h) {
    G_infty += cur_h * (target_N / cur_d);

    for (int i = idx; i < num_primes; i++) {
        int64_t p = primes[i];
        int64_t p2 = p * p;
        if (cur_d > target_N / p2) break;

        int64_t pe = p2;
        int64_t p_pow_em2 = 1;
        while (cur_d <= target_N / pe) {
            int64_t h_pe = p_pow_em2 * (p - 1);
            dfs_powerful(i + 1, cur_d * pe, cur_h * h_pe);
            if (pe > target_N / p) break;
            pe *= p;
            p_pow_em2 *= p;
        }
    }
}

static int64_t k_diff_total = 0;
static int current_k = 0;

static void dfs_k_diff(int idx, int64_t cur_d, int64_t cur_h_inf, int64_t cur_h_k) {
    if (cur_h_inf != cur_h_k) {
        k_diff_total += (cur_h_inf - cur_h_k) * (target_N / cur_d);
    }

    for (int i = idx; i < num_primes; i++) {
        int64_t p = primes[i];
        int64_t p2 = p * p;
        if (cur_d > target_N / p2) break;

        int64_t pe = p2;
        int e = 2;
        while (cur_d <= target_N / pe) {
            int64_t h_inf_e = ipow(p, e - 2) * (p - 1);
            int exp_curr = e - (e + current_k - 1) / current_k;
            int exp_prev = (e - 1) - (e - 1 + current_k - 1) / current_k;
            int64_t g_curr = ipow(p, exp_curr);
            int64_t g_prev = ipow(p, exp_prev);
            int64_t h_k_e = g_curr - g_prev;

            dfs_k_diff(i + 1, cur_d * pe, cur_h_inf * h_inf_e, cur_h_k * h_k_e);
            if (pe > target_N / p) break;
            pe *= p;
            e++;
        }
    }
}

EXPORT void compute_sums(int64_t N, int64_t* out_g_infty, int64_t* out_diff_sum) {
    target_N = N;
    int limit = (int)sqrt(N) + 1;
    sieve(limit);

    G_infty = 0;
    dfs_powerful(0, 1, 1);
    *out_g_infty = G_infty;

    int64_t diff_sum = 0;
    for (int k = 3; k <= 45; k += 2) {
        current_k = k;
        k_diff_total = 0;
        dfs_k_diff(0, 1, 1, 1);
        diff_sum += k_diff_total;
    }
    *out_diff_sum = diff_sum;
}
