# Right Triangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3128 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Combinatorics, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/right-triangles/) |

## Problem Description

### Goal

You are given a two-dimensional boolean matrix `grid`. Choose three cells whose values are all `1`. They form a right triangle when one of the chosen cells shares its row with a second chosen cell and shares its column with the third chosen cell.

The three cells do not need to be adjacent. Count every distinct collection of three `1` cells that satisfies this row-and-column relationship, and return the total number of such right triangles.

### Function Contract

Let $m$ be the number of rows and $n$ the number of columns.

**Inputs**

- `grid`: An $m\times n$ matrix whose entries are either `0` or `1`, where $1\le m,n\le1000$.

**Return value**

Return the number of distinct right triangles whose three selected cells all contain `1`.

### Examples

#### Example 1

- **Input:** `grid = [[0,1,0],[0,1,1],[0,1,0]]`
- **Output:** `2`
- **Explanation:** The middle-right `1` can be paired with either of the other two `1` cells in its column, producing two triangles.

#### Example 2

- **Input:** `grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]`
- **Output:** `0`
- **Explanation:** No `1` has both another `1` in its row and another `1` in its column.

#### Example 3

- **Input:** `grid = [[1,0,1],[1,0,0],[1,0,0]]`
- **Output:** `2`
- **Explanation:** The upper-left `1` can use the upper-right cell together with either lower `1` in the first column.
