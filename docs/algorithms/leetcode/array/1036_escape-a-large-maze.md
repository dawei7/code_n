# Escape a Large Maze

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1036 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search |
| Official Link | [escape-a-large-maze](https://leetcode.com/problems/escape-a-large-maze/) |

## Problem Description & Examples
### Goal
On a very large square grid, some cells are blocked. Determine whether it is possible to move from `source` to `target` using four-directional moves without stepping on a blocked cell.

### Function Contract
**Inputs**

- `blocked`: List[List[int]] blocked coordinates
- `source`: List[int] starting coordinate
- `target`: List[int] destination coordinate

**Return value**

bool - whether the target can be reached

### Examples
**Example 1**

- Input: `blocked = [[0, 1], [1, 0]], source = [0, 0], target = [0, 2]`
- Output: `False`

**Example 2**

- Input: `blocked = [], source = [0, 0], target = [999999, 999999]`
- Output: `True`

**Example 3**

- Input: `blocked = [[10, 10], [10, 11]], source = [0, 0], target = [20, 20]`
- Output: `True`

---

## Underlying Base Algorithm(s)
Bounded breadth-first search with enclosure detection.

---

## Complexity Analysis
- **Time Complexity**: `O(b^2)` where `b` is the number of blocked cells
- **Space Complexity**: `O(b^2)`
