import sys


def orient_graph(n: int, edges: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    degree = [0] * n
    for idx, (u, v) in enumerate(edges):
        u -= 1
        v -= 1
        graph[u].append((v, idx))
        graph[v].append((u, idx))
        degree[u] += 1
        degree[v] += 1

    if any(value % 2 for value in degree):
        return None

    # All cities must belong to the single road network.
    seen = [False] * n
    stack = [0]
    seen[0] = True
    while stack:
        node = stack.pop()
        for nxt, _edge_idx in graph[node]:
            if not seen[nxt]:
                seen[nxt] = True
                stack.append(nxt)
    if not all(seen):
        return None

    answer: list[tuple[int, int] | None] = [None] * len(edges)
    used = [False] * len(edges)
    cursor = [0] * n
    stack_edges: list[tuple[int, int]] = [(0, -1)]

    while stack_edges:
        node, incoming_edge = stack_edges[-1]
        while cursor[node] < len(graph[node]) and used[graph[node][cursor[node]][1]]:
            cursor[node] += 1
        if cursor[node] == len(graph[node]):
            stack_edges.pop()
            if incoming_edge != -1 and stack_edges:
                prev = stack_edges[-1][0]
                answer[incoming_edge] = (prev + 1, node + 1)
        else:
            nxt, edge_idx = graph[node][cursor[node]]
            used[edge_idx] = True
            stack_edges.append((nxt, edge_idx))

    if not all(used):
        return None
    return [edge for edge in answer if edge is not None]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    idx = 2
    edges = []
    for _ in range(m):
        edges.append((data[idx], data[idx + 1]))
        idx += 2
    oriented = orient_graph(n, edges)
    if oriented is None:
        print("NO")
    else:
        out = ["YES"]
        out.extend(f"{u} {v}" for u, v in oriented)
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
