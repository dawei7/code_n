import sys

def solve_case(values: list[int], edges: list[tuple[int, int]]) -> int:
    directed = []
    for u, v in edges:
        u -= 1
        v -= 1
        if values[u] < values[v]:
            directed.append((values[v] - values[u], u, v))
        elif values[v] < values[u]:
            directed.append((values[u] - values[v], v, u))
    directed.sort()
    best = [1] * len(values)
    answer = 1
    i = 0
    while i < len(directed):
        j = i
        updates: list[tuple[int, int]] = []
        diff = directed[i][0]
        while j < len(directed) and directed[j][0] == diff:
            _d, u, v = directed[j]
            updates.append((v, best[u] + 1))
            j += 1
        for node, value in updates:
            if value > best[node]:
                best[node] = value
                if value > answer:
                    answer = value
        i = j
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, m = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        edges = []
        for _ in range(m):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        out.append(str(solve_case(values, edges)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
