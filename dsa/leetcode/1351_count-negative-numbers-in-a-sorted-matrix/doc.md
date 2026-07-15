# Count Negative Numbers in a Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1351 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) |

## Problem Description

### Goal

You are given a rectangular integer matrix `grid`. The values in every row are sorted in non-increasing order from left to right, and the values in every column are also sorted in non-increasing order from top to bottom.

Return the total number of entries whose value is strictly less than zero. Zero is not negative. The shared row and column ordering creates a monotone boundary between nonnegative and negative cells, so the entire matrix need not be inspected individually.

### Function Contract

**Inputs**

- `grid`: a nonempty $m \times n$ integer matrix whose rows and columns are each sorted in non-increasing order.
- $m$ and $n$ denote its row and column counts.

**Return value**

- Return the number of cells containing a value less than zero.

### Examples

**Example 1**

- Input: `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`
- Output: `8`

**Example 2**

- Input: `grid = [[3,2],[1,0]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,-1],[-1,-1]]`
- Output: `3`

### Required Complexity

- **Time:** $O(m+n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Start where one comparison eliminates a region.** Place a pointer at the bottom-left cell. If that value is negative, every cell to its right in the same row is no larger and is therefore also negative. Add `n - column` to the count and move up one row; that row is completely resolved.

If the current value is nonnegative, every cell above it in the same column is at least as large and cannot be negative. Move right one column, resolving that column for all remaining rows.

Each comparison therefore discards either one row or one column. The pointer never moves down or left, and it stops after leaving the top or right boundary. Every discarded negative suffix is counted exactly once, while every discarded column portion is proven nonnegative, so the accumulated count contains precisely all negative cells.

#### Complexity detail

The pointer moves upward at most $m$ times and rightward at most $n$ times, giving $O(m+n)$ time. The scan stores only coordinates and the running count, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Inspect every cell:** A direct count is simple and correct but requires $O(mn)$ time.
- **Binary search each row:** Finding the first negative entry independently in each row takes $O(m \log n)$ time and does not exploit column ordering as fully.
- **All values nonnegative:** The pointer moves across the bottom row and returns zero.
- **All values negative:** Each visited row contributes all $n$ columns.
- **Zero boundary:** Comparisons must use strict negativity; zero belongs to the nonnegative region.
- **Rectangular matrix:** The same scan works without requiring equal dimensions.

</details>
