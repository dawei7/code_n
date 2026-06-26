# Max Value of Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1499 |
| Difficulty | Hard |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Official Link | [max-value-of-equation](https://leetcode.com/problems/max-value-of-equation/) |

## Problem Description & Examples
### Goal
Given points sorted by increasing `x`, choose two points `i < j` with
`xj - xi <= k` and maximize `yi + yj + |xi - xj|`.

### Function Contract
**Inputs**

- `points`: a list of `[x, y]` coordinates sorted by `x`.
- `k`: the maximum allowed horizontal distance.

**Return value**

The largest equation value among valid pairs.

### Examples
**Example 1**

- Input: `points = [[1, 3], [2, 0], [5, 10], [6, -10]], k = 1`
- Output: `4`

**Example 2**

- Input: `points = [[0, 0], [3, 0], [9, 2]], k = 3`
- Output: `3`

**Example 3**

- Input: `points = [[1, 1], [2, 2], [3, 3]], k = 2`
- Output: `6`

---

## Underlying Base Algorithm(s)
Because `xj >= xi`, the expression becomes `yj + xj + (yi - xi)`. Sweep points
from left to right and keep a monotonic deque of previous candidates ordered by
their `yi - xi` value. Remove candidates that are more than `k` away, use the
front as the best partner for the current point, then insert the current point
while preserving decreasing candidate value.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.
