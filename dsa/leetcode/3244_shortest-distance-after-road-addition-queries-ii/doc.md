# Shortest Distance After Road Addition Queries II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3244 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Graph Theory, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-distance-after-road-addition-queries-ii](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/).

### Goal
Given a linear path of $n$ cities indexed from $0$ to $n-1$ with initial roads connecting city $i$ to $i+1$, we receive a series of queries. Each query adds a new directed road from city $u$ to city $v$. After each addition, calculate the shortest path distance from city $0$ to city $n-1$. The roads are always added such that $u < v$, and the new roads never cross existing ones in a way that would invalidate the path structure.

### Function Contract
**Inputs**

- `n`: An integer representing the number of cities.
- `queries`: A list of lists, where each inner list `[u, v]` represents a new directed road from city `u` to city `v`.

**Return value**

- A list of integers representing the shortest path distance from city $0$ to city $n-1$ after each query is processed.

### Examples
**Example 1**

- Input: `n = 5, queries = [[2, 4], [0, 2], [0, 4]]`
- Output: `[3, 2, 1]`

**Example 2**

- Input: `n = 5, queries = [[0, 3], [0, 2]]`
- Output: `[2, 2]`

**Example 3**

- Input: `n = 4, queries = [[0, 3]]`
- Output: `[1]`

---

## Solution
### Approach
The problem can be solved using a greedy approach combined with a data structure to manage active intervals. Since we only add roads that skip intermediate nodes, we can maintain a set of "active" nodes that are part of the current shortest path. When a new road $(u, v)$ is added, any existing nodes between $u$ and $v$ are bypassed. We use a sorted collection (or a Disjoint Set Union / SortedList) to track the next reachable node from any given city, allowing us to efficiently remove nodes that are no longer part of the shortest path.

### Complexity Analysis
- **Time Complexity**: $O(q \log n)$, where $q$ is the number of queries. We use a sorted data structure to find and remove bypassed nodes, and each node is removed at most once.
- **Space Complexity**: $O(n)$, to store the mapping of the next reachable city for each node.

### Reference Implementations
<details>
<summary>python</summary>

```python
import bisect

def solve(n: int, queries: list[list[int]]) -> list[int]:
    # We maintain a sorted list of cities that are currently "entry points"
    # to the next segment of the path. Initially, every city i is connected to i+1.
    # The distance is initially n - 1.

    # Using a sorted list to keep track of the indices that are currently
    # part of the shortest path sequence.
    # Initially, the path is 0 -> 1 -> 2 -> ... -> n-1
    active_nodes = list(range(n))
    current_dist = n - 1
    results = []

    for u, v in queries:
        # Find the position of u and v in our active nodes list
        idx_u = bisect.bisect_left(active_nodes, u)
        idx_v = bisect.bisect_left(active_nodes, v)

        # If u and v are already connected by a shortcut or the path is already
        # shorter, we check if we need to remove nodes between them.
        # If active_nodes[idx_u] == u and active_nodes[idx_v] == v,
        # then all nodes between idx_u and idx_v are bypassed.
        if idx_u + 1 < idx_v:
            # The number of nodes removed is (idx_v - idx_u - 1)
            nodes_to_remove = idx_v - idx_u - 1
            current_dist -= nodes_to_remove
            # Remove the bypassed nodes from the active list
            del active_nodes[idx_u + 1 : idx_v]

        results.append(current_dist)

    return results
```
</details>
