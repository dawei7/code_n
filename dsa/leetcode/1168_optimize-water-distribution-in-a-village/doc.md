# Optimize Water Distribution in a Village

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1168 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [optimize-water-distribution-in-a-village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/optimize-water-distribution-in-a-village/).

### Goal
Each house needs water. You may either build a well at a house or connect houses with bidirectional pipes so water can flow from a house that has access. Return the minimum total cost to supply every house.

### Function Contract
**Inputs**

- `n`: Number of houses labeled `1` through `n`.
- `wells`: `wells[i - 1]` is the cost to build a well at house `i`.
- `pipes`: Each entry `[house1, house2, cost]` is a possible pipe.

**Return value**

Minimum total cost to provide water to all houses.

### Examples
**Example 1**

- Input: `n = 3`, `wells = [1, 2, 2]`, `pipes = [[1, 2, 1], [2, 3, 1]]`
- Output: `3`

**Example 2**

- Input: `n = 2`, `wells = [1, 1]`, `pipes = [[1, 2, 1], [1, 2, 2]]`
- Output: `2`

**Example 3**

- Input: `n = 5`, `wells = [5, 4, 6, 2, 3]`, `pipes = [[1, 2, 1], [2, 3, 2], [4, 5, 1]]`
- Output: `10`

---

## Solution
### Approach
Create a virtual node `0` representing a water source. Add an edge from `0` to each house `i` with cost `wells[i - 1]`, meaning "build a well here". Keep every pipe as an edge between houses.

The problem becomes finding a minimum spanning tree over nodes `0..n`. Kruskal's algorithm with union-find selects the cheapest combination of wells and pipes.

### Complexity Analysis
- **Time Complexity**: `O((n + p) log (n + p))`, where `p` is the number of pipes.
- **Space Complexity**: `O(n + p)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
