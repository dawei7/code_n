import sys
from collections import deque


def assignment(n: int, edges: list[tuple[int, int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    values = [0] * n
    values[0] = 1
    queue = deque([0])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if values[nxt] == 0:
                values[nxt] = 3 - values[node]
                queue.append(nxt)
    return values


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        edges = []
        for _ in range(n - 1):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        out.append(" ".join(map(str, assignment(n, edges))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
