from typing import List


class Solution:
    def kthSmallest(
        self, par: List[int], vals: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(par)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)

        path_xor = [0] * n
        path_xor[0] = vals[0]

        bfs = [0]
        for u in bfs:
            for v in tree[u]:
                path_xor[v] = path_xor[u] ^ vals[v]
                bfs.append(v)

        narvetholi = path_xor

        sz = [1] * n
        heavy = [-1] * n
        for u in reversed(bfs):
            max_c = 0
            for v in tree[u]:
                sz[u] += sz[v]
                if sz[v] > max_c:
                    max_c = sz[v]
                    heavy[u] = v

        tin = [0] * n
        tout = [0] * n
        flat = [0] * n
        timer = 0

        for u in range(n):
            if heavy[u] != -1:
                tree[u].remove(heavy[u])
                tree[u].append(heavy[u])

        stack = [0]
        while stack:
            u = stack.pop()
            tin[u] = timer
            flat[timer] = u
            timer += 1
            for v in reversed(tree[u]):
                stack.append(v)
        for u in range(n):
            tout[u] = tin[u] + sz[u] - 1

        MAX_V = 262144
        BIT_MASK = 1 << 18
        bit_tree = [0] * (MAX_V + 1)
        counts = [0] * MAX_V
        total_distinct = 0

        def bit_add(val: int, delta: int) -> None:
            nonlocal total_distinct
            if delta == 1:
                counts[val] += 1
                if counts[val] == 1:
                    total_distinct += 1
                    i = val + 1
                    while i <= MAX_V:
                        bit_tree[i] += 1
                        i += i & (-i)
            else:
                counts[val] -= 1
                if counts[val] == 0:
                    total_distinct -= 1
                    i = val + 1
                    while i <= MAX_V:
                        bit_tree[i] -= 1
                        i += i & (-i)

        def find_kth(k: int) -> int:
            if k > total_distinct:
                return -1
            idx = 0
            current_sum = 0
            m = BIT_MASK
            while m > 0:
                next_idx = idx + m
                if next_idx <= MAX_V and current_sum + bit_tree[next_idx] < k:
                    idx = next_idx
                    current_sum += bit_tree[idx]
                m >>= 1
            return idx

        node_queries = [[] for _ in range(n)]
        for idx, (u, k) in enumerate(queries):
            node_queries[u].append((k, idx))

        ans = [-1] * len(queries)

        dsu_stack = [(0, 0, 1)]
        while dsu_stack:
            u, stage, keep = dsu_stack.pop()
            if stage == 0:
                dsu_stack.append((u, 1, keep))
                if heavy[u] != -1:
                    dsu_stack.append((heavy[u], 0, 1))
                for v in tree[u][:-1] if heavy[u] != -1 else tree[u]:
                    dsu_stack.append((v, 0, 0))
            else:
                for v in tree[u][:-1] if heavy[u] != -1 else []:
                    for p in range(tin[v], tout[v] + 1):
                        bit_add(path_xor[flat[p]], 1)
                bit_add(path_xor[u], 1)
                for k, q_idx in node_queries[u]:
                    ans[q_idx] = find_kth(k)
                if not keep:
                    for p in range(tin[u], tout[u] + 1):
                        bit_add(path_xor[flat[p]], -1)

        return ans
