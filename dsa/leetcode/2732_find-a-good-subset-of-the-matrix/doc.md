# Find a Good Subset of the Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2732 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/) |

## Problem Description

### Goal

Given a binary matrix, choose a nonempty subset of its rows. If the subset contains $k$ rows, it is good when every column contains at most $\lfloor k/2\rfloor$ ones among those rows.

Return the selected row indices in ascending order. Any good subset is acceptable when several exist. Return an empty array if no good subset can be formed; selecting no rows is not itself a good subset.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ binary matrix with $1 \le m \le 10^4$, $1 \le n \le 5$, and every entry equal to `0` or `1`.

**Return value**

Return ascending indices of any nonempty good row subset, or `[]` when none exists.

### Examples

**Example 1**

- Input: `grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]`
- Output: `[0,1]`
- Explanation: Across rows zero and one, every column has at most one `1`, which equals $\lfloor2/2\rfloor$.

**Example 2**

- Input: `grid = [[0]]`
- Output: `[0]`
- Explanation: The only column sum is zero, satisfying the bound $\lfloor1/2\rfloor=0$.

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1]]`
- Output: `[]`
- Explanation: Neither row is all zero, and the two rows share a `1` in every column.
