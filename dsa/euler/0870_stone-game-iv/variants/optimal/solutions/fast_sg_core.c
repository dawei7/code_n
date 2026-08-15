#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

typedef struct {
    int64_t num;
    int64_t den;
} Frac;

static inline int frac_cmp(Frac a, Frac b) {
    __int128 left = (__int128)a.num * b.den;
    __int128 right = (__int128)b.num * a.den;
    if (left < right) return -1;
    if (left > right) return 1;
    return 0;
}

static inline int64_t gcd(int64_t a, int64_t b) {
    while (b) {
        int64_t t = a % b;
        a = b;
        b = t;
    }
    return a;
}

EXPORT double compute_transition_value(int target_idx) {
    Frac cur_r;
    cur_r.num = 1;
    cur_r.den = 1;

    static int64_t a[3000];
    static int j_list[3000];
    int max_len = 2500;

    for (int step = 2; step <= target_idx; step++) {
        a[0] = 0;
        a[1] = 1;
        j_list[0] = 0;
        j_list[1] = 0;
        int len = 2;

        for (int k = 2; k < max_len; k++) {
            __int128 target = (__int128)cur_r.den * a[k - 1];

            // Binary search for smallest j in [1, k-1] such that cur_r.num * a[j] >= target
            int low = 1, high = k - 1, best_j = -1;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if ((__int128)cur_r.num * a[mid] >= target) {
                    best_j = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }

            if (best_j == -1) break;

            a[k] = a[k - 1] + a[best_j];
            j_list[k] = best_j;
            len = k + 1;
        }

        Frac min_next;
        min_next.num = -1;
        min_next.den = 1;

        for (int k = 2; k < len; k++) {
            int j = j_list[k];
            int cand_j = (j > 1) ? (j - 1) : 1;

            Frac cand;
            cand.num = a[k - 1];
            cand.den = a[cand_j];

            if (frac_cmp(cand, cur_r) > 0) {
                if (min_next.num == -1 || frac_cmp(cand, min_next) < 0) {
                    min_next = cand;
                }
            }
        }

        if (min_next.num == -1) break;

        int64_t g = gcd(min_next.num, min_next.den);
        min_next.num /= g;
        min_next.den /= g;

        cur_r = min_next;
    }

    double result = (double)cur_r.num / (double)cur_r.den;
    return result;
}
