
#include <stdint.h>
#include <stdlib.h>

#define MAX_N 25000

static uint32_t row[MAX_N + 1];
static uint32_t new_row[MAX_N + 1];

uint32_t solve_c(int n, uint32_t mod) {
    row[0] = 1;
    for (int i = 1; i <= n; ++i) {
        if (i & 1) {
            new_row[0] = 0;
            for (int j = 1; j <= i; ++j) {
                uint32_t v = new_row[j - 1] + row[j - 1];
                if (v >= mod) v -= mod;
                new_row[j] = v;
            }
        } else {
            new_row[i] = 0;
            for (int j = i - 1; j >= 0; --j) {
                uint32_t v = new_row[j + 1] + row[j];
                if (v >= mod) v -= mod;
                new_row[j] = v;
            }
        }
        for (int j = 0; j <= i; ++j) {
            row[j] = new_row[j];
        }
    }
    return (n & 1) ? row[n] : row[0];
}
