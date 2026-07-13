# Reachable Nodes With Restrictions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2368 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reachable-nodes-with-restrictions](https://leetcode.com/problems/reachable-nodes-with-restrictions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reachable-nodes-with-restrictions/).

### Goal
Given an undirected tree structure represented by edges, determine the total number of nodes reachable from the root (node 0) without passing through any of the nodes specified in a restricted set.

### Function Contract
**Inputs**

- `n` (int): The total number of nodes in the tree, labeled from 0 to n-1.
- `edges` (List[List[int]]): A list of pairs representing undirected connections between nodes.
- `restricted` (List[int]): A list of nodes that cannot be visited.

**Return value**

- `int`: The count of unique nodes reachable starting from node 0, excluding any restricted nodes.

### Examples
**Example 1**

- Input: `n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]`
- Output: `4`

**Example 2**

- Input: `n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]`
- Output: `3`

**Example 3**

- Input: `n = 10, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], restricted = [3,6,9]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a Graph Traversal algorithm, specifically Depth-First Search (DFS) or Breadth-First Search (BFS). By representing the tree as an adjacency list, we can traverse the graph starting from node 0 while maintaining a set of restricted nodes to prune the search space.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the number of nodes. We visit each node and edge at most once during the traversal.
- **Space Complexity**: O(n), required to store the adjacency list representation of the tree and the recursion stack (or queue) during traversal.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import deque, defaultdict

def solve(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Convert restricted list to a set for O(1) lookup
    restricted_set = set(restricted)

    # BFS traversal starting from node 0
    count = 0
    queue = deque([0])
    visited = {0}

    while queue:
        curr = queue.popleft()
        count += 1

        for neighbor in adj[curr]:
            if neighbor not in visited and neighbor not in restricted_set:
                visited.add(neighbor)
                queue.append(neighbor)

    return count
```
</details>
