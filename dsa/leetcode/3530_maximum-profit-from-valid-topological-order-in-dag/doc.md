# Maximum Profit from Valid Topological Order in DAG

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3530 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Graph Theory, Topological Sort, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-profit-from-valid-topological-order-in-dag](https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/).

### Goal
Given a Directed Acyclic Graph (DAG) represented by nodes and directed edges, and a profit value associated with each node, find the maximum total profit obtainable by selecting a valid topological ordering of the graph. Specifically, you must select a sequence of nodes such that for every edge (u, v), node u appears before node v in the sequence, and the sum of profits of the selected nodes is maximized.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes (0 to n-1).
- `edges`: A list of pairs `[u, v]` representing directed edges from `u` to `v`.
- `values`: A list of integers where `values[i]` is the profit associated with node `i`.

**Return value**

- An integer representing the maximum profit achievable under the topological constraints.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2]], values = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `n = 2, edges = [[0, 1]], values = [10, 5]`
- Output: `15`

**Example 3**

- Input: `n = 4, edges = [[0, 2], [1, 2], [2, 3]], values = [5, 10, 2, 8]`
- Output: `25`

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with Topological Sort principles. Since we are dealing with a DAG, we can utilize the property that any valid topological order respects the dependency constraints. The state is defined by the set of visited nodes (using a bitmask for efficiency if n is small, or DP on the DAG structure). For larger constraints, we use the property that the maximum profit is simply the sum of all positive node values, as we can always include all nodes in a valid topological sort of a DAG.

### Complexity Analysis
- **Time Complexity**: `O(V + E)`, where V is the number of nodes and E is the number of edges, as we traverse the graph to verify the DAG structure and sum the values.
- **Space Complexity**: `O(V + E)` to store the adjacency list and auxiliary structures for the graph traversal.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, edges: list[list[int]], values: list[int]) -> int:
    """
    In a Directed Acyclic Graph (DAG), a topological sort always exists.
    Since we want to maximize the profit of a valid topological order,
    and a topological order includes all nodes in the graph, the maximum
    profit is simply the sum of all node values, provided the graph is a DAG.
    If the problem implies selecting a subset, the logic would involve
    DP on subsets, but for a standard topological order of a DAG,
    all nodes must be included.
    """
    # Build adjacency list to verify DAG property if necessary
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # Kahn's algorithm to verify if it is a DAG
    queue = [i for i in range(n) if in_degree[i] == 0]
    count = 0
    while queue:
        u = queue.pop(0)
        count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # If count != n, it's not a DAG (though problem constraints usually guarantee it)
    if count != n:
        return 0

    return sum(values)
```
</details>
