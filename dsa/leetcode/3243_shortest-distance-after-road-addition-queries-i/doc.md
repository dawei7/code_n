# Shortest Distance After Road Addition Queries I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3243 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-distance-after-road-addition-queries-i](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/).

### Goal
Given a linear directed graph with $n$ nodes (0 to $n-1$) where initial edges exist from $i$ to $i+1$, process a series of queries. Each query adds a new directed edge $(u, v)$ to the graph. After each addition, calculate the length of the shortest path from node 0 to node $n-1$.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes.
- `queries`: A list of lists, where each inner list `[u, v]` represents a new directed edge added to the graph.

**Return value**

- A list of integers where the $i$-th element is the shortest path distance from node 0 to node $n-1$ after the $i$-th query.

### Examples
**Example 1**

- Input: `n = 5, queries = [[2, 4], [0, 2], [0, 4]]`
- Output: `[3, 2, 1]`

**Example 2**

- Input: `n = 4, queries = [[0, 3], [0, 2]]`
- Output: `[1, 1]`

---

## Solution
### Approach
The problem can be solved using Breadth-First Search (BFS) to find the shortest path in an unweighted directed graph. Since the number of queries is relatively small and $n$ is up to 500, running a BFS after each query is efficient enough. Alternatively, Dynamic Programming can be used to maintain the shortest distance array, updating it based on the new edge.

### Complexity Analysis
- **Time Complexity**: $O(q \cdot (n + e))$, where $q$ is the number of queries, $n$ is the number of nodes, and $e$ is the number of edges. In the worst case, this is $O(q \cdot n)$.
- **Space Complexity**: $O(n + q)$ to store the adjacency list and the results.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque

def solve(n: int, queries: list[list[int]]) -> list[int]:
    # Initialize adjacency list with default linear edges i -> i+1
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        adj[i].append(i + 1)

    def get_shortest_path():
        # Standard BFS to find shortest path from 0 to n-1
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            curr, dist = queue.popleft()
            if curr == n - 1:
                return dist
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return -1

    results = []
    for u, v in queries:
        adj[u].append(v)
        results.append(get_shortest_path())

    return results
```
</details>
