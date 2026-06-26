# Detect Cycles in 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1559 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [detect-cycles-in-2d-grid](https://leetcode.com/problems/detect-cycles-in-2d-grid/) |

## Problem Description & Examples
### Goal
Detect whether a grid contains a cycle made of adjacent cells with the same
character. The cycle must have length at least four.

### Function Contract
**Inputs**

- `grid`: a matrix of lowercase letters.

**Return value**

`true` if such a same-character cycle exists; otherwise `false`.

### Examples
**Example 1**

- Input: `grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]`
- Output: `true`

**Example 2**

- Input: `grid = [["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]`
- Output: `true`

**Example 3**

- Input: `grid = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]`
- Output: `false`

---

## Underlying Base Algorithm(s)
Run DFS or BFS over same-character components. When exploring from a cell, carry
the parent cell so the immediate back edge is ignored. If a visited neighbor of
the same character is reached that is not the parent, a cycle exists.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`.
- **Space Complexity**: `O(m * n)` for visited state and traversal stack or queue.
