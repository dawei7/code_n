# Longest Special Path II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3486 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-special-path-ii](https://leetcode.com/problems/longest-special-path-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-special-path-ii/).

### Goal
Given a tree where each node has a value and each edge has a weight, identify the longest path such that no two nodes on the path share the same value. The length of a path is defined as the sum of the weights of the edges along that path.

### Function Contract
**Inputs**

- `edges`: A list of lists where each element `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `values`: A list of integers where `values[i]` is the value associated with node `i`.

**Return value**

- A list of two integers: `[max_length, count]`, where `max_length` is the maximum path length found, and `count` is the number of paths that achieve this maximum length.

### Examples
**Example 1**

- Input: `edges = [[0,1,2],[1,2,3]], values = [1,2,3]`
- Output: `[5, 1]`

**Example 2**

- Input: `edges = [[0,1,1],[0,2,2],[1,3,3],[1,4,4]], values = [1,2,1,3,4]`
- Output: `[7, 1]`

**Example 3**

- Input: `edges = [[0,1,1],[1,2,2],[2,3,3]], values = [1,1,1,1]`
- Output: `[1, 1]`

---

## Solution
### Approach
The problem is solved using Depth-First Search (DFS) on the tree structure. To maintain the "special" property (no duplicate values), we track the current path's node values using a hash map (or frequency array) and the prefix sum of edge weights from the root. As we traverse, we maintain the starting point of the current valid path by tracking the depth of the most recent occurrence of each value.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes. We visit each node and edge exactly once during the DFS traversal.
- **Space Complexity**: `O(N)`, required for the adjacency list, the recursion stack, and the hash map storing value positions.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict
from heapq import heappop, heappush
import sys

sys.setrecursionlimit(200000)


def solve(edges: list[list[int]], nums: list[int]) -> list[int]:
    n = len(nums)
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    positions: dict[int, list[int]] = defaultdict(list)
    second_heap: list[tuple[int, int, int]] = []
    third_heap: list[tuple[int, int, int]] = []
    second_version: dict[int, int] = defaultdict(int)
    third_version: dict[int, int] = defaultdict(int)
    prefix = [0] * (n + 1)
    best_length = 0
    best_nodes = 1

    def push_value_state(value: int) -> None:
        stack = positions[value]
        second_version[value] += 1
        if len(stack) >= 2:
            heappush(second_heap, (-stack[-2], value, second_version[value]))
        third_version[value] += 1
        if len(stack) >= 3:
            heappush(third_heap, (-stack[-3], value, third_version[value]))

    def is_current_second(entry: tuple[int, int, int]) -> bool:
        depth, value, version = -entry[0], entry[1], entry[2]
        stack = positions[value]
        return version == second_version[value] and len(stack) >= 2 and stack[-2] == depth

    def is_current_third(entry: tuple[int, int, int]) -> bool:
        depth, value, version = -entry[0], entry[1], entry[2]
        stack = positions[value]
        return version == third_version[value] and len(stack) >= 3 and stack[-3] == depth

    def clean_second() -> None:
        while second_heap and not is_current_second(second_heap[0]):
            heappop(second_heap)

    def clean_third() -> None:
        while third_heap and not is_current_third(third_heap[0]):
            heappop(third_heap)

    def max_third_depth() -> int:
        clean_third()
        return -third_heap[0][0] if third_heap else -1

    def second_largest_pair_start() -> int:
        clean_second()
        if len(second_heap) < 2:
            return -1
        first = heappop(second_heap)
        clean_second()
        result = -second_heap[0][0] if second_heap else -1
        heappush(second_heap, first)
        return result

    def dfs(node: int, parent: int, depth: int, distance: int) -> None:
        nonlocal best_length, best_nodes

        value = nums[node]
        positions[value].append(depth)
        push_value_state(value)

        left = max(max_third_depth() + 1, second_largest_pair_start() + 1)
        length = distance - prefix[left]
        node_count = depth - left + 1
        if length > best_length:
            best_length = length
            best_nodes = node_count
        elif length == best_length and node_count < best_nodes:
            best_nodes = node_count

        for child, weight in graph[node]:
            if child == parent:
                continue
            prefix[depth + 1] = distance + weight
            dfs(child, node, depth + 1, distance + weight)

        positions[value].pop()
        push_value_state(value)

    dfs(0, -1, 0, 0)
    return [best_length, best_nodes]
```
</details>
