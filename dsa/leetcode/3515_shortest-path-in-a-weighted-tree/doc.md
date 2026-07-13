# Shortest Path in a Weighted Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3515 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-path-in-a-weighted-tree](https://leetcode.com/problems/shortest-path-in-a-weighted-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-path-in-a-weighted-tree/).

### Goal
Given a weighted tree structure and a set of queries, determine the shortest path distance between two specified nodes for each query. The tree edges have associated weights, and the path distance is defined as the sum of weights of all edges connecting the two nodes.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes in the tree (labeled 0 to n-1).
- `edges`: A list of lists where each inner list `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `queries`: A list of lists where each inner list `[start, end]` represents a request to find the distance between `start` and `end`.

**Return value**

- A list of integers where the $i$-th element is the shortest path distance for the $i$-th query.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1, 5], [1, 2, 3]], queries = [[0, 2]]`
- Output: `[8]`

**Example 2**

- Input: `n = 4, edges = [[0, 1, 1], [1, 2, 2], [1, 3, 3]], queries = [[0, 2], [2, 3]]`
- Output: `[3, 5]`

**Example 3**

- Input: `n = 5, edges = [[0, 1, 2], [0, 2, 4], [1, 3, 1], [1, 4, 7]], queries = [[3, 4], [2, 3]]`
- Output: `[8, 7]`

---

## Solution
### Approach
The problem is solved using the Lowest Common Ancestor (LCA) approach. Since the distance between two nodes $u$ and $v$ in a tree is given by $dist(root, u) + dist(root, v) - 2 \times dist(root, LCA(u, v))$, we precompute the depths and distances from the root using DFS, and use Binary Lifting to find the LCA in logarithmic time.

### Complexity Analysis
- **Time Complexity**: $O((n + q) \log n)$, where $n$ is the number of nodes and $q$ is the number of queries. Preprocessing the tree takes $O(n \log n)$ and each query takes $O(\log n)$.
- **Space Complexity**: $O(n \log n)$ to store the binary lifting table (ancestor table).

### Reference Implementations
<details>
<summary>python</summary>

```python
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(n, edges, queries):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    LOG = n.bit_length()
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n
    dist = [0] * n

    def dfs(u, p, d, w):
        depth[u] = d
        dist[u] = w
        up[u][0] = p
        for v, weight in adj[u]:
            if v != p:
                dfs(v, u, d + 1, w + weight)

    dfs(0, -1, 0, 0)

    for i in range(1, LOG):
        for u in range(n):
            if up[u][i-1] != -1:
                up[u][i] = up[up[u][i-1]][i-1]

    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u

        diff = depth[u] - depth[v]
        for i in range(LOG):
            if (diff >> i) & 1:
                u = up[u][i]

        if u == v:
            return u

        for i in range(LOG - 1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]

        return up[u][0]

    results = []
    for u, v in queries:
        lca = get_lca(u, v)
        d = dist[u] + dist[v] - 2 * dist[lca]
        results.append(d)

    return results
```
</details>
