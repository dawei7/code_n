# Connecting Cities With Minimum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1135 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [connecting-cities-with-minimum-cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/connecting-cities-with-minimum-cost/).

### Goal
Given `n` cities and possible bidirectional connections with costs, choose a set of connections with minimum total cost so that every city is connected. Return `-1` if connecting all cities is impossible.

### Function Contract
**Inputs**

- `n`: Number of cities labeled `1` through `n`.
- `connections`: List of `[city_a, city_b, cost]` edges.

**Return value**

Minimum total cost to connect all cities, or `-1`.

### Examples
**Example 1**

- Input: `n = 3, connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]`
- Output: `6`

**Example 2**

- Input: `n = 4, connections = [[1, 2, 3], [3, 4, 4]]`
- Output: `-1`

**Example 3**

- Input: `n = 4, connections = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [1, 4, 10]]`
- Output: `6`

---

## Solution
### Approach
This is a minimum spanning tree problem. Sort connections by cost and process them with union-find. Whenever an edge connects two previously separate components, include its cost and union the components.

After processing edges, all cities are connected only if exactly `n - 1` edges were chosen.

### Complexity Analysis
- **Time Complexity**: `O(e log e)`, where `e` is the number of connections.
- **Space Complexity**: `O(n)` for union-find.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
