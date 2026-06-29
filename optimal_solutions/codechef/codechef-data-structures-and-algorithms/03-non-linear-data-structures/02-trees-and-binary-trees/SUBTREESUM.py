import sys
from collections import defaultdict

def dfs(node, parent, adj, subtsum):
    subtsum[node] += node
    for neighbor in adj[node]:
        if neighbor != parent:
            dfs(neighbor, node, adj, subtsum)
            subtsum[node] += subtsum[neighbor]

def solve():
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    adj = defaultdict(list)
    subtsum = [0] * (n + 1)
    index = 1
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    dfs(1, -1, adj, subtsum)
    print(' '.join(map(str, subtsum[1:])))


if __name__ == "__main__":
    solve()
