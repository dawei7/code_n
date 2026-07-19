# Design Excel Sum Formula

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 631 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Graph Theory, Design, Topological Sort, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/design-excel-sum-formula/) |

## Problem Description
### Goal
Design a spreadsheet with rows `1` through `height` and columns `A` through `width`, initially filled with zeroes. Support `set(row, column, value)` for replacing a cell with a literal integer, `get(row, column)` for reading its current value, and `sum(row, column, references)` for assigning a sum formula and returning its value.

A formula may reference individual cells and inclusive rectangular ranges, and repeated or overlapping references contribute with their full multiplicity. Formulas remain active: changing a referenced cell must update every dependent formula value. Assigning a literal or a new formula replaces the target cell's previous contents and dependency behavior.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `Excel`, followed by `set`, `get`, or `sum` calls
- `arguments`: the matching constructor dimensions, cell coordinates and values, or formula reference lists
- `Excel(height, width)`: create rows `1` through `height` and columns `A` through `width`, initially filled with zeroes
- `set(row, column, value)`: replace the target cell, including any previous formula, with a literal value
- `get(row, column)`: read the target cell's current value
- `sum(row, column, references)`: replace the target with a formula, then return its current value; each reference is a cell such as `A1` or an inclusive range such as `A1:C3`

**Return value**

- The operation trace returns null for construction and `set`, and returns the requested integer for `get` and `sum`
- Repeated or overlapping references contribute with their full multiplicity

### Examples
**Example 1**

- Input: construct a `3` by `A:C` sheet; set `A1 = 2`; set `C3` to `SUM(A1, A1:B2)`; then set `B2 = 2` and get `C3`
- Output: `null, null, 4, null, 6`

**Example 2**

- Input: construct a `2` by `A:B` sheet; get `A1`; set `A1 = 5`; get `A1`
- Output: `null, 0, null, 5`

**Example 3**

- Input: set `A1 = 2`, define `B1 = SUM(A1)`, define `C1 = SUM(A1:B1)`, then change `A1` to `3` and get `C1`
- Output: the final value is `6`
