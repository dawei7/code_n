# Number of Ways to Paint N × 3 Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1411 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) |

## Problem Description

### Goal

Consider a grid with $n$ rows and exactly three columns. Paint every cell using one of three colors. A valid painting must give different colors to every pair of cells that share a horizontal or vertical side, so the restriction applies both within each row and between consecutive rows.

Count all valid paintings of the entire grid. Because the count grows quickly, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: the number of grid rows, where $1 \le n \le 5000$.

**Return value**

- The number of valid paintings of the $n \times 3$ grid, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `12`

**Example 2**

- Input: `n = 2`
- Output: `54`

**Example 3**

- Input: `n = 3`
- Output: `246`
