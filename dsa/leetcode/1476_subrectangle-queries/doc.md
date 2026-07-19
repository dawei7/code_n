# Subrectangle Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1476 |
| Difficulty | Medium |
| Topics | Array, Design, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/subrectangle-queries/) |

## Problem Description
### Goal

Implement `SubrectangleQueries` for a rectangular integer matrix. The object must support inclusive subrectangle updates: given a top-left coordinate `(row1, col1)`, a bottom-right coordinate `(row2, col2)`, and `newValue`, replace every cell whose row lies from `row1` through `row2` and whose column lies from `col1` through `col2`.

It must also answer point queries by returning the matrix's current value at `(row, col)`. Updates are cumulative and ordered: when subrectangles overlap, the most recent update determines the cells in their intersection while cells outside the newer rectangle retain their previous values.

### Function Contract
**Platform interface**

Let $R$ and $C$ be the matrix dimensions, $Q$ the number of method calls, and $U$ the total number of cell positions covered across all update calls, counted once per call that covers them.

- `SubrectangleQueries(rectangle)` initializes the object from an $R\times C$ matrix, where $1 \le R,C \le 100$.
- `updateSubrectangle(row1, col1, row2, col2, newValue)` assigns `newValue` to every cell in the inclusive coordinate product $[\texttt{row1},\texttt{row2}]\times[\texttt{col1},\texttt{col2}]$ and returns nothing.
- `getValue(row, col)` returns the current integer stored at that valid coordinate.
- Rectangle entries and update values lie in $[1,10^9]$, and at most $500$ update and query calls occur in total.

**App-local adapter**

- `rectangle`: the initial matrix.
- `operations`: an ordered array of `[name, arguments]` entries using `"updateSubrectangle"` or `"getValue"`.
- Return one output per operation: `null` for an update and the queried integer for `getValue`.

### Examples
**Example 1**

- Input: `rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]], operations = [["getValue",[0,2]],["updateSubrectangle",[0,0,3,2,5]],["getValue",[0,2]],["getValue",[3,1]],["updateSubrectangle",[3,0,3,2,10]],["getValue",[3,1]],["getValue",[0,2]]]`
- Output: `[1,null,5,5,null,10,5]`
- Explanation: The first update fills the entire matrix with `5`; the second changes only the last row to `10`.

**Example 2**

- Input: `rectangle = [[1,1,1],[2,2,2],[3,3,3]], operations = [["getValue",[0,0]],["updateSubrectangle",[0,0,2,2,100]],["getValue",[0,0]],["getValue",[2,2]],["updateSubrectangle",[1,1,2,2,20]],["getValue",[2,2]]]`
- Output: `[1,null,100,100,null,20]`
- Explanation: The lower-right update overwrites only its overlap with the earlier whole-matrix update.

**Example 3**

- Input: `rectangle = [[3]], operations = [["getValue",[0,0]],["updateSubrectangle",[0,0,0,0,9]],["getValue",[0,0]]]`
- Output: `[3,null,9]`
