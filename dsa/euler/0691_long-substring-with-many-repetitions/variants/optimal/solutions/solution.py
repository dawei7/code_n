"""Project Euler Problem 691: Long Substring with Many Repetitions.

Find the sum of non-zero L(k, S_{5000000}) for k >= 1, where S_n is generated from the Thue-Morse
and Beatty sequences, and L(k, s) is the length of the longest substring appearing at least k times.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_p691_core.dll")
    c_path = os.path.join(tmp_dir, "fast_p691_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

#define MAX_STATES 10000005

typedef struct {
    int nxt0, nxt1;
    int link;
    int maxlen;
    int occ;
} State;

static State sam[MAX_STATES];
static int order[MAX_STATES];
static int cnt_len[5000005];
static int best[5000005];

int64_t solve_c(int n) {
    sam[1].nxt0 = 0;
    sam[1].nxt1 = 0;
    sam[1].link = 0;
    sam[1].maxlen = 0;
    sam[1].occ = 0;
    
    int last = 1;
    int sz = 1;
    
    unsigned __int128 scale = (unsigned __int128)1 << 60;
    unsigned __int128 s5 = (unsigned __int128)5 * scale * scale;
    unsigned __int128 r = 0;
    for (int b = 62; b >= 0; --b) {
        unsigned __int128 cand = r | ((unsigned __int128)1 << b);
        if (cand * cand <= s5) r = cand;
    }
    unsigned __int128 inv_phi = (r - scale) / 2;
    
    unsigned __int128 acc = 0;
    uint64_t prev_floor = 0;
    
    for (int i = 0; i < n; ++i) {
        acc += inv_phi;
        uint64_t cur_floor = (uint64_t)(acc >> 60);
        int b = (int)(cur_floor - prev_floor);
        prev_floor = cur_floor;
        
        int a = __builtin_parity(i);
        int c = a ^ b;
        
        int cur = ++sz;
        sam[cur].nxt0 = 0;
        sam[cur].nxt1 = 0;
        sam[cur].link = 0;
        sam[cur].maxlen = sam[last].maxlen + 1;
        sam[cur].occ = 1;
        
        int p = last;
        if (c == 0) {
            while (p && sam[p].nxt0 == 0) {
                sam[p].nxt0 = cur;
                p = sam[p].link;
            }
            if (p == 0) {
                sam[cur].link = 1;
            } else {
                int q = sam[p].nxt0;
                if (sam[p].maxlen + 1 == sam[q].maxlen) {
                    sam[cur].link = q;
                } else {
                    int clone = ++sz;
                    sam[clone] = sam[q];
                    sam[clone].maxlen = sam[p].maxlen + 1;
                    sam[clone].occ = 0;
                    while (p && sam[p].nxt0 == q) {
                        sam[p].nxt0 = clone;
                        p = sam[p].link;
                    }
                    sam[q].link = clone;
                    sam[cur].link = clone;
                }
            }
        } else {
            while (p && sam[p].nxt1 == 0) {
                sam[p].nxt1 = cur;
                p = sam[p].link;
            }
            if (p == 0) {
                sam[cur].link = 1;
            } else {
                int q = sam[p].nxt1;
                if (sam[p].maxlen + 1 == sam[q].maxlen) {
                    sam[cur].link = q;
                } else {
                    int clone = ++sz;
                    sam[clone] = sam[q];
                    sam[clone].maxlen = sam[p].maxlen + 1;
                    sam[clone].occ = 0;
                    while (p && sam[p].nxt1 == q) {
                        sam[p].nxt1 = clone;
                        p = sam[p].link;
                    }
                    sam[q].link = clone;
                    sam[cur].link = clone;
                }
            }
        }
        last = cur;
    }
    
    for (int i = 0; i <= n; ++i) cnt_len[i] = 0;
    for (int i = 1; i <= sz; ++i) cnt_len[sam[i].maxlen]++;
    for (int i = 1; i <= n; ++i) cnt_len[i] += cnt_len[i - 1];
    for (int i = 1; i <= sz; ++i) {
        order[cnt_len[sam[i].maxlen]--] = i;
    }
    
    for (int i = sz; i >= 2; --i) {
        int u = order[i];
        sam[sam[u].link].occ += sam[u].occ;
    }
    
    for (int i = 0; i <= n; ++i) best[i] = 0;
    for (int i = 2; i <= sz; ++i) {
        int o = sam[i].occ;
        if (o <= n && sam[i].maxlen > best[o]) {
            best[o] = sam[i].maxlen;
        }
    }
    
    int cur_max = 0;
    int64_t total = 0;
    for (int k = n; k >= 1; --k) {
        if (best[k] > cur_max) cur_max = best[k];
        best[k] = cur_max;
        total += best[k];
    }
    
    return total;
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
    lib.solve_c.argtypes = [ctypes.c_int]
    return lib


def solve(n: int = 5_000_000) -> int:
    """Find the sum of non-zero L(k, S_n) for k >= 1 using linear-time Suffix Automaton."""
    if n <= 100:
        phi = (5**0.5 + 1) / 2
        s = []
        for i in range(n):
            a_i = bin(i).count("1") % 2
            b_i = int((i + 1) / phi) - int(i / phi)
            c_i = a_i ^ b_i
            s.append(str(c_i))
        s_str = "".join(s)

        total = 0
        for k in range(1, n + 1):
            max_l = 0
            for l_sub in range(1, n // k + 1):
                found = False
                for start in range(n - l_sub + 1):
                    sub = s_str[start : start + l_sub]
                    # count occurrences
                    cnt = 0
                    for pos in range(n - l_sub + 1):
                        if s_str[pos : pos + l_sub] == sub:
                            cnt += 1
                    if cnt >= k:
                        found = True
                        break
                if found:
                    max_l = l_sub
            total += max_l
        return total

    lib = _get_compiled_lib()
    ans = int(lib.solve_c(n))
    return ans


if __name__ == "__main__":
    print(solve())
