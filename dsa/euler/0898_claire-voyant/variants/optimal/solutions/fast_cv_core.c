#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

typedef struct {
    double s;
    double p;
} State;

static int compare_states(const void* a, const void* b) {
    double sa = ((const State*)a)->s;
    double sb = ((const State*)b)->s;
    if (sa < sb) return -1;
    if (sa > sb) return 1;
    return 0;
}

typedef struct {
    double w;
    double p_plus;
    double p_zero;
    double p_minus;
} Pair;

static Pair pairs[25];

static State* list1 = NULL;
static int count1 = 0;

static void gen_first_half(int idx, int end, double curr_s, double curr_p) {
    if (idx == end) {
        list1[count1].s = curr_s;
        list1[count1].p = curr_p;
        count1++;
        return;
    }
    gen_first_half(idx + 1, end, curr_s + 2.0 * pairs[idx].w, curr_p * pairs[idx].p_plus);
    gen_first_half(idx + 1, end, curr_s, curr_p * pairs[idx].p_zero);
    gen_first_half(idx + 1, end, curr_s - 2.0 * pairs[idx].w, curr_p * pairs[idx].p_minus);
}

static double* prefix_p = NULL;
static double total_p_correct = 0.0;

static void gen_second_half(int idx, int end, double curr_s, double curr_p) {
    if (idx == end) {
        // Query list1 for s1 > -curr_s:
        // Binary search for first element in list1 with s > -curr_s
        double target = -curr_s;
        int low = 0, high = count1 - 1;
        int ans = count1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (list1[mid].s > target + 1e-12) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        double prob_strictly_greater = prefix_p[count1] - prefix_p[ans];

        // Check for s1 == -curr_s (equality within 1e-12)
        int eq_low = 0, eq_high = count1 - 1;
        int first_eq = count1;
        while (eq_low <= eq_high) {
            int mid = (eq_low + eq_high) / 2;
            if (list1[mid].s >= target - 1e-12) {
                first_eq = mid;
                eq_high = mid - 1;
            } else {
                eq_low = mid + 1;
            }
        }
        double prob_eq = 0.0;
        if (first_eq < ans) {
            prob_eq = prefix_p[ans] - prefix_p[first_eq];
        }

        total_p_correct += curr_p * (prob_strictly_greater + 0.5 * prob_eq);
        return;
    }
    gen_second_half(idx + 1, end, curr_s + 2.0 * pairs[idx].w, curr_p * pairs[idx].p_plus);
    gen_second_half(idx + 1, end, curr_s, curr_p * pairs[idx].p_zero);
    gen_second_half(idx + 1, end, curr_s - 2.0 * pairs[idx].w, curr_p * pairs[idx].p_minus);
}

EXPORT double compute_probability(void) {
    for (int i = 0; i < 25; i++) {
        double p = (25.0 + i) / 100.0;
        double w = log((1.0 - p) / p);
        pairs[i].w = w;
        pairs[i].p_plus = (1.0 - p) * (1.0 - p);
        pairs[i].p_zero = 2.0 * p * (1.0 - p);
        pairs[i].p_minus = p * p;
    }

    int n1 = 12; // 3^12 = 531,441
    int cap1 = 531441;
    list1 = (State*)malloc(cap1 * sizeof(State));
    count1 = 0;
    gen_first_half(0, n1, 0.0, 1.0);

    qsort(list1, count1, sizeof(State), compare_states);

    prefix_p = (double*)malloc((count1 + 1) * sizeof(double));
    prefix_p[0] = 0.0;
    for (int i = 0; i < count1; i++) {
        prefix_p[i + 1] = prefix_p[i] + list1[i].p;
    }

    total_p_correct = 0.0;
    gen_second_half(n1, 25, 0.0, 1.0);

    free(list1);
    free(prefix_p);
    return total_p_correct;
}
