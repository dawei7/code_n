#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT int64_t compute_winning_partitions(int N) {
    int* g = (int*)calloc(N + 1, sizeof(int));
    for (int n = 1; n <= N; n++) {
        if (n % 2 == 1) {
            int m = (n - 1) / 2;
            int val = 2 * g[m] + 1;
            g[n] = (val > 0) ? val : 0;
        } else {
            int m = (n - 2) / 2;
            int val = 2 * g[m] - 1;
            g[n] = (val < 0) ? val : 0;
        }
    }

    int MAX_V = N;
    int V_SIZE = 2 * MAX_V + 1;
    int OFFSET = MAX_V;

    int64_t* table = (int64_t*)calloc((size_t)(N + 1) * V_SIZE, sizeof(int64_t));
    #define TABLE(w, v) table[(size_t)(w) * V_SIZE + (v)]

    TABLE(0, OFFSET) = 1;

    for (int x = 1; x <= N; x++) {
        int gx = g[x];
        for (int w = x; w <= N; w++) {
            for (int v = 0; v < V_SIZE; v++) {
                int prev_v = v - gx;
                if (prev_v >= 0 && prev_v < V_SIZE) {
                    TABLE(w, v) += TABLE(w - x, prev_v);
                }
            }
        }
    }

    int64_t ans = 0;
    for (int v = 0; v <= OFFSET; v++) {
        ans += TABLE(N, v);
    }

    free(g);
    free(table);
    return ans;
}
