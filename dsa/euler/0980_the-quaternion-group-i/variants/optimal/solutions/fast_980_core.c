#include <stdio.h>
#include <stdint.h>

static const int mult_table[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1}
};

static inline int q_mul(int a, int b) {
    int sign = 1;
    if (a < 0) { sign = -sign; a = -a; }
    if (b < 0) { sign = -sign; b = -b; }
    return sign * mult_table[a][b];
}

long long compute_F(int N) {
    long long a = 88888888;
    long long MOD = 888888883;
    long long freq[9] = {0};
    
    int mapping[3] = {2, 3, 4}; // 0->i(2), 1->j(3), 2->k(4)
    
    for (int i = 0; i < N; ++i) {
        int cur = 1;
        for (int step = 0; step < 50; ++step) {
            int b = a % 3;
            cur = q_mul(cur, mapping[b]);
            a = (8888 * a) % MOD;
        }
        freq[cur + 4]++;
    }
    
    long long total_pairs = 0;
    for (int v1 = -4; v1 <= 4; ++v1) {
        if (v1 == 0) continue;
        for (int v2 = -4; v2 <= 4; ++v2) {
            if (v2 == 0) continue;
            if (q_mul(v1, v2) == 1) {
                total_pairs += freq[v1 + 4] * freq[v2 + 4];
            }
        }
    }
    return total_pairs;
}
