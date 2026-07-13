# Build a Matrix With Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2392 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Graph Theory, Topological Sort, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [build-a-matrix-with-conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/build-a-matrix-with-conditions/).

### Goal
You are given a positive integer `k`. You are also given:
- `row_conditions`: a 2D integer array where `row_conditions[i] = [u_i, v_i]`
- `col_conditions`: a 2D integer array where `col_conditions[i] = [u_i, v_i]`

The conditions mean that number `u_i` must appear in a row/column above/left of `v_i`.

Build a `k x k` matrix containing integers from `1` to `k` (each exactly once, empty cells are `0`) satisfying all conditions. Return empty list if impossible.

### Function Contract
**Inputs**

- `k`: int
- `row_conditions`: List[List[int]]
- `col_conditions`: List[List[int]]

**Return value**

List[List[int]] - matrix or empty list

### Examples
**Example 1**

- Input: `k = 3, row_conditions = [[1, 2]], col_conditions = [[3, 2]]`
- Output: `[[3, 0, 0], [0, 0, 1], [0, 2, 0]]`

**Example 2**

- Input: `k = 2, row_conditions = [[1, 2], [1, 2]], col_conditions = [[1, 2], [1, 2]]`
- Output: `[[1, 0], [0, 2]]`

**Example 3**

- Input: `k = 3, row_conditions = [[1, 2], [1, 3], [1, 3]], col_conditions = [[1, 2], [1, 2], [1, 3]]`
- Output: `[[1, 0, 0], [0, 2, 0], [0, 0, 3]]`

---

## Solution
### Approach
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
