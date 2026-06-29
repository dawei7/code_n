import sys
from collections import deque

def choose_provinces(n: int, incomes: list[int], populations: list[int], edges: list[tuple[int, int]]) -> list[int]:
    best = 0
    for i in range(1, n):
        if incomes[i] * populations[best] > incomes[best] * populations[i]:
            best = i
    eligible = [incomes[i] * populations[best] == incomes[best] * populations[i] for i in range(n)]
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        if eligible[u] and eligible[v]:
            graph[u].append(v)
            graph[v].append(u)
    seen = [False] * n
    answer: list[int] = []
    for i in range(n):
        if not eligible[i] or seen[i]:
            continue
        seen[i] = True
        queue = deque([i])
        component: list[int] = []
        while queue:
            node = queue.popleft()
            component.append(node + 1)
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    queue.append(nxt)
        if len(component) > len(answer):
            answer = component
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
        incomes = data[idx:idx + n]
        idx += n
        populations = data[idx:idx + n]
        idx += n
        edges = []
        for _ in range(m):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        chosen = choose_provinces(n, incomes, populations, edges)
        out.append(str(len(chosen)))
        out.append(' '.join(map(str, chosen)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
