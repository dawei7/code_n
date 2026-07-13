import heapq
from collections import defaultdict


def solve(n, edges, succ_prob, start, end):
    n = max(0, int(n))
    graph = defaultdict(list)
    for index, edge in enumerate(edges):
        if not isinstance(edge, list) or len(edge) < 2:
            continue
        u, v = int(edge[0]) % max(1, n), int(edge[1]) % max(1, n)
        probability = float(succ_prob[index]) if index < len(succ_prob) else 1.0
        if probability > 1:
            probability = probability / 100.0
        probability = max(0.0, min(1.0, probability))
        graph[u].append((v, probability))
        graph[v].append((u, probability))
    start = int(start) % max(1, n) if n else 0
    end = int(end) % max(1, n) if n else 0
    heap = [(-1.0, start)]
    best = {start: 1.0}
    while heap:
        neg_prob, node = heapq.heappop(heap)
        prob = -neg_prob
        if node == end:
            return prob
        if prob < best.get(node, 0.0):
            continue
        for nxt, edge_prob in graph[node]:
            candidate = prob * edge_prob
            if candidate > best.get(nxt, 0.0):
                best[nxt] = candidate
                heapq.heappush(heap, (-candidate, nxt))
    return 0.0
