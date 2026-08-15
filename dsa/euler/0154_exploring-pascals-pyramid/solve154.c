#include <stdint.h>

__declspec(dllexport) int64_t solve_c(int N) {
    static uint8_t f2[200001];
    static uint8_t f5[200001];
    f2[0] = 0;
    f5[0] = 0;
    for (int i = 1; i <= N; i++) {
        f2[i] = (i & 1) + f2[i >> 1];
        f5[i] = (i % 5) + f5[i / 5];
    }
    int64_t total = 0;

    for (int i = 0; i <= N / 3; i++) {
        int rem5_i = 56 - f5[i];
        if (rem5_i > 58) continue;
        int rem2_i = 18 - f2[i];
        int rem_n = N - i;
        int j_max = rem_n / 2;
        for (int j = i; j <= j_max; j++) {
            int k = rem_n - j;
            if (f5[j] + f5[k] >= rem5_i) {
                if (f2[j] + f2[k] >= rem2_i) {
                    if (i == j && j == k) {
                        total += 1;
                    } else if (i == j || j == k || i == k) {
                        total += 3;
                    } else {
                        total += 6;
                    }
                }
            }
        }
    }
    return total;
}
