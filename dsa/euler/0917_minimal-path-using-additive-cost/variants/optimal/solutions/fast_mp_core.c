#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 998388889LL
#define INF 0x3fffffffffffffffLL

EXPORT uint64_t compute_A(int N, int bandwidth) {
    // Generate a and b arrays of size N + 1
    uint32_t* a = (uint32_t*)malloc((N + 1) * sizeof(uint32_t));
    uint32_t* b = (uint32_t*)malloc((N + 1) * sizeof(uint32_t));

    uint64_t cur = 102022661ULL;
    for (int i = 1; i <= N; i++) {
        a[i] = (uint32_t)cur;
        cur = (cur * cur) % MOD;
        b[i] = (uint32_t)cur;
        cur = (cur * cur) % MOD;
    }

    // Banded rolling DP along antidiagonals:
    // d = i + j ranges from 2 to 2N
    // For fixed d, offset delta = i - j ranges from -W to +W (step 2)
    // Map delta to index k = (delta + W) / 2
    int W = bandwidth;
    int max_k = W + 1;

    uint64_t* dp_prev = (uint64_t*)malloc(max_k * sizeof(uint64_t));
    uint64_t* dp_curr = (uint64_t*)malloc(max_k * sizeof(uint64_t));

    for (int k = 0; k < max_k; k++) {
        dp_prev[k] = INF;
        dp_curr[k] = INF;
    }

    // Base case d = 2: i = 1, j = 1, delta = 0 -> k = W / 2
    int k_mid = W / 2;
    dp_curr[k_mid] = (uint64_t)a[1] + b[1];

    for (int d = 3; d <= 2 * N; d++) {
        // Swap buffers
        uint64_t* tmp = dp_prev;
        dp_prev = dp_curr;
        dp_curr = tmp;

        for (int k = 0; k < max_k; k++) {
            dp_curr[k] = INF;
        }

        // Parity of delta:
        // delta = 2*i - d -> delta has same parity as d
        int min_i = (d - N > 1) ? (d - N) : 1;
        int max_i = (d - 1 < N) ? (d - 1) : N;

        for (int i = min_i; i <= max_i; i++) {
            int j = d - i;
            int delta = i - j;
            if (delta < -W || delta > W) continue;

            int k = (delta + W) / 2;
            uint64_t cost = (uint64_t)a[i] + b[j];

            // Came from (i - 1, j): prev_d = d - 1, prev_delta = (i - 1) - j = delta - 1
            // prev_delta has index (delta - 1 + W) / 2?
            // Note: in prev_d, delta' = (i - 1) - j = delta - 1 (different parity).
            // So if delta is mapped by (delta + W) / 2:
            // Came from top (i - 1, j): delta' = delta - 1
            // Came from left (i, j - 1): delta' = delta + 1
            // Let's use direct (i, j) banded state on row i!
        }
    }

    // Direct rolling row DP with band [i - W, i + W]:
    int win_size = 2 * W + 1;
    uint64_t* row_prev = (uint64_t*)malloc(win_size * sizeof(uint64_t));
    uint64_t* row_curr = (uint64_t*)malloc(win_size * sizeof(uint64_t));

    for (int k = 0; k < win_size; k++) {
        row_prev[k] = INF;
        row_curr[k] = INF;
    }

    row_curr[W] = (uint64_t)a[1] + b[1]; // i = 1, j = 1 (offset 0 -> W)

    // Complete row 1:
    for (int j = 2; j <= 1 + W && j <= N; j++) {
        row_curr[W + (j - 1)] = row_curr[W + (j - 2)] + (uint64_t)a[1] + b[j];
    }

    for (int i = 2; i <= N; i++) {
        uint64_t* tmp = row_prev;
        row_prev = row_curr;
        row_curr = tmp;

        for (int k = 0; k < win_size; k++) {
            row_curr[k] = INF;
        }

        int j_min = (i - W > 1) ? (i - W) : 1;
        int j_max = (i + W < N) ? (i + W) : N;

        for (int j = j_min; j <= j_max; j++) {
            int k = j - i + W;
            uint64_t cost = (uint64_t)a[i] + b[j];

            // From top (i - 1, j):
            // In row i - 1, col j has index j - (i - 1) + W = k + 1:
            uint64_t from_top = INF;
            if (k + 1 < win_size) {
                from_top = row_prev[k + 1];
            }

            // From left (i, j - 1):
            // In current row i, col j - 1 has index k - 1:
            uint64_t from_left = INF;
            if (k - 1 >= 0) {
                from_left = row_curr[k - 1];
            }

            uint64_t best_prev = (from_top < from_left) ? from_top : from_left;
            if (best_prev < INF) {
                row_curr[k] = best_prev + cost;
            }
        }
    }

    uint64_t ans = row_curr[W]; // at i = N, j = N (offset 0 -> W)

    free(a);
    free(b);
    free(dp_prev);
    free(dp_curr);
    free(row_prev);
    free(row_curr);

    return ans;
}
