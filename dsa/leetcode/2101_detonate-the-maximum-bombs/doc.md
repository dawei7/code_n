# Detonate the Maximum Bombs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2101 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Graph Theory, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [detonate-the-maximum-bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/detonate-the-maximum-bombs/).

### Goal
Detonating one bomb triggers every bomb whose center lies within its blast radius, potentially causing a chain reaction. Maximize the number detonated from one starting bomb.

### Function Contract
**Inputs**

- `bombs`: entries `[x, y, radius]`.

**Return value**

Return the largest chain-reaction size.

### Examples
**Example 1**

- Input: `bombs = [[2,1,3],[6,1,4]]`
- Output: `2`

**Example 2**

- Input: `bombs = [[1,1,5],[10,10,5]]`
- Output: `1`

**Example 3**

- Input: `bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]`
- Output: `5`

---

## Solution
### Approach
Build a directed graph: add edge `i -> j` when squared center distance is at most `radius_i^2`. Run DFS or BFS from every bomb and take the maximum number of reachable nodes.

### Complexity Analysis
- **Time Complexity**: `O(n^3)` with a traversal from every node after `O(n^2)` graph construction.
- **Space Complexity**: `O(n^2)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
