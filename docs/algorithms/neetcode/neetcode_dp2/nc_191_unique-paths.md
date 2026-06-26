## Problem Description & Examples
### Goal
There is a robot on an `m` x `n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Function Contract
**Inputs**

- `m`: int
- `n`: int

**Return value**

int - number of unique paths

### Examples
**Example 1**

- Input: `m = 3, n = 7`
- Output: `28`

**Example 2**

- Input: `m = 2, n = 2`
- Output: `2`

**Example 3**

- Input: `m = 3, n = 2`
- Output: `3`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
