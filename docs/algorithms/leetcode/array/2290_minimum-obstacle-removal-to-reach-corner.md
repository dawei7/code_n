# Minimum Obstacle Removal to Reach Corner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2290 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [minimum-obstacle-removal-to-reach-corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) |

## Problem Description & Examples
### Goal
Move from the top-left to the bottom-right of a binary grid in four directions. Entering an obstacle cell removes that obstacle at cost one; entering an empty cell costs zero. Minimize removals.

### Function Contract
**Inputs**

- `grid`: a binary matrix with empty start and destination cells.

**Return value**

The minimum number of obstacles that must be removed along a path.

### Examples
**Example 1**

- Input: `grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[0]]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Run 0-1 BFS. Maintain the best known removal cost for each cell. When relaxing a neighbor, add its grid value; push zero-cost moves to the front of a deque and obstacle moves to the back. This processes cells in nondecreasing cost without a general priority queue.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`
