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
        values = data[idx:idx + n]
        idx += n
        adj = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = data[idx] - 1
            v = data[idx + 1] - 1
            idx += 2
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        order = [0]
        for node in order:
            for nei in adj[node]:
                if nei != parent[node]:
                    parent[nei] = node
                    order.append(nei)

        sub_gcd = values[:]
        side_sum = [0] * n
        for node in reversed(order):
            g = values[node]
            total = 0
            for child in adj[node]:
                if parent[child] == node:
                    g = math.gcd(g, sub_gcd[child])
                    total += sub_gcd[child]
            sub_gcd[node] = g
            side_sum[node] = total

        best = 0
        stack = [(0, 0)]
        while stack:
            node, carry = stack.pop()
            best = max(best, carry + side_sum[node])
            for child in adj[node]:
                if parent[child] == node:
                    stack.append((child, carry + side_sum[node] - sub_gcd[child]))
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
