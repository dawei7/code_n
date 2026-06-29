import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    graph = [[] for _ in range(n)]
    idx = 1
    for _ in range(n - 1):
        u, v = data[idx], data[idx + 1]
        idx += 2
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * n
    order = [0]
    parent[0] = -2
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    count = [1] * n
    down = [0] * n
    for u in reversed(order):
        for v in graph[u]:
            if parent[v] == u:
                count[u] += count[v]
                down[u] += count[v] + down[v]

    ans = [0] * n
    ans[0] = down[0]
    for u in order:
        for v in graph[u]:
            if parent[v] == u:
                ans[v] = ans[u] + n - 2 * count[v]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
