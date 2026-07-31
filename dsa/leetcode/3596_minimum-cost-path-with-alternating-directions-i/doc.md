# Minimum Cost Path with Alternating Directions I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3596 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/) |

## Problem Description
### Goal
Consider an `m`-by-`n` grid whose rows and columns are zero-indexed. Entering cell `(i, j)` costs `(i + 1) * (j + 1)`. A path starts at `(0, 0)`, includes that cell's entrance cost, and aims to reach the bottom-right cell `(m - 1, n - 1)`.

Movement directions alternate. On the first, third, and every subsequent odd-numbered transition, move to an adjacent cell either right or down. On each even-numbered transition, move to an adjacent cell either left or up. Every move must remain inside the grid. Return the least possible sum of entrance costs along a valid path to the destination, or `-1` when the alternating rules make the destination unreachable.

### Function Contract
**Inputs**

- `m`: the number of grid rows
- `n`: the number of grid columns

Both dimensions satisfy $1 \le m, n \le 10^6$.

**Return value**

The minimum total entrance cost of a valid alternating-direction path from `(0, 0)` to `(m - 1, n - 1)`, or `-1` if no such path exists.

### Examples
**Example 1**

- Input: `m = 1, n = 1`
- Output: `1`

The starting cell is already the destination, and its entrance cost is `1`.

**Example 2**

- Input: `m = 2, n = 1`
- Output: `3`

Enter `(0, 0)` for cost `1`, then move down once and enter `(1, 0)` for cost `2`.

**Example 3**

- Input: `m = 2, n = 2`
- Output: `-1`

After the first right or down transition, the required left or up transition returns to `(0, 0)`, so the opposite corner cannot be reached.
