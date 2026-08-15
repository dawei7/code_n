#include <stdint.h>
#include <stdlib.h>

static int64_t power(int64_t base, int64_t exp, int64_t mod) {
    int64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}

static int64_t modInverse(int64_t n, int64_t m) {
    return power(n, m - 2, m);
}

int64_t compute_amidakuji(int64_t m, int64_t n, int64_t mod) {
    if ((m + n) % 2 != 0) return 0;
    int64_t A0 = (m - 1) / 2;
    int64_t C0 = (n - 1) / 2;
    int64_t max_den = 2 * A0 + 4;

    int32_t* inv = (int32_t*)malloc(max_den * sizeof(int32_t));
    if (!inv) return -1;
    inv[1] = 1;
    for (int64_t i = 2; i < max_den; i++) {
        inv[i] = (int32_t)((int64_t)(mod - mod / i) * inv[mod % i] % mod);
    }

    int64_t u0 = (A0 + C0 + 1) % mod;
    int64_t num = 1, den = 1;
    for (int64_t i = 1; i <= A0; i++) {
        num = (__int128)num * ((C0 + i) % mod) % mod;
        den = (__int128)den * inv[i] % mod;
    }
    u0 = (__int128)u0 * num % mod * den % mod;
    u0 = (mod - u0) % mod;

    int64_t tri_sum = 0;
    int64_t uk = u0;

    for (int64_t k = 0; k <= A0; k++) {
        tri_sum = (tri_sum + uk) % mod;
        if (k < A0) {
            int64_t factor = (__int128)((A0 - k) % mod) * ((C0 - k) % mod) % mod;
            factor = (__int128)factor * inv[2 * k + 2] % mod;
            factor = (__int128)factor * inv[2 * k + 3] % mod;
            uk = (__int128)uk * factor % mod;
        }
    }
    free(inv);

    int64_t num_comb = 1, den_comb = 1;
    for (int64_t i = 1; i <= m; i++) {
        num_comb = (__int128)num_comb * ((n + i) % mod) % mod;
        den_comb = (__int128)den_comb * i % mod;
    }
    int64_t comb = (__int128)num_comb * modInverse(den_comb, mod) % mod;

    int64_t total = (comb + 2 * tri_sum) % mod;
    total = (__int128)total * modInverse(3, mod) % mod;
    return total;
}
