
#include <stdint.h>
#define MOD 1008691207LL

int64_t solve_c(int64_t n) {
    int64_t fact = 1;
    int64_t sum_fact = 1;
    for (int64_t k = 1; k < n; ++k) {
        fact = (fact * k) % MOD;
        sum_fact += fact;
        if (sum_fact >= MOD) sum_fact -= MOD;
    }
    int64_t ans = ((n - 3) % MOD * sum_fact + 2) % MOD;
    if (ans < 0) ans += MOD;
    return ans;
}
