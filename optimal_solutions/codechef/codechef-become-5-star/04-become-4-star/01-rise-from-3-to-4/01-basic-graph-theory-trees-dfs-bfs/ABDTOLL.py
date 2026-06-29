import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    out = []
    for _ in range(num_test_cases):
        n = int(next(iterator))
        x = int(next(iterator))
        k = int(next(iterator))
        toll = [0] * (n + 1)
        for i in range(1, n + 1):
            toll[i] = int(next(iterator))
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        totalCost = 0

        def dfs(node, parent, k):
            nonlocal totalCost
            if len(adj[node]) == 1 and adj[node][0] == parent:
                totalCost += max(0, toll[node] - k) * 2
                toll[node] = min(toll[node], k)
                return toll[node]
            maxChildCost = -2147483648
            for it in adj[node]:
                if it != parent:
                    childCost = dfs(it, node, k)
                    if childCost + toll[node] > k:
                        totalCost += (childCost + toll[node] - k) * 2
                        toll[node] = k - childCost
                    maxChildCost = max(maxChildCost, childCost)
            return maxChildCost + toll[node]
        dfs(x, -1, k)
        out.append(str(totalCost))
    print('\n'.join(out))


if __name__ == "__main__":
    solve()
