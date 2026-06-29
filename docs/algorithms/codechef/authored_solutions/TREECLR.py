import sys


MOD = 1_000_000_007


def falling(start: int, count: int) -> int:
    if count < 0 or start < count:
        return 0
    result = 1
    for x in range(start, start - count, -1):
        result = (result * x) % MOD
    return result


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    colors = data[1]
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(n - 1):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * n
    order = [0]
    for node in order:
        for child in adj[node]:
            if child != parent[node]:
                parent[child] = node
                order.append(child)

    answer = colors % MOD
    answer = (answer * falling(colors - 1, len(adj[0]))) % MOD
    for node in order[1:]:
        child_count = len(adj[node]) - 1
        answer = (answer * falling(colors - 2, child_count)) % MOD

    print(answer)


if __name__ == "__main__":
    main()
