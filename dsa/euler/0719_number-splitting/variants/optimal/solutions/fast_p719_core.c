
#include <stdint.h>
#include <stdbool.h>

static bool check_split(int64_t num, int64_t target, int parts_count) {
    if (num == target && parts_count > 0) return true;
    if (num < target) return false;
    
    int64_t mod = 10;
    while (mod < num) {
        int64_t head = num / mod;
        int64_t tail = num % mod;
        if (tail <= target) {
            if (check_split(head, target - tail, parts_count + 1)) return true;
        }
        mod *= 10;
    }
    return false;
}

int64_t solve_c(int64_t limit) {
    int64_t total = 0;
    for (int64_t k = 2; k <= limit; ++k) {
        int r = k % 9;
        if (r == 0 || r == 1) {
            int64_t n = k * k;
            if (check_split(n, k, 0)) {
                total += n;
            }
        }
    }
    return total;
}
