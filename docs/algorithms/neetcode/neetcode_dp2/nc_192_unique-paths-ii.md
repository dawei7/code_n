## Problem Description & Examples
### Goal
You are given an `m` x `n` integer array `obstacle_grid` where `obstacle_grid[i][j]` represents whether there is an obstacle (1) or a free space (0) at that cell.

Return the number of unique paths from the top-left corner to the bottom-right corner. The robot can only move down or right.

### Function Contract
**Inputs**

- `obstacle_grid`: List[List[int]]

**Return value**

int - number of unique paths

### Examples
**Example 1**

- Input: `obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]`
- Output: `2`

**Example 2**

- Input: `obstacle_grid = [[0, 1], [0, 0]]`
- Output: `1`

**Example 3**

- Input: `obstacle_grid = [[0, 0], [0, 0]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
