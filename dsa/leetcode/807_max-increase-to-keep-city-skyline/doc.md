# Max Increase to Keep City Skyline

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 807 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) |

## Problem Description

### Goal

An $n \times n$ city grid contains one building per block, and `grid[r][c]` is its height. The skyline viewed from the north or south is determined by column maxima, while the skyline from the east or west is determined by row maxima.

Increase any building heights by non-negative amounts without changing any of those four directional skylines. Return the maximum total increase summed across all buildings. A building may rise only as high as both its original row maximum and its original column maximum permit.

### Function Contract

**Inputs**

- `grid`: a nonempty square matrix of nonnegative building heights.

**Return value**

- The maximum sum of all height increases that preserves every row and column skyline.

### Examples

**Example 1**

- Input: `grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]`
- Output: `35`
- Explanation: Each building can rise to the smaller of its row maximum and column maximum; the resulting increases sum to 35.

**Example 2**

- Input: `grid = [[1,2],[3,4]]`
- Output: `1`
- Explanation: Only the upper-left building can rise, from 1 to 2.

**Example 3**

- Input: `grid = [[5]]`
- Output: `0`
- Explanation: Increasing the only building would change both skylines.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Capture the original skyline limits**

Compute the maximum height of every row and every column before changing anything. A building at `(row, col)` cannot exceed either of those two maxima: exceeding the row maximum changes the skyline from one viewing direction, and exceeding the column maximum changes it from the perpendicular direction.

**Raise each cell to its tightest limit**

The greatest legal height at `(row, col)` is therefore `min(row_max[row], column_max[col])`. Add the difference between this bound and the current height for every cell.

This bound is legal because it never exceeds either original skyline limit. Each original row maximum remains present at its original cell, whose bound cannot be below its current height, and the same holds for every column maximum. Thus all skylines stay unchanged. No cell can be raised higher without violating at least one skyline, so independently taking every bound maximizes the total increase.

#### Complexity detail

For an `n` by `n` grid, computing maxima and summing increases each scans $n^{2}$ cells, taking $O(n^2)$ time. The row and column maximum arrays use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Transpose for column maxima:** `zip(*grid)` can expose columns compactly; it has the same asymptotic work but may allocate tuple views.
- **Recompute maxima per cell:** Scanning an entire row and column for every building is correct but takes $O(n^3)$ time.
- **Materialize the raised grid:** Building the final matrix is unnecessary when only the total increase is requested and uses $O(n^2)$ extra space.
- **Single cell:** Its row and column limits equal its height, so the increase is zero.
- **Uniform grid:** Every cell already equals both skyline limits.
- **Zero heights:** They may rise only when both their row and column have taller buildings.
- **Tied maxima:** Multiple buildings may preserve the same skyline; the cellwise bound remains unchanged.

</details>
