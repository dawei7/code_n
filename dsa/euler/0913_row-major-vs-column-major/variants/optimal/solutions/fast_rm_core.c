#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

// Fast 64-bit integer arithmetic
static inline uint64_t mul_mod(uint64_t a, uint64_t b, uint64_t m) {
    return (uint64_t)((__int128)a * b % m);
}

static inline uint64_t power_mod(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = mul_mod(res, base, mod);
        base = mul_mod(base, base, mod);
        exp >>= 1;
    }
    return res;
}

// Order of a mod d
static uint64_t get_order(uint64_t a, uint64_t d, uint64_t phi_d) {
    if (d == 1) return 1;
    // Order divides phi_d
    // Factor phi_d:
    uint64_t ord = phi_d;
    uint64_t temp = phi_d;
    for (uint64_t p = 2; p * p <= temp; p++) {
        if (temp % p == 0) {
            while (ord % p == 0 && power_mod(a, ord / p, d) == 1) {
                ord /= p;
            }
            while (temp % p == 0) temp /= p;
        }
    }
    if (temp > 1) {
        uint64_t p = temp;
        while (ord % p == 0 && power_mod(a, ord / p, d) == 1) {
            ord /= p;
        }
    }
    return ord;
}

// Divisors and phi
typedef struct {
    uint64_t p;
    int e;
} Factor;

static int factor_int(uint64_t n, Factor* factors) {
    int count = 0;
    for (uint64_t p = 2; p * p <= n; p++) {
        if (n % p == 0) {
            factors[count].p = p;
            factors[count].e = 0;
            while (n % p == 0) {
                factors[count].e++;
                n /= p;
            }
            count++;
        }
    }
    if (n > 1) {
        factors[count].p = n;
        factors[count].e = 1;
        count++;
    }
    return count;
}

static uint64_t current_a;
static uint64_t current_cycles;

static void dfs_divs(int idx, int total_factors, const Factor* factors, uint64_t d, uint64_t phi_d) {
    if (idx == total_factors) {
        uint64_t ord = get_order(current_a, d, phi_d);
        current_cycles += phi_d / ord;
        return;
    }
    uint64_t cur_p = factors[idx].p;
    int max_e = factors[idx].e;
    
    // e = 0
    dfs_divs(idx + 1, total_factors, factors, d, phi_d);
    
    uint64_t p_pow = cur_p;
    uint64_t cur_phi = cur_p - 1;
    for (int e = 1; e <= max_e; e++) {
        dfs_divs(idx + 1, total_factors, factors, d * p_pow, phi_d * cur_phi);
        p_pow *= cur_p;
        cur_phi *= cur_p;
    }
}

EXPORT uint64_t compute_S_total(int max_val) {
    uint64_t total_swaps = 0;
    Factor factors[64];

    for (int n = 2; n <= max_val; n++) {
        for (int m = n; m <= max_val; m++) {
            uint64_t N = (uint64_t)n * n * n * n;
            uint64_t M = (uint64_t)m * m * m * m;
            uint64_t NM = N * M;
            uint64_t NM_minus_1 = NM - 1;

            int num_f = factor_int(NM_minus_1, factors);
            current_a = N % NM_minus_1;
            current_cycles = 1; // for NM - 1

            dfs_divs(0, num_f, factors, 1, 1);

            uint64_t swaps = NM - current_cycles;
            total_swaps += swaps;
        }
    }
    return total_swaps;
}
