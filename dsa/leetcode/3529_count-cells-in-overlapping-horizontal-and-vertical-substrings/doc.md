# Count Cells in Overlapping Horizontal and Vertical Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3529 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Rolling Hash, String Matching, Matrix, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/) |

## Problem Description

### Goal

You are given an $m \times n$ character matrix `grid` and a string `pattern`. A horizontal substring reads cells from left to right. On reaching the end of a row, it continues at the first cell of the next row; it cannot continue past the final row. A vertical substring reads from top to bottom and, after the bottom of a column, continues at the top of the next column; it cannot continue past the final column.

Count the cells that belong to at least one horizontal occurrence of `pattern` and also belong to at least one vertical occurrence of `pattern`. The two occurrences need not start or end at the same cell, and overlapping occurrences in either reading order are allowed. Each qualifying cell contributes once.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix of lowercase English letters.
- `pattern`: A non-empty lowercase string to match in both reading orders.

The dimensions satisfy $1 \le m,n \le 1000$ and $1 \le mn \le 10^5$. The pattern length is between $1$ and $mn$.

**Return value**

- The number of grid cells covered by at least one matching substring in each orientation.

### Examples

#### Example 1

- **Input:** `grid = [["a", "a", "c", "c"], ["b", "b", "b", "c"], ["a", "a", "b", "a"], ["c", "a", "a", "c"], ["a", "a", "b", "a"]], pattern = "abaca"`
- **Output:** `1`

#### Example 2

- **Input:** `grid = [["c", "a", "a", "a"], ["a", "a", "b", "a"], ["b", "b", "a", "a"], ["a", "a", "b", "a"]], pattern = "aba"`
- **Output:** `4`

#### Example 3

- **Input:** `grid = [["a"]], pattern = "a"`
- **Output:** `1`
