import sys

sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]], price: list[int]) -> int:
    if n == 1:
        return 0

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    ans = 0

    def dfs(u, p):
        nonlocal ans

        best_keep = price[u]
        best_drop = 0

        for v in adj[u]:
            if v == p:
                continue
            child_keep, child_drop = dfs(v, u)
            ans = max(ans, best_keep + child_drop, best_drop + child_keep)
            best_keep = max(best_keep, price[u] + child_keep)
            best_drop = max(best_drop, price[u] + child_drop)

        return best_keep, best_drop

    dfs(0, -1)
    return ans
