# Path with Maximum Probability

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1514 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [path-with-maximum-probability](https://leetcode.com/problems/path-with-maximum-probability/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/path-with-maximum-probability/).

### Goal
In an undirected graph whose edges have success probabilities, find the path
from `start` to `end` with the largest product of edge probabilities.

### Function Contract
**Inputs**

- `n`: the number of nodes labeled from `0` to `n - 1`.
- `edges`: undirected edges.
- `succProb`: success probability for each corresponding edge.
- `start`: the starting node.
- `end`: the destination node.

**Return value**

The maximum success probability, or `0.0` if no path exists.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.2], start = 0, end = 2`
- Output: `0.25`

**Example 2**

- Input: `n = 3, edges = [[0, 1], [1, 2], [0, 2]], succProb = [0.5, 0.5, 0.3], start = 0, end = 2`
- Output: `0.3`

**Example 3**

- Input: `n = 3, edges = [[0, 1]], succProb = [0.5], start = 0, end = 2`
- Output: `0.0`

---

## Solution
### Approach
Build an adjacency list and run a Dijkstra-style search with a max-heap ordered
by current path probability. When visiting an edge, multiply the current
probability by the edge probability and relax the neighbor if that product is
better than its best known value.

### Complexity Analysis
- **Time Complexity**: `O((n + e) log n)`, where `e` is the number of edges.
- **Space Complexity**: `O(n + e)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
