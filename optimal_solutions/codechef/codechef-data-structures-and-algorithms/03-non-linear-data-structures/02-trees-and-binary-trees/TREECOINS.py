def dfs(node, parent, adj, coins):
    ans = 0
    for child in adj[node]:
        if child != parent:
            res = dfs(child, node, adj, coins)
            if res > 0 or coins[child]:
                ans += res + 2
    return ans

def solve():
    n = int(input())
    coins = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    coin_values = list(map(int, input().split()))
    for i in range(1, n + 1):
        coins[i] = coin_values[i - 1]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    min_time = dfs(1, 0, adj, coins)
    print(min_time)


if __name__ == "__main__":
    solve()
