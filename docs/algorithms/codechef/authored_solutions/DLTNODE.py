import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        adj = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = data[idx] - 1
            v = data[idx + 1] - 1
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
        values = data[idx:idx + n]
        idx += n

        parent = [-1] * n
        order = [0]
        for node in order:
            for nei in adj[node]:
                if nei != parent[node]:
                    parent[nei] = node
                    order.append(nei)

        sub_gcd = values[:]
        for node in reversed(order):
            g = values[node]
            for nei in adj[node]:
                if parent[nei] == node:
                    g = math.gcd(g, sub_gcd[nei])
            sub_gcd[node] = g

        up_gcd = [0] * n
        for node in order:
            comps = []
            for nei in adj[node]:
                comps.append(up_gcd[node] if nei == parent[node] else sub_gcd[nei])
            prefix = [0]
            for g in comps:
                prefix.append(math.gcd(prefix[-1], g))
            suffix = [0] * (len(comps) + 1)
            for i in range(len(comps) - 1, -1, -1):
                suffix[i] = math.gcd(suffix[i + 1], comps[i])
            for i, nei in enumerate(adj[node]):
                if parent[nei] == node:
                    up_gcd[nei] = math.gcd(values[node], math.gcd(prefix[i], suffix[i + 1]))

        best = 0
        for node in range(n):
            total = 0
            for nei in adj[node]:
                total += up_gcd[node] if nei == parent[node] else sub_gcd[nei]
            best = max(best, total)
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
