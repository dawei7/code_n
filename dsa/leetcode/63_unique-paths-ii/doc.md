# Unique Paths II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 63 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-paths-ii/) |

## Problem Description
### Goal
You are given a rectangular grid where `0` marks a free cell and `1` marks an obstacle. A robot begins at the top-left cell and wants to reach the bottom-right, moving exactly one cell right or down at each step.

Count the unique paths that never enter an obstacle and return that number. If the start or destination is blocked, no path exists. Obstacles may force detours or disconnect the destination entirely, while a single free cell represents one valid zero-move path.

### Function Contract
**Inputs**

- `obstacle_grid`: an `m` by `n` matrix of zeros and ones

**Return value**

The number of valid paths that never enter an obstacle.

### Examples
**Example 1**

- Input: `obstacle_grid = [[0,0,0],[0,1,0],[0,0,0]]`
- Output: `2`

**Example 2**

- Input: `obstacle_grid = [[0,1],[0,0]]`
- Output: `1`

**Example 3**

- Input: `obstacle_grid = [[1]]`
- Output: `0`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**One rolling row preserves both predecessor counts**

Let `paths[column]` represent the number of ways to reach the relevant cell in that column. Before a current-row update, its old value is the count from directly above; after the previous column has been updated, `paths[column - 1]` is the count from directly left. Their sum therefore implements the full two-dimensional recurrence in one array.

**An obstacle erases every path arriving at that cell**

When the current cell is blocked, set its count to zero instead of adding predecessors. This prevents cells later in the row from inheriting a path that crossed the obstacle. Initialize `paths[0] = 1` before scanning; a blocked start resets it to zero naturally, and that zero propagates until another route from above becomes available in a later column.

**Update order distinguishes current-row left from previous-row above**

After processing cell `(row, column)`, `paths[column]` equals the number of legal paths to that cell. Entries to its left describe the current row, while entries to its right still describe the previous row, exactly matching the two predecessor directions.

**Trace an obstacle cutting one predecessor direction**

For `[[0,0,0],[0,1,0],[0,0,0]]`, the first row becomes `[1,1,1]`. The center obstacle changes the second row to `[1,0,1]`; the final row accumulates `[1,1,2]`, so two paths reach the destination.

**Final moves partition the paths to each free cell**

Every legal path reaching a free cell ends with exactly one of two moves: down from above or right from the left. Those path sets are disjoint because their final edges differ, so their counts add without duplication. An obstacle admits no path and resets its state to zero, preventing routes from passing through it.

Processing in row-major order ensures both predecessor counts are already complete when a cell is updated. The destination state therefore counts all and only obstacle-avoiding paths.

#### Complexity detail

Each of the `mn` cells is processed once, giving $O(mn)$ time. The rolling array contains `n` counts, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Full two-dimensional DP:** has the same time complexity but uses $O(mn)$ additional space.
- **Unmemoized path recursion:** is faithful to the movement choices but repeats subproblems exponentially.
- **In-place counts in the grid:** can use constant auxiliary space but destroys the obstacle input.
- A blocked start or blocked destination yields zero. A one-cell free grid has one path consisting of that cell alone.
- The rolling array width can use the smaller grid dimension only if traversal and indexing are transposed carefully; the straightforward form uses one entry per column.

</details>
