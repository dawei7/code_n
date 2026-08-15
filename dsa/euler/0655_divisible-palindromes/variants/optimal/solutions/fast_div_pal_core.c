
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static int64_t pow_mod(int64_t base, int64_t exp, int64_t mod) {
    int64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return res;
}

static int64_t modinv(int64_t a, int64_t m) {
    return pow_mod(a, m - 2, m);
}

void extend_all(int64_t* dp, int64_t* tmp, int64_t c, int64_t m, int64_t inv10) {
    int64_t src = 0;
    for (int64_t j = 0; j < m; ++j) {
        tmp[j] = dp[src];
        src += inv10;
        if (src >= m) src -= m;
    }
    
    if (c == 0) {
        for (int64_t i = 0; i < m; ++i) dp[i] = tmp[i] * 10;
        return;
    }
    
    int64_t idx = (-10 * c) % m;
    if (idx < 0) idx += m;
    
    int64_t window[10];
    int64_t s = 0;
    for (int t = 0; t < 10; ++t) {
        int64_t v = tmp[idx];
        window[t] = v;
        s += v;
        idx += c;
        if (idx >= m) idx -= m;
    }
    
    idx = 0;
    int pos = 0;
    for (int64_t step = 0; step < m; ++step) {
        int64_t v = tmp[idx];
        int64_t old = window[pos];
        s += v - old;
        window[pos] = v;
        pos++;
        if (pos == 10) pos = 0;
        dp[idx] = s;
        idx += c;
        if (idx >= m) idx -= m;
    }
}

int64_t solve_c(int max_len, int64_t m) {
    int64_t inv10 = modinv(10, m);
    int64_t* pow10 = (int64_t*)malloc((max_len + 1) * sizeof(int64_t));
    pow10[0] = 1;
    for (int i = 1; i <= max_len; ++i) pow10[i] = (pow10[i - 1] * 10) % m;
    
    int64_t* dp = (int64_t*)malloc(m * sizeof(int64_t));
    int64_t* tmp = (int64_t*)malloc(m * sizeof(int64_t));
    
    int64_t total = 0;
    for (int d = 1; d < 10; ++d) {
        if (d % m == 0) total++;
    }
    
    // Even lengths
    memset(dp, 0, m * sizeof(int64_t));
    dp[0] = 1;
    int cur_len = 0;
    while (cur_len + 2 <= max_len) {
        int new_len = cur_len + 2;
        int64_t c = (pow10[new_len - 1] + 1) % m;
        int64_t prev_zero = dp[0];
        extend_all(dp, tmp, c, m, inv10);
        total += dp[0] - prev_zero;
        cur_len = new_len;
    }
    
    // Odd lengths
    memset(dp, 0, m * sizeof(int64_t));
    for (int d = 0; d < 10; ++d) dp[d % m]++;
    cur_len = 1;
    while (cur_len + 2 <= max_len) {
        int new_len = cur_len + 2;
        int64_t c = (pow10[new_len - 1] + 1) % m;
        int64_t prev_zero = dp[0];
        extend_all(dp, tmp, c, m, inv10);
        total += dp[0] - prev_zero;
        cur_len = new_len;
    }
    
    free(pow10);
    free(dp);
    free(tmp);
    return total;
}
