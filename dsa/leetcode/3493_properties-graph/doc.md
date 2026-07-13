# Properties Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3493 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [properties-graph](https://leetcode.com/problems/properties-graph/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/properties-graph/).

### Goal
Given a directed graph represented by an adjacency list, determine the properties of the graph's components. Specifically, identify if each connected component is a simple cycle, a tree, or a more complex structure (like a functional graph component), and calculate the total number of nodes involved in cycles versus those in tree-like structures attached to cycles.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes (labeled 0 to n-1).
- `edges`: A list of lists where each `[u, v]` represents a directed edge from node `u` to node `v`.

**Return value**

- A list of integers or a structured object representing the classification of each component (e.g., count of cyclic nodes and count of tree nodes).

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2], [2, 0]]`
- Output: `[3, 0]` (A single cycle of 3 nodes, 0 tree nodes)

**Example 2**

- Input: `n = 4, edges = [[0, 1], [1, 2], [2, 1]]`
- Output: `[2, 2]` (A cycle of 2 nodes, 2 nodes forming a path leading into the cycle)

**Example 3**

- Input: `n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]`
- Output: `[0, 5]` (No cycles, 5 nodes forming a directed path/tree)

---

## Solution
### Approach
The problem is solved using Kahn's Algorithm (Topological Sort) to peel away the "tree" parts of the graph. Nodes that remain after the topological sort are part of cycles. We use an in-degree array to identify nodes with no incoming edges, iteratively removing them to isolate the cyclic components.

### Complexity Analysis
- **Time Complexity**: `O(V + E)`, where V is the number of vertices and E is the number of edges, as we traverse each node and edge a constant number of times.
- **Space Complexity**: `O(V + E)` to store the adjacency list and the in-degree array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(properties: list[list[int]], k: int) -> int:
    n = len(properties)
    sets = [set(row) for row in properties]
    parent = list(range(n))

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(a: int, b: int) -> None:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    for i in range(n):
        for j in range(i + 1, n):
            if len(sets[i] & sets[j]) >= k:
                union(i, j)

    return len({find(i) for i in range(n)})
```
</details>
