# Grid Illumination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1001 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/grid-illumination/) |

## Problem Description

### Goal

An $n\times n$ grid initially has every lamp turned off. Each position `[row, col]` in `lamps` turns on that cell's lamp; listing the same position more than once still represents only one active lamp. An active lamp illuminates its own cell and every cell sharing its row, column, or either diagonal.

For each query, first report whether its cell is currently illuminated. Then turn off any active lamp in the queried cell and in its eight side-or-corner adjacent cells, when those positions exist. Return the query answers in order, using `1` for illuminated and `0` for unilluminated.

### Function Contract

**Inputs**

- `n`: the grid side length, where $1\le\texttt{n}\le10^9$.
- `lamps`: a list of $L$ valid grid coordinates, where $0\le L\le2\cdot10^4$; duplicate coordinates are allowed.
- `queries`: a list of $Q$ valid grid coordinates, where $0\le Q\le2\cdot10^4$.

**Return value**

- A length-$Q$ list whose $j$th value is `1` if the $j$th query cell was illuminated before its shutdown step, and `0` otherwise.

### Examples

**Example 1**

- Input: `n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 0]]`
- Output: `[1, 0]`

**Example 2**

- Input: `n = 5, lamps = [[0, 0], [4, 4]], queries = [[1, 1], [1, 1]]`
- Output: `[1, 1]`
- Explanation: The first shutdown removes the lamp at `[0, 0]`, but the other diagonal lamp still illuminates the repeated query.

**Example 3**

- Input: `n = 5, lamps = [[0, 0], [0, 4]], queries = [[0, 4], [0, 1], [1, 4]]`
- Output: `[1, 1, 0]`
