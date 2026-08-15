# Cells in a Range on an Excel Sheet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2194 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/) |

## Problem Description

### Goal

Each spreadsheet cell is named by one uppercase column letter followed by one
row digit. The range string `s` has the form `"C1R1:C2R2"` in positional
terms: its first cell supplies the smallest included column and row, while its
second cell supplies the greatest included column and row.

List every cell inside this inclusive rectangular range. Order the result
first by non-decreasing column and, within each column, by non-decreasing row.
Each returned item must retain the same column-letter-plus-row-digit format.

### Function Contract

**Inputs**

- `s`: a five-character range `"C1R1:C2R2"` whose columns lie from `A` to
  `Z`, rows lie from `1` to `9`, and both endpoints are non-decreasing.

If the range spans $w$ columns and $h$ rows, define its cell count as
$A=wh$.

**Return value**

Return all $A$ cell names in column-major, then row-major, order.

### Examples

#### Example 1

- **Input:** `s = "K1:L2"`
- **Output:** `["K1","K2","L1","L2"]`

#### Example 2

- **Input:** `s = "A1:F1"`
- **Output:** `["A1","B1","C1","D1","E1","F1"]`

#### Example 3

- **Input:** `s = "Z9:Z9"`
- **Output:** `["Z9"]`
