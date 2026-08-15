"""Project Euler Problem 680: Yarra Gnisrever.

Find R(10^18, 10^6) mod 10^9, where R(N, K) = sum_{i=0}^{N-1} i * A[i] after K successive
Fibonacci-indexed subarray reversals.
"""

import ctypes
import os
import subprocess

_MOD = 1_000_000_000


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p680_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p680_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>

#define MOD 1000000000LL

typedef struct Node {
    int64_t seg_len;
    int64_t seg_start;
    int64_t seg_dir;
    int64_t tot_len;
    int64_t sum_val;
    int64_t sum_pos;
    uint32_t prio;
    uint8_t rev;
    int lch, rch;
} Node;

#define MAX_NODES 5000000
static Node tree[MAX_NODES];
static int node_cnt = 0;

static uint32_t rng_state = 2463534242U;
static inline uint32_t xorshift32() {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 17;
    rng_state ^= rng_state << 5;
    return rng_state;
}

static inline int64_t tri_mod(int64_t L) {
    int64_t a = L, b = L - 1;
    if ((a & 1) == 0) a /= 2;
    else b /= 2;
    return (a % MOD) * (b % MOD) % MOD;
}

static inline int64_t sqsum_mod(int64_t L) {
    int64_t a = L - 1, b = L, c = 2 * L - 1;
    if ((a & 1) == 0) a /= 2;
    else b /= 2;
    if (a % 3 == 0) a /= 3;
    else if (b % 3 == 0) b /= 3;
    else c /= 3;
    int64_t ab = (a % MOD) * (b % MOD) % MOD;
    return ab * (c % MOD) % MOD;
}

static inline void seg_sums(int64_t L, int64_t start, int64_t dir, int64_t* out_s, int64_t* out_k) {
    int64_t st = (start % MOD + MOD) % MOD;
    int64_t Lm = L % MOD;
    int64_t tr = tri_mod(L);
    int64_t sq = sqsum_mod(L);
    if (dir == 1) {
        *out_s = (st * Lm + tr) % MOD;
        *out_k = (st * tr + sq) % MOD;
    } else {
        *out_s = (st * Lm - tr % MOD + MOD) % MOD;
        *out_k = (st * tr - sq % MOD + MOD) % MOD;
    }
}

static int new_node(int64_t L, int64_t start, int64_t dir) {
    int u = ++node_cnt;
    tree[u].seg_len = L;
    tree[u].seg_start = start;
    tree[u].seg_dir = dir;
    tree[u].tot_len = L;
    tree[u].prio = xorshift32();
    tree[u].rev = 0;
    tree[u].lch = 0;
    tree[u].rch = 0;
    int64_t s, k;
    seg_sums(L, start, dir, &s, &k);
    tree[u].sum_val = s;
    tree[u].sum_pos = k;
    return u;
}

static inline void apply_rev(int u) {
    if (!u) return;
    int tmp = tree[u].lch;
    tree[u].lch = tree[u].rch;
    tree[u].rch = tmp;
    tree[u].rev ^= 1;
    int64_t L = tree[u].seg_len;
    int64_t d = tree[u].seg_dir;
    if (L > 1) {
        tree[u].seg_start = tree[u].seg_start + d * (L - 1);
    }
    tree[u].seg_dir = -d;
    int64_t s, k;
    seg_sums(L, tree[u].seg_start, tree[u].seg_dir, &s, &k);
    int64_t tot = tree[u].tot_len;
    int64_t new_sum_pos = (tot - 1) % MOD * tree[u].sum_val % MOD - tree[u].sum_pos % MOD + MOD;
    tree[u].sum_pos = new_sum_pos % MOD;
}

static inline void push(int u) {
    if (u && tree[u].rev) {
        apply_rev(tree[u].lch);
        apply_rev(tree[u].rch);
        tree[u].rev = 0;
    }
}

static inline void pull(int u) {
    if (!u) return;
    int l = tree[u].lch;
    int r = tree[u].rch;
    int64_t L = tree[u].seg_len;
    int64_t s, k;
    seg_sums(L, tree[u].seg_start, tree[u].seg_dir, &s, &k);
    
    int64_t len_l = l ? tree[l].tot_len : 0;
    int64_t len_r = r ? tree[r].tot_len : 0;
    tree[u].tot_len = len_l + L + len_r;
    
    int64_t sv = s;
    int64_t sp = (k + (len_l % MOD) * s) % MOD;
    
    if (l) {
        sv = (sv + tree[l].sum_val) % MOD;
        sp = (sp + tree[l].sum_pos) % MOD;
    }
    if (r) {
        sv = (sv + tree[r].sum_val) % MOD;
        int64_t off = (len_l + L) % MOD;
        sp = (sp + tree[r].sum_pos + off * tree[r].sum_val) % MOD;
    }
    tree[u].sum_val = sv;
    tree[u].sum_pos = sp;
}

static void split(int u, int64_t k, int* out_l, int* out_r) {
    if (!u) {
        *out_l = 0;
        *out_r = 0;
        return;
    }
    push(u);
    int64_t len_l = tree[u].lch ? tree[tree[u].lch].tot_len : 0;
    if (k <= len_l) {
        int r_sub;
        split(tree[u].lch, k, out_l, &r_sub);
        tree[u].lch = r_sub;
        pull(u);
        *out_r = u;
    } else if (k >= len_l + tree[u].seg_len) {
        int l_sub;
        split(tree[u].rch, k - len_l - tree[u].seg_len, &l_sub, out_r);
        tree[u].rch = l_sub;
        pull(u);
        *out_l = u;
    } else {
        int64_t cut = k - len_l;
        int64_t L = tree[u].seg_len;
        int64_t st = tree[u].seg_start;
        int64_t d = tree[u].seg_dir;
        
        int left_node = new_node(cut, st, d);
        int right_node = new_node(L - cut, st + d * cut, d);
        
        int orig_l = tree[u].lch;
        int orig_r = tree[u].rch;
        
        tree[left_node].lch = orig_l;
        pull(left_node);
        *out_l = left_node;
        
        tree[right_node].rch = orig_r;
        pull(right_node);
        *out_r = right_node;
    }
}

static int merge(int l, int r) {
    if (!l || !r) return l ? l : r;
    if (tree[l].prio > tree[r].prio) {
        push(l);
        tree[l].rch = merge(tree[l].rch, r);
        pull(l);
        return l;
    } else {
        push(r);
        tree[r].lch = merge(l, tree[r].lch);
        pull(r);
        return r;
    }
}

int64_t solve_c(int64_t N, int64_t K) {
    node_cnt = 0;
    rng_state = 2463534242U;
    
    int root = new_node(N, 0, 1);
    
    int64_t f_prev = 1;
    int64_t f_curr = 1;
    
    for (int64_t step = 1; step <= K; ++step) {
        int64_t s = f_prev % N;
        int64_t t = f_curr % N;
        
        int64_t f_next1 = (f_prev + f_curr) % N;
        int64_t f_next2 = (f_curr + f_next1) % N;
        f_prev = f_next1;
        f_curr = f_next2;
        
        int64_t L_idx = (s < t) ? s : t;
        int64_t R_idx = (s < t) ? t : s;
        
        int A, B, C, BC;
        split(root, L_idx, &A, &BC);
        split(BC, R_idx - L_idx + 1, &B, &C);
        
        apply_rev(B);
        
        root = merge(merge(A, B), C);
    }
    
    return tree[root].sum_pos % MOD;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            [
                "gcc",
                "-O3",
                "-shared",
                "-static",
                "-static-libgcc",
                "-o",
                dll_path,
                c_path,
            ],
            check=True,
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_c.restype = ctypes.c_int64
    lib.solve_c.argtypes = [ctypes.c_int64, ctypes.c_int64]
    return lib


def solve(
    n: int = 1_000_000_000_000_000_000,
    k: int = 1_000_000,
) -> int:
    """Compute R(N, K) modulo 10^9 using dynamic interval-splitting Treap with lazy reversals."""
    if n <= 1000 and k <= 1000:
        arr = list(range(n))
        f_prev = 1
        f_curr = 1
        for _ in range(k):
            s = f_prev % n
            t = f_curr % n
            f_next1 = f_prev + f_curr
            f_next2 = f_curr + f_next1
            f_prev, f_curr = f_next1, f_next2

            l_idx = min(s, t)
            r_idx = max(s, t)
            arr[l_idx : r_idx + 1] = arr[l_idx : r_idx + 1][::-1]

        total = sum(i * val for i, val in enumerate(arr)) % _MOD
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n, k))
    return ans


if __name__ == "__main__":
    print(solve())
