# Flower Planting With No Adjacent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1042 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [flower-planting-with-no-adjacent](https://leetcode.com/problems/flower-planting-with-no-adjacent/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/flower-planting-with-no-adjacent/).

### Goal
There are `n` gardens connected by paths, and each garden must receive one of four flower types. Choose flower types so that no two directly connected gardens have the same type.

### Function Contract
**Inputs**

- `n`: Number of gardens, labeled from `1` to `n`.
- `paths`: Undirected edges between gardens.

**Return value**

List of `n` flower types, each in `1..4`. Any valid assignment is accepted.

### Examples
**Example 1**

- Input: `n = 3, paths = [[1, 2], [2, 3], [3, 1]]`
- Output: `[1, 2, 3]`

**Example 2**

- Input: `n = 4, paths = [[1, 2], [3, 4]]`
- Output: `[1, 2, 1, 2]`

**Example 3**

- Input: `n = 4, paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]`
- Output: `[1, 2, 3, 4]`

---

## Solution
### Approach
Build the adjacency list and assign gardens from `1` to `n`. For each garden, inspect the flower types already used by its neighbors and choose the smallest type from `1..4` that is not used.

The problem guarantees each garden has at most three neighbors, so one of the four types is always available.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`, where `m` is the number of paths.
- **Space Complexity**: `O(n + m)` for the graph and answer.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
