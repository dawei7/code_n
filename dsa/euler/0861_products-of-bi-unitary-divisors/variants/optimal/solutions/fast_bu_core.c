#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

static int primes[200000];
static int num_primes = 0;
static char is_p[2000005];

static void sieve(int limit) {
    memset(is_p, 1, sizeof(char) * (limit + 1));
    is_p[0] = is_p[1] = 0;
    for (int p = 2; p * p <= limit; p++) {
        if (is_p[p]) {
            for (int i = p * p; i <= limit; i += p) is_p[i] = 0;
        }
    }
    num_primes = 0;
    for (int p = 2; p <= limit; p++) {
        if (is_p[p]) primes[num_primes++] = p;
    }
}

static int64_t* V_val;
static int64_t* S_val;
static int num_V = 0;
static int64_t N_global;
static int K_global;

static void init_pi_table(int64_t N) {
    N_global = N;
    K_global = (int)sqrt(N);
    sieve(K_global + 1000);

    num_V = 2 * K_global;
    V_val = (int64_t*)malloc(((size_t)num_V + 5) * sizeof(int64_t));
    S_val = (int64_t*)malloc(((size_t)num_V + 5) * sizeof(int64_t));

    int idx = 0;
    for (int i = 1; i <= K_global; i++) {
        V_val[idx] = N / i;
        S_val[idx] = V_val[idx] - 1;
        idx++;
    }
    for (int64_t i = V_val[idx - 1] - 1; i >= 1; i--) {
        V_val[idx] = i;
        S_val[idx] = i - 1;
        idx++;
    }
    num_V = idx;

    #define GET_V_INDEX(v) ((v) >= K_global ? (int)(N_global / (v) - 1) : (num_V - (int)(v)))

    for (int p_idx = 0; p_idx < num_primes; p_idx++) {
        int64_t p = primes[p_idx];
        int64_t p2 = p * p;
        if (p2 > N) break;
        int64_t sp = S_val[GET_V_INDEX(p - 1)];

        for (int i = 0; i < num_V; i++) {
            int64_t v = V_val[i];
            if (v < p2) break;
            int64_t v_div_p = v / p;
            int next_idx = GET_V_INDEX(v_div_p);
            S_val[i] -= (S_val[next_idx] - sp);
        }
    }
}

static inline int64_t query_pi(int64_t v) {
    if (v < 2) return 0;
    if (v > N_global) v = N_global;
    int idx = (v >= K_global) ? (int)(N_global / v - 1) : (num_V - (int)v);
    return S_val[idx];
}

static int64_t count_1(int64_t N, int e1) {
    int64_t max_p1 = (int64_t)pow((double)N, 1.0 / e1);
    while (1) {
        __int128 p1_e = 1;
        for (int i = 0; i < e1; i++) p1_e *= (max_p1 + 1);
        if (p1_e <= N) max_p1++;
        else break;
    }
    while (max_p1 >= 1) {
        __int128 p1_e = 1;
        for (int i = 0; i < e1; i++) p1_e *= max_p1;
        if (p1_e > N) max_p1--;
        else break;
    }
    return query_pi(max_p1);
}

static int64_t count_2(int64_t N, int e1, int e2) {
    int64_t ans = 0;
    if (e1 == e2) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem = N;
            for (int k = 0; k < e1; k++) rem /= p1;
            if (rem < p1) break;
            int64_t max_p2 = (int64_t)pow((double)rem, 1.0 / e2);
            while (1) {
                __int128 p2_e = 1;
                for (int k = 0; k < e2; k++) p2_e *= (max_p2 + 1);
                if (p2_e <= rem) max_p2++;
                else break;
            }
            while (max_p2 >= 1) {
                __int128 p2_e = 1;
                for (int k = 0; k < e2; k++) p2_e *= max_p2;
                if (p2_e > rem) max_p2--;
                else break;
            }
            if (max_p2 <= p1) break;
            ans += (query_pi(max_p2) - (i + 1));
        }
    } else {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem = N;
            for (int k = 0; k < e1; k++) rem /= p1;
            if (rem == 0) break;
            int64_t max_p2 = (int64_t)pow((double)rem, 1.0 / e2);
            while (1) {
                __int128 p2_e = 1;
                for (int k = 0; k < e2; k++) p2_e *= (max_p2 + 1);
                if (p2_e <= rem) max_p2++;
                else break;
            }
            while (max_p2 >= 1) {
                __int128 p2_e = 1;
                for (int k = 0; k < e2; k++) p2_e *= max_p2;
                if (p2_e > rem) max_p2--;
                else break;
            }
            int64_t pi_p2 = query_pi(max_p2);
            if (max_p2 >= p1) pi_p2--;
            ans += pi_p2;
        }
    }
    return ans;
}

static int64_t count_3(int64_t N, int e1, int e2, int e3) {
    int64_t ans = 0;
    if (e1 == e2 && e2 == e3) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem1 = N;
            for (int k = 0; k < e1; k++) rem1 /= p1;
            if (rem1 < p1 * p1) break;

            for (int j = i + 1; j < num_primes; j++) {
                int64_t p2 = primes[j];
                int64_t rem2 = rem1;
                for (int k = 0; k < e2; k++) rem2 /= p2;
                if (rem2 <= p2) break;

                int64_t max_p3 = (int64_t)pow((double)rem2, 1.0 / e3);
                while (1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= (max_p3 + 1);
                    if (p3_e <= rem2) max_p3++;
                    else break;
                }
                while (max_p3 >= 1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= max_p3;
                    if (p3_e > rem2) max_p3--;
                    else break;
                }
                if (max_p3 <= p2) break;
                ans += (query_pi(max_p3) - (j + 1));
            }
        }
    } else if (e1 > e2 && e2 == e3) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem1 = N;
            for (int k = 0; k < e1; k++) rem1 /= p1;
            if (rem1 == 0) break;

            for (int j = 0; j < num_primes; j++) {
                if (j == i) continue;
                int64_t p2 = primes[j];
                int64_t rem2 = rem1;
                for (int k = 0; k < e2; k++) rem2 /= p2;
                if (rem2 <= p2) {
                    if (j > i) break;
                    else continue;
                }

                int64_t max_p3 = (int64_t)pow((double)rem2, 1.0 / e3);
                while (1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= (max_p3 + 1);
                    if (p3_e <= rem2) max_p3++;
                    else break;
                }
                while (max_p3 >= 1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= max_p3;
                    if (p3_e > rem2) max_p3--;
                    else break;
                }
                if (max_p3 <= p2) continue;

                int64_t count = query_pi(max_p3) - (j + 1);
                if (p1 > p2 && p1 <= max_p3) count--;
                ans += count;
            }
        }
    } else if (e1 == e2 && e2 > e3) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem1 = N;
            for (int k = 0; k < e1; k++) rem1 /= p1;
            if (rem1 < p1) break;

            for (int j = i + 1; j < num_primes; j++) {
                int64_t p2 = primes[j];
                int64_t rem2 = rem1;
                for (int k = 0; k < e2; k++) rem2 /= p2;
                if (rem2 == 0) break;

                int64_t max_p3 = (int64_t)pow((double)rem2, 1.0 / e3);
                while (1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= (max_p3 + 1);
                    if (p3_e <= rem2) max_p3++;
                    else break;
                }
                while (max_p3 >= 1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= max_p3;
                    if (p3_e > rem2) max_p3--;
                    else break;
                }
                int64_t count = query_pi(max_p3);
                if (max_p3 >= p1) count--;
                if (max_p3 >= p2) count--;
                ans += count;
            }
        }
    } else {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem1 = N;
            for (int k = 0; k < e1; k++) rem1 /= p1;
            if (rem1 == 0) break;

            for (int j = 0; j < num_primes; j++) {
                if (j == i) continue;
                int64_t p2 = primes[j];
                int64_t rem2 = rem1;
                for (int k = 0; k < e2; k++) rem2 /= p2;
                if (rem2 == 0) break;

                int64_t max_p3 = (int64_t)pow((double)rem2, 1.0 / e3);
                while (1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= (max_p3 + 1);
                    if (p3_e <= rem2) max_p3++;
                    else break;
                }
                while (max_p3 >= 1) {
                    __int128 p3_e = 1;
                    for (int k = 0; k < e3; k++) p3_e *= max_p3;
                    if (p3_e > rem2) max_p3--;
                    else break;
                }
                int64_t count = query_pi(max_p3);
                if (max_p3 >= p1) count--;
                if (max_p3 >= p2) count--;
                ans += count;
            }
        }
    }
    return ans;
}

static int64_t count_4(int64_t N, int e1, int e2, int e3, int e4) {
    int64_t ans = 0;
    if (e1 == 1 && e2 == 1 && e3 == 1 && e4 == 1) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            if (p1 * p1 * p1 * p1 > N) break;

            for (int j = i + 1; j < num_primes; j++) {
                int64_t p2 = primes[j];
                if (p1 * p2 * p2 * p2 > N) break;

                for (int k = j + 1; k < num_primes; k++) {
                    int64_t p3 = primes[k];
                    int64_t p123 = p1 * p2 * p3;
                    if (p123 * p3 > N) break;
                    int64_t max_p4 = N / p123;
                    if (max_p4 <= p3) break;
                    ans += (query_pi(max_p4) - (k + 1));
                }
            }
        }
    } else if (e1 == 2 && e2 == 1 && e3 == 1 && e4 == 1) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            int64_t rem1 = N / (p1 * p1);
            if (rem1 < 2 * 3 * 5) break;

            for (int j = 0; j < num_primes; j++) {
                if (j == i) continue;
                int64_t p2 = primes[j];
                if (p2 * p2 * p2 > rem1) {
                    if (j > i) break;
                    else continue;
                }
                int64_t rem2 = rem1 / p2;

                for (int k = j + 1; k < num_primes; k++) {
                    if (k == i) continue;
                    int64_t p3 = primes[k];
                    if (p3 * p3 > rem2) {
                        if (k > i) break;
                        else continue;
                    }
                    int64_t max_p4 = rem2 / p3;
                    if (max_p4 <= p3) continue;

                    int64_t count = query_pi(max_p4) - (k + 1);
                    if (p1 > p3 && p1 <= max_p4) count--;
                    ans += count;
                }
            }
        }
    } else if (e1 == 2 && e2 == 2 && e3 == 1 && e4 == 1) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            if (p1 * p1 * p1 * p1 > N) break;

            for (int j = i + 1; j < num_primes; j++) {
                int64_t p2 = primes[j];
                int64_t p12 = (p1 * p1) * (p2 * p2);
                if (p12 > N) break;
                int64_t rem = N / p12;

                for (int k = 0; k < num_primes; k++) {
                    if (k == i || k == j) continue;
                    int64_t p3 = primes[k];
                    if (p3 * p3 > rem) {
                        if (k > j) break;
                        else continue;
                    }
                    int64_t max_p4 = rem / p3;
                    if (max_p4 <= p3) continue;

                    int64_t count = query_pi(max_p4) - (k + 1);
                    if (p1 > p3 && p1 <= max_p4) count--;
                    if (p2 > p3 && p2 <= max_p4) count--;
                    ans += count;
                }
            }
        }
    } else if (e1 == 2 && e2 == 2 && e3 == 2 && e4 == 1) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            if (p1 * p1 * p1 * p1 * p1 * p1 > N) break;

            for (int j = i + 1; j < num_primes; j++) {
                int64_t p2 = primes[j];
                for (int k = j + 1; k < num_primes; k++) {
                    int64_t p3 = primes[k];
                    __int128 p123 = (__int128)p1 * p1 * p2 * p2 * p3 * p3;
                    if (p123 > N) break;
                    int64_t max_p4 = (int64_t)(N / p123);
                    int64_t count = query_pi(max_p4);
                    if (max_p4 >= p1) count--;
                    if (max_p4 >= p2) count--;
                    if (max_p4 >= p3) count--;
                    ans += count;
                }
            }
        }
    } else if (e1 == 2 && e2 == 2 && e3 == 2 && e4 == 2) {
        for (int i = 0; i < num_primes; i++) {
            int64_t p1 = primes[i];
            for (int j = i + 1; j < num_primes; j++) {
                int64_t p2 = primes[j];
                for (int k = j + 1; k < num_primes; k++) {
                    int64_t p3 = primes[k];
                    __int128 p123 = (__int128)p1 * p1 * p2 * p2 * p3 * p3;
                    if (p123 > N) break;
                    int64_t rem = (int64_t)(N / p123);
                    int64_t max_p4 = (int64_t)sqrt(rem);
                    if (max_p4 <= p3) break;
                    ans += (query_pi(max_p4) - (k + 1));
                }
            }
        }
    }
    return ans;
}

EXPORT int64_t compute_q_sum(int64_t N) {
    init_pi_table(N);

    int shapes[][4] = {
        {1, 1, 0, 0}, {1, 1, 1, 0}, {1, 1, 1, 1},
        {2, 1, 0, 0}, {2, 1, 1, 0}, {2, 1, 1, 1},
        {2, 2, 0, 0}, {2, 2, 1, 0}, {2, 2, 1, 1},
        {2, 2, 2, 0}, {2, 2, 2, 1}, {2, 2, 2, 2},
        {3, 0, 0, 0}, {3, 1, 0, 0}, {3, 1, 1, 0}, {3, 2, 0, 0}, {3, 2, 1, 0}, {3, 2, 2, 0}, {3, 3, 0, 0},
        {4, 0, 0, 0}, {4, 1, 0, 0}, {4, 1, 1, 0}, {4, 2, 0, 0}, {4, 2, 1, 0}, {4, 2, 2, 0}, {4, 3, 0, 0}, {4, 4, 0, 0},
        {5, 0, 0, 0}, {5, 1, 0, 0}, {5, 2, 0, 0},
        {6, 0, 0, 0}, {6, 1, 0, 0}, {6, 2, 0, 0},
        {7, 0, 0, 0}, {7, 1, 0, 0}, {7, 2, 0, 0},
        {8, 0, 0, 0}, {8, 1, 0, 0}, {8, 2, 0, 0},
        {9, 0, 0, 0}, {9, 1, 0, 0}, {9, 2, 0, 0},
        {10, 0, 0, 0}, {10, 1, 0, 0}, {10, 2, 0, 0},
        {11, 0, 0, 0}, {12, 0, 0, 0}, {13, 0, 0, 0}, {14, 0, 0, 0},
        {15, 0, 0, 0}, {16, 0, 0, 0}, {17, 0, 0, 0}, {18, 0, 0, 0}, {19, 0, 0, 0}, {20, 0, 0, 0}
    };
    int num_shapes = sizeof(shapes) / sizeof(shapes[0]);

    int64_t total_ans = 0;
    for (int i = 0; i < num_shapes; i++) {
        int e1 = shapes[i][0];
        int e2 = shapes[i][1];
        int e3 = shapes[i][2];
        int e4 = shapes[i][3];

        int64_t count = 0;
        if (e2 == 0) {
            count = count_1(N, e1);
        } else if (e3 == 0) {
            count = count_2(N, e1, e2);
        } else if (e4 == 0) {
            count = count_3(N, e1, e2, e3);
        } else {
            count = count_4(N, e1, e2, e3, e4);
        }
        total_ans += count;
    }

    free(V_val);
    free(S_val);
    return total_ans;
}
