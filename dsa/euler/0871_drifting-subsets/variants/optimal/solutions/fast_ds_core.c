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

#define MAX_N 100500

static int f_arr[MAX_N];
static int in_deg[MAX_N];
static int is_cyc[MAX_N];
static int cyc_vis[MAX_N];
static int topo[MAX_N];

static int head[MAX_N];
static int next_child[MAX_N];
static int child_val[MAX_N];
static int edge_cnt = 0;

static int dp0[MAX_N];
static int dp1[MAX_N];
static int dp2[MAX_N];

static inline void add_edge(int u, int v) {
    child_val[edge_cnt] = v;
    next_child[edge_cnt] = head[u];
    head[u] = edge_cnt++;
}

static int compute_D(int n) {
    edge_cnt = 0;
    for (int x = 0; x < n; x++) {
        head[x] = -1;
        in_deg[x] = 0;
        is_cyc[x] = 1;
        cyc_vis[x] = 0;
        dp0[x] = 0;
        dp1[x] = 1;
        dp2[x] = 0;

        int64_t x64 = x;
        f_arr[x] = (int)((x64 * x64 % n * x64 + x64 + 1) % n);
    }

    for (int x = 0; x < n; x++) {
        int fx = f_arr[x];
        in_deg[fx]++;
        add_edge(fx, x);
    }

    int q_head = 0, q_tail = 0;
    for (int x = 0; x < n; x++) {
        if (in_deg[x] == 0) {
            topo[q_tail++] = x;
        }
    }

    while (q_head < q_tail) {
        int u = topo[q_head++];
        is_cyc[u] = 0;
        int p = f_arr[u];
        in_deg[p]--;
        if (in_deg[p] == 0) {
            topo[q_tail++] = p;
        }
    }

    for (int idx = 0; idx < q_tail; idx++) {
        int u = topo[idx];
        int s0 = 0;
        int best_diff = -1000000000;
        int has_child = 0;

        for (int e = head[u]; e != -1; e = next_child[e]) {
            int v = child_val[e];
            has_child = 1;
            int opt_not = (dp0[v] > dp2[v]) ? dp0[v] : dp2[v];
            s0 += opt_not;
            int diff = dp1[v] - opt_not;
            if (diff > best_diff) best_diff = diff;
        }

        dp0[u] = s0;
        dp1[u] = 1 + s0;
        dp2[u] = s0 + (has_child && best_diff > 0 ? best_diff : 0);
    }

    static int cyc[MAX_N];
    static int base_s0[MAX_N];
    static int best_tree_diff[MAX_N];

    int tot_D = 0;

    for (int s = 0; s < n; s++) {
        if (is_cyc[s] && !cyc_vis[s]) {
            int m = 0;
            int curr = s;
            while (!cyc_vis[curr]) {
                cyc_vis[curr] = 1;
                cyc[m++] = curr;
                curr = f_arr[curr];
            }

            for (int i = 0; i < m; i++) {
                int c = cyc[i];
                int s0 = 0;
                int b_diff = -1000000000;
                for (int e = head[c]; e != -1; e = next_child[e]) {
                    int v = child_val[e];
                    if (!is_cyc[v]) {
                        int opt_not = (dp0[v] > dp2[v]) ? dp0[v] : dp2[v];
                        s0 += opt_not;
                        int diff = dp1[v] - opt_not;
                        if (diff > b_diff) b_diff = diff;
                    }
                }
                base_s0[i] = s0;
                best_tree_diff[i] = b_diff;
            }

            int best_cyc = 0;

            for (int start_st = 0; start_st < 3; start_st++) {
                // start_st: 0: NONE, 1: IN, 2: TREE
                int dp_none = -1000000000;
                int dp_in = -1000000000;
                int dp_tree = -1000000000;

                if (start_st == 0) {
                    dp_none = base_s0[0];
                } else if (start_st == 1) {
                    dp_in = base_s0[0] + 1;
                } else if (start_st == 2) {
                    if (best_tree_diff[0] >= 0) {
                        dp_tree = base_s0[0] + best_tree_diff[0];
                    } else {
                        continue;
                    }
                }

                for (int i = 1; i < m; i++) {
                    int next_none = -1000000000;
                    int next_in = -1000000000;
                    int next_tree = -1000000000;

                    // From none
                    if (dp_none >= 0) {
                        int v_none = dp_none + base_s0[i];
                        if (v_none > next_none) next_none = v_none;

                        int v_in = dp_none + base_s0[i] + 1;
                        if (v_in > next_in) next_in = v_in;

                        if (best_tree_diff[i] >= 0) {
                            int v_tree = dp_none + base_s0[i] + best_tree_diff[i];
                            if (v_tree > next_tree) next_tree = v_tree;
                        }
                    }

                    // From tree
                    if (dp_tree >= 0) {
                        int v_none = dp_tree + base_s0[i];
                        if (v_none > next_none) next_none = v_none;

                        int v_in = dp_tree + base_s0[i] + 1;
                        if (v_in > next_in) next_in = v_in;

                        if (best_tree_diff[i] >= 0) {
                            int v_tree = dp_tree + base_s0[i] + best_tree_diff[i];
                            if (v_tree > next_tree) next_tree = v_tree;
                        }
                    }

                    // From in (c_{i-1} in A => c_i must be NONE)
                    if (dp_in >= 0) {
                        int v_none = dp_in + base_s0[i];
                        if (v_none > next_none) next_none = v_none;
                    }

                    dp_none = next_none;
                    dp_in = next_in;
                    dp_tree = next_tree;
                }

                // Close cycle
                if (dp_none > best_cyc) best_cyc = dp_none;
                if (dp_tree > best_cyc) best_cyc = dp_tree;
                if (start_st == 0 && dp_in > best_cyc) best_cyc = dp_in;
            }

            tot_D += best_cyc;
        }
    }

    return tot_D;
}

EXPORT int64_t compute_drifting_sum(int start_n, int count) {
    int64_t sum = 0;
    for (int i = 1; i <= count; i++) {
        sum += compute_D(start_n + i);
    }
    return sum;
}
