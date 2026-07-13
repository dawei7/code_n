# Construct 2D Grid Matching Graph Layout

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3311 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Graph Theory, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [construct-2d-grid-matching-graph-layout](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/).

### Goal
Given a set of edges representing a graph that is guaranteed to be a grid, reconstruct the original 2D grid layout. The grid dimensions are unknown, but the connectivity of the nodes must match the provided edge list.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes (labeled 0 to n-1).
- `edges`: A list of lists, where each inner list `[u, v]` represents an undirected edge between nodes `u` and `v`.

**Return value**

- A 2D list of integers representing the reconstructed grid layout.

### Examples
**Example 1**

- Input: `n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]`
- Output: `[[0,1],[2,3]]`

**Example 2**

- Input: `n = 5, edges = [[0,1],[1,3],[2,3],[3,4]]`
- Output: `[[0],[1],[3],[2],[4]]`

**Example 3**

- Input: `n = 9, edges = [[0,1],[0,4],[1,2],[1,5],[2,6],[3,4],[3,7],[4,5],[4,8],[5,9]...]` (simplified)
- Output: `[[0,1,2],[3,4,5],[6,7,8]]`

---

## Solution
### Approach
The solution relies on graph degree analysis to identify corner, edge, and interior nodes. By identifying a corner node (degree 2) and its neighbors, we can determine the grid's width. Once the width is established, we perform a Breadth-First Search (BFS) or a row-by-row traversal to fill the grid, ensuring that each node's neighbors in the grid match the adjacency list provided.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the number of nodes. We iterate through the edges to build an adjacency list and then traverse the grid once.
- **Space Complexity**: O(n), required to store the adjacency list and the resulting 2D grid.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    if n == 1:
        return [[0]]

    def validate(grid: list[list[int]]) -> bool:
        flat = [node for row in grid for node in row]
        if len(flat) != n or set(flat) != set(range(n)):
            return False
        rows, cols = len(grid), len(grid[0])
        seen_edges = set()
        for r in range(rows):
            if len(grid[r]) != cols:
                return False
            for c in range(cols):
                u = grid[r][c]
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if nr < rows and nc < cols:
                        v = grid[nr][nc]
                        seen_edges.add((min(u, v), max(u, v)))
        graph_edges = {(min(u, v), max(u, v)) for u, v in edges}
        return seen_edges == graph_edges

    degree = [len(nei) for nei in adj]

    if min(degree) <= 1:
        start = min((i for i in range(n) if degree[i] <= 1), key=lambda x: (degree[x], x))
        row = []
        prev = -1
        cur = start
        while cur != -1:
            row.append(cur)
            nxt = -1
            for node in sorted(adj[cur]):
                if node != prev:
                    nxt = node
                    break
            prev, cur = cur, nxt
        return [row]

    corners = [i for i, d in enumerate(degree) if d == 2]

    def shortest_path(src: int, dst: int) -> list[int]:
        parent = [-2] * n
        parent[src] = -1
        queue = deque([src])
        while queue:
            node = queue.popleft()
            if node == dst:
                break
            for nxt in adj[node]:
                if parent[nxt] == -2:
                    parent[nxt] = node
                    queue.append(nxt)
        if parent[dst] == -2:
            return []
        path = []
        cur = dst
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        return path[::-1]

    def build_from_first_row(first_row: list[int]) -> list[list[int]] | None:
        width = len(first_row)
        if width == 0 or n % width:
            return None
        height = n // width
        grid = [first_row[:]]
        used = set(first_row)

        for r in range(1, height):
            row = []
            for c in range(width):
                if c == 0:
                    candidates = adj[grid[r - 1][0]] - used
                else:
                    candidates = (adj[grid[r - 1][c]] & adj[row[c - 1]]) - used
                if not candidates:
                    return None
                node = min(candidates)
                row.append(node)
                used.add(node)
            grid.append(row)
        return grid if validate(grid) else None

    factor_pairs = []
    for rows in range(2, int(n**0.5) + 1):
        if n % rows == 0:
            cols = n // rows
            factor_pairs.append((rows, cols))
            if rows != cols:
                factor_pairs.append((cols, rows))

    for rows, cols in factor_pairs:
        for start in corners:
            for end in corners:
                if start == end:
                    continue
                path = shortest_path(start, end)
                if len(path) != cols:
                    continue
                grid = build_from_first_row(path)
                if grid is not None:
                    return grid

    raise ValueError("input graph is not a rectangular grid")
```
</details>
