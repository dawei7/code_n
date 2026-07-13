# Longest Special Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3425 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-special-path](https://leetcode.com/problems/longest-special-path/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-special-path/).

### Goal
Given a tree where each node has a value and each edge has a weight, find the length of the longest path such that all node values on the path are unique. The length of a path is defined as the sum of the weights of the edges along that path.

### Function Contract
**Inputs**

- `edges`: A list of lists where each element `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `values`: A list of integers where `values[i]` is the value associated with node `i`.

**Return value**

- A list of two integers: `[max_length, number_of_paths]`. `max_length` is the length of the longest path with unique node values, and `number_of_paths` is the count of such paths.

### Examples
**Example 1**

- Input: `edges = [[0,1,2],[1,2,3],[1,3,5]], values = [1,2,3,4]`
- Output: `[8, 1]`

**Example 2**

- Input: `edges = [[0,1,1],[1,2,2],[2,3,3]], values = [1,1,2,2]`
- Output: `[3, 1]`

**Example 3**

- Input: `edges = [[0,1,1]], values = [1,1]`
- Output: `[1, 1]`

---

## Solution
### Approach
The problem is solved using Depth-First Search (DFS) on the tree structure. To maintain the "unique node values" constraint, we track the current path's node values using a hash map (or dictionary) that stores the depth (or prefix sum) at which each value was last encountered. As we traverse, we maintain the current prefix sum of edge weights. If a node value is repeated, we identify the valid sub-path by checking the last recorded position of that value.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes. We visit each node and edge exactly once during the DFS traversal.
- **Space Complexity**: `O(N)`, required for the adjacency list, the recursion stack, and the hash map storing node values and their associated prefix sums.

### Reference Implementations
<details>
<summary>python</summary>

```python
import sys

sys.setrecursionlimit(200000)


def solve(edges, nums):
    n = len(nums)
    graph = [[] for _ in range(n)]
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))

    best_length = 0
    best_nodes = 1
    last_depth = {}

    def dfs(node, parent, depth, distance, left_depth, path_distances):
        nonlocal best_length, best_nodes

        value = nums[node]
        previous_depth = last_depth.get(value, -1)
        current_left = max(left_depth, previous_depth + 1)
        length = distance - path_distances[current_left]
        node_count = depth - current_left + 1

        if length > best_length:
            best_length = length
            best_nodes = node_count
        elif length == best_length:
            best_nodes = min(best_nodes, node_count)

        old_depth = last_depth.get(value)
        last_depth[value] = depth

        for child, edge_length in graph[node]:
            if child == parent:
                continue
            path_distances.append(distance + edge_length)
            dfs(child, node, depth + 1, distance + edge_length, current_left, path_distances)
            path_distances.pop()

        if old_depth is None:
            del last_depth[value]
        else:
            last_depth[value] = old_depth

    dfs(0, -1, 0, 0, 0, [0])
    return [best_length, best_nodes]
```
</details>
