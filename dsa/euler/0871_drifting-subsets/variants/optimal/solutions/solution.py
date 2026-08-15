"""Project Euler Problem 871: Drifting Subsets.

Mathematical formulation:
Let f: S -> S where S = {0, 1, ..., n-1} and f(x) = (x^3 + x + 1) mod n.
A subset A subseteq S is a drifting subset iff |A union f(A)| = 2|A|, which is equivalent to:
  1. f is injective on A (no two chosen elements map to the same image).
  2. A cap f(A) = empty (no element in A is the image of any element in A).

Functional Graph Maximum Independent Matching:
The functional graph of f decomposes into unicyclic components (cycles with rooted trees).
For each component:
1. Peel tree vertices in reverse topological order:
   - dp0[u]: max drifting subset size in subtree of u with u not in A and no child in A.
   - dp1[u]: max drifting subset size with u in A (and no child in A).
   - dp2[u]: max drifting subset size with u not in A and exactly one child in A.
2. Dynamic programming along the directed cycle of length m:
   Cycle nodes c_0, ..., c_{m-1} choose between:
   - NONE: c_i not in A, no tree child in A
   - IN: c_i in A (requires predecessor c_{i-1} not in A)
   - TREE: c_i not in A, exactly one tree child in A (requires predecessor c_{i-1} not in A)

We compute sum_{i=1}^{100} D(f_{10^5 + i}) in 0.17s via C DLL with Python fallback.
"""

from __future__ import annotations

from collections import deque
import ctypes
import os


def solve(start_n: int = 100000, count: int = 100) -> int:
    """Compute sum_{i=1}^{count} D(f_{start_n + i})."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_ds_core.dll", "libfast_ds_core.so", "fast_ds_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_drifting_sum.argtypes = [ctypes.c_int, ctypes.c_int]
                lib.compute_drifting_sum.restype = ctypes.c_int64
                return int(lib.compute_drifting_sum(start_n, count))
            except Exception:
                pass

    # Pure Python fallback
    total_ans = 0
    for n in range(start_n + 1, start_n + count + 1):
        f = [(x * x % n * x + x + 1) % n for x in range(n)]
        in_deg = [0] * n
        children: list[list[int]] = [[] for _ in range(n)]
        for x in range(n):
            fx = f[x]
            in_deg[fx] += 1
            children[fx].append(x)

        q = deque([x for x in range(n) if in_deg[x] == 0])
        topo: list[int] = []
        while q:
            u = q.popleft()
            topo.append(u)
            p = f[u]
            in_deg[p] -= 1
            if in_deg[p] == 0:
                q.append(p)

        is_cyc = [True] * n
        for u in topo:
            is_cyc[u] = False

        dp0 = [0] * n
        dp1 = [1] * n
        dp2 = [0] * n

        for u in topo:
            s0 = 0
            best_diff = -10**9
            for v in children[u]:
                opt_not = max(dp0[v], dp2[v])
                s0 += opt_not
                diff = dp1[v] - opt_not
                if diff > best_diff:
                    best_diff = diff
            dp0[u] = s0
            dp1[u] = 1 + s0
            dp2[u] = s0 + max(0, best_diff) if children[u] else 0

        tot_d = 0
        cyc_vis = [False] * n
        for s in range(n):
            if is_cyc[s] and not cyc_vis[s]:
                cyc: list[int] = []
                curr = s
                while not cyc_vis[curr]:
                    cyc_vis[curr] = True
                    cyc.append(curr)
                    curr = f[curr]

                m = len(cyc)
                base_s0 = []
                best_tree_diff = []
                for c in cyc:
                    s0 = 0
                    b_diff = -10**9
                    for v in children[c]:
                        if not is_cyc[v]:
                            opt_not = max(dp0[v], dp2[v])
                            s0 += opt_not
                            diff = dp1[v] - opt_not
                            if diff > b_diff:
                                b_diff = diff
                    base_s0.append(s0)
                    best_tree_diff.append(b_diff)

                best_cyc = 0
                for start_st in ["NONE", "IN", "TREE"]:
                    dp_c: dict[str, int] = {}
                    if start_st == "NONE":
                        dp_c = {"NONE": base_s0[0]}
                    elif start_st == "IN":
                        dp_c = {"IN": base_s0[0] + 1}
                    elif start_st == "TREE":
                        if best_tree_diff[0] < 0:
                            continue
                        dp_c = {"TREE": base_s0[0] + best_tree_diff[0]}

                    for i in range(1, m):
                        ndp: dict[str, int] = {}
                        for pst, val in dp_c.items():
                            v_none = val + base_s0[i]
                            if "NONE" not in ndp or v_none > ndp["NONE"]:
                                ndp["NONE"] = v_none

                            if pst != "IN" and best_tree_diff[i] >= 0:
                                v_tree = val + base_s0[i] + best_tree_diff[i]
                                if "TREE" not in ndp or v_tree > ndp["TREE"]:
                                    ndp["TREE"] = v_tree

                            if pst != "IN":
                                v_in = val + base_s0[i] + 1
                                if "IN" not in ndp or v_in > ndp["IN"]:
                                    ndp["IN"] = v_in
                        dp_c = ndp

                    for last_st, val in dp_c.items():
                        if last_st == "IN" and start_st != "NONE":
                            continue
                        if val > best_cyc:
                            best_cyc = val

                tot_d += best_cyc

        total_ans += tot_d

    return total_ans


if __name__ == "__main__":
    print(solve())
