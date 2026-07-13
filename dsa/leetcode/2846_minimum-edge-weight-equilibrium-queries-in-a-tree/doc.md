# Minimum Edge Weight Equilibrium Queries in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2846 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-edge-weight-equilibrium-queries-in-a-tree](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/).

### Goal
Given a weighted tree with $n$ nodes and $n-1$ edges (weights between 1 and 26), process a series of queries. Each query consists of two nodes $(u, v)$. For each query, determine the minimum number of edge weight modifications required to make all edges on the simple path between $u$ and $v$ have the same weight.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes in the tree.
- `edges`: A list of lists where each inner list `[u, v, w]` represents an undirected edge between `u` and `v` with weight `w`.
- `queries`: A list of lists where each inner list `[u, v]` represents a query for the path between `u` and `v`.

**Return value**

- A list of integers representing the minimum modifications for each query.

### Examples
**Example 1**

- Input: `n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]`
- Output: `[0, 0, 1, 3]`

**Example 2**

- Input: `n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,5]], queries = [[4,6],[0,4],[6,5],[7,4]]`
- Output: `[1, 2, 3, 2]`

**Example 3**

- Input: `n = 9, edges = [[0,1,3],[1,2,2],[2,3,4],[3,4,4],[4,5,1],[5,6,6],[6,7,9],[7,8,8]], queries = [[0,7],[4,8],[0,1]]`
- Output: `[6, 5, 0]`

---

## Solution
### Approach
The problem is solved using Binary Lifting to find the Lowest Common Ancestor (LCA) and to maintain prefix sums of edge weight frequencies along paths from the root. By storing the count of each weight (1-26) on the path from the root to every node, the frequency of weights on any path $(u, v)$ can be calculated as $count(u) + count(v) - 2 \times count(LCA(u, v))$. The minimum modifications required is the total number of edges on the path minus the maximum frequency of any single weight on that path.

### Complexity Analysis
- **Time Complexity**: $O((n + q) \log n)$, where $n$ is the number of nodes and $q$ is the number of queries. Preprocessing the tree takes $O(n \log n)$, and each query takes $O(\log n)$ to find the LCA and $O(26)$ to compute the result.
- **Space Complexity**: $O(n \log n)$ to store the binary lifting table and the prefix frequency counts for each node.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections
import sys

def solve(n, edges, queries):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 10))

    adj = collections.defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    LOG = n.bit_length()
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n
    # counts[node][weight-1] stores frequency of weight on path from root to node
    counts = [[0] * 26 for _ in range(n)]

    def dfs(u, p, d, current_counts):
        depth[u] = d
        up[u][0] = p
        counts[u] = list(current_counts)
        for v, w in adj[u]:
            if v != p:
                current_counts[w - 1] += 1
                dfs(v, u, d + 1, current_counts)
                current_counts[w - 1] -= 1

    dfs(0, -1, 0, [0] * 26)

    for i in range(1, LOG):
        for u in range(n):
            if up[u][i - 1] != -1:
                up[u][i] = up[up[u][i - 1]][i - 1]

    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for i in range(LOG - 1, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
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
        path_len = depth[u] + depth[v] - 2 * depth[lca]

        max_freq = 0
        for i in range(26):
            freq = counts[u][i] + counts[v][i] - 2 * counts[lca][i]
            if freq > max_freq:
                max_freq = freq

        results.append(path_len - max_freq)

    return results
```
</details>
