#define __USE_MINGW_ANSI_STDIO 1
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <omp.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#define MOD 1000000007LL

static inline int64_t gcd(int64_t a, int64_t b) {
    while (b) {
        int64_t t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static inline int64_t lcm(int64_t a, int64_t b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

EXPORT int64_t compute_P(int m) {
    int n = m * (m + 1) / 2;

    int* sigma = (int*)malloc((n + 1) * sizeof(int));
    for (int k = 1; k <= m; k++) {
        int start = k * (k - 1) / 2 + 1;
        int end = k * (k + 1) / 2;
        for (int i = start; i < end; i++) {
            sigma[i] = i + 1;
        }
        sigma[end] = start;
    }

    int* tau = (int*)malloc((n + 1) * sizeof(int));
    int* tau_inv = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 1; i <= n; i++) {
        int64_t val = ((1000000007LL * i) % n) + 1;
        tau[i] = (int)val;
        tau_inv[(int)val] = i;
    }

    int* pi = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 1; i <= n; i++) {
        pi[i] = tau_inv[sigma[tau[i]]];
    }

    uint8_t* visited = (uint8_t*)calloc(n + 1, sizeof(uint8_t));
    int* cycle_len = (int*)malloc((m + 2) * sizeof(int));
    int** cycle_nodes = (int**)malloc((m + 2) * sizeof(int*));
    int num_cycles = 0;

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            int curr = i;
            int c_len = 0;
            int temp[500];
            while (!visited[curr]) {
                visited[curr] = 1;
                temp[c_len++] = curr;
                curr = pi[curr];
            }
            int c_idx = num_cycles++;
            cycle_len[c_idx] = c_len;
            cycle_nodes[c_idx] = (int*)malloc(c_len * sizeof(int));
            for (int pos = 0; pos < c_len; pos++) {
                cycle_nodes[c_idx][pos] = temp[pos];
            }
        }
    }

    int64_t fact_m_mod = 1;
    for (int i = 1; i <= m; i++) {
        fact_m_mod = (fact_m_mod * i) % MOD;
    }

    int max_inv = 10005;
    int64_t* inv = (int64_t*)malloc((max_inv + 1) * sizeof(int64_t));
    inv[1] = 1;
    for (int i = 2; i <= max_inv; i++) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    int64_t* fact_n = (int64_t*)malloc((n + 1) * sizeof(int64_t));
    fact_n[0] = 1;
    for (int i = 1; i <= n; i++) {
        fact_n[i] = (fact_n[i - 1] * i) % MOD;
    }

    int64_t total_ans = fact_m_mod;

    #pragma omp parallel for reduction(+:total_ans) schedule(dynamic)
    for (int ca = 0; ca < num_cycles; ca++) {
        int* cyc_a = cycle_nodes[ca];
        int La = cycle_len[ca];

        // 1. Same cycle
        for (int pa = 0; pa < La; pa++) {
            int u = cyc_a[pa];
            int64_t weight_u = fact_n[n - u];
            for (int pb = 0; pb < La; pb++) {
                int v = cyc_a[pb];
                if (v <= u) continue;
                int cnt = 0;
                for (int k = 0; k < La; k++) {
                    if (cyc_a[(pa + k) % La] > cyc_a[(pb + k) % La]) cnt++;
                }
                int64_t reps = (fact_m_mod * inv[La]) % MOD;
                int64_t term = ((weight_u * reps) % MOD * cnt) % MOD;
                total_ans = (total_ans + term) % MOD;
            }
        }

        // 2. Pair with cb > ca
        for (int cb = ca + 1; cb < num_cycles; cb++) {
            int* cyc_b = cycle_nodes[cb];
            int Lb = cycle_len[cb];
            int T = (int)lcm(La, Lb);
            int64_t reps = (fact_m_mod * inv[T]) % MOD;

            for (int pa = 0; pa < La; pa++) {
                int u = cyc_a[pa];
                int64_t weight_u = fact_n[n - u];
                for (int pb = 0; pb < Lb; pb++) {
                    int v = cyc_b[pb];
                    if (v < u) {
                        int64_t weight_v = fact_n[n - v];
                        int cnt = 0;
                        for (int k = 0; k < T; k++) {
                            if (cyc_b[(pb + k) % Lb] > cyc_a[(pa + k) % La]) cnt++;
                        }
                        int64_t term = ((weight_v * reps) % MOD * cnt) % MOD;
                        total_ans = (total_ans + term) % MOD;
                    } else {
                        int cnt = 0;
                        for (int k = 0; k < T; k++) {
                            if (cyc_a[(pa + k) % La] > cyc_b[(pb + k) % Lb]) cnt++;
                        }
                        int64_t term = ((weight_u * reps) % MOD * cnt) % MOD;
                        total_ans = (total_ans + term) % MOD;
                    }
                }
            }
        }
    }

    free(sigma);
    free(tau);
    free(tau_inv);
    free(pi);
    free(visited);
    free(cycle_len);
    for (int c = 0; c < num_cycles; c++) free(cycle_nodes[c]);
    free(cycle_nodes);
    free(inv);
    free(fact_n);

    return total_ans % MOD;
}
