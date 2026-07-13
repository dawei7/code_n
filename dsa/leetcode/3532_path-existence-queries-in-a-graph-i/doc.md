# Path Existence Queries in a Graph I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3532 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [path-existence-queries-in-a-graph-i](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/).

### Goal
Given an undirected graph with $n$ nodes labeled from $0$ to $n-1$ and a list of edges, determine for several query pairs $(u, v)$ whether there exists a path between node $u$ and node $v$. Since the graph is undirected, a path exists if and only if both nodes belong to the same connected component.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes in the graph.
- `edges`: A list of lists, where each inner list `[u, v]` represents an undirected edge between nodes `u` and `v`.
- `queries`: A list of lists, where each inner list `[u, v]` represents a query to check if a path exists between `u` and `v`.

**Return value**

- A list of booleans where the $i$-th element is `True` if a path exists between the $i$-th query nodes, and `False` otherwise.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2]], queries = [[0, 2]]`
- Output: `[True]`

**Example 2**

- Input: `n = 4, edges = [[0, 1], [2, 3]], queries = [[0, 3], [1, 2]]`
- Output: `[False, False]`

**Example 3**

- Input: `n = 5, edges = [[0, 1], [1, 2], [3, 4]], queries = [[0, 2], [0, 4]]`
- Output: `[True, False]`

---

## Solution
### Approach
The problem is solved using the **Disjoint Set Union (DSU)** (also known as Union-Find) data structure. By iterating through all edges and performing `union` operations, we group all connected nodes into the same set. For each query, we perform a `find` operation on both nodes; if they share the same root representative, they are connected.

### Complexity Analysis
- **Time Complexity**: $O((E + Q) \cdot \alpha(n))$, where $E$ is the number of edges, $Q$ is the number of queries, and $\alpha$ is the inverse Ackermann function, which is nearly constant.
- **Space Complexity**: $O(n)$ to store the parent array for the DSU structure.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[bool]:
    parent = list(range(n))

    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> None:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for u, v in edges:
        union(u, v)

    results = []
    for u, v in queries:
        results.append(find(u) == find(v))

    return results
```
</details>
