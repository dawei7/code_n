# Select Cells in Grid With Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3276 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Select Cells in Grid With Maximum Score](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/) |

## Problem Description

### Goal

A rectangular matrix contains only positive integers. Select at least one of its cells, subject to two restrictions: no row may contribute more than one selected cell, and no numeric value may occur more than once among all selected cells. Cells from different rows may therefore conflict when they hold the same value.

The score of a valid selection is the sum of its selected values. Return the greatest score attainable under both restrictions. A row may be left unused when choosing any of its values would block a more valuable combination elsewhere.

### Function Contract

**Inputs**

- `grid`: A rectangular matrix of positive integers.

Let $m$ be the number of rows and $n$ the number of columns. Both satisfy $1 \le m,n \le 10$, and every cell value lies from $1$ through $100$. Let $V=100$ denote the value-domain bound.

**Return value**

Return the maximum sum of one or more selected cells such that selected rows and selected values are both unique.

### Examples

#### Example 1

- **Input:** `grid = [[1, 2, 3], [4, 3, 2], [1, 1, 1]]`
- **Output:** `8`
- **Explanation:** Values `3`, `4`, and `1` can be taken from three different rows.

#### Example 2

- **Input:** `grid = [[8, 7, 6], [8, 3, 2]]`
- **Output:** `15`
- **Explanation:** Choose `7` from the first row and `8` from the second.

#### Example 3

- **Input:** `grid = [[7, 7], [7], [7, 7, 7]]`
- **Output:** `7`
- **Explanation:** Repeated occurrences of the same value cannot all be selected.
