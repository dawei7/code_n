## Problem Description & Examples
### Goal
Given a `m` x `n` grid filled with non-negative numbers, find a path from top-left to bottom-right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

### Function Contract
**Inputs**

- `grid`: List[List[int]]

**Return value**

int - minimum path sum

### Examples
**Example 1**

- Input: `grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]`
- Output: `7`

**Example 2**

- Input: `grid = [[1, 5], [9, 8]]`
- Output: `14`

**Example 3**

- Input: `grid = [[5, 2], [8, 8]]`
- Output: `15`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
