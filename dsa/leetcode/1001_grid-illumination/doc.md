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

### Required Complexity

- **Time:** $O(L+Q)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Index every illuminated line:** Maintain counters for active lamps in each row, column, main diagonal `row - col`, and anti-diagonal `row + col`. Also keep a set of active coordinates. Insert a listed lamp only if its coordinate is not already active, preventing duplicates from inflating the counters.

**Answer a query from four counters:** A query cell is illuminated exactly when at least one of its row, column, or two diagonal counters is positive. Record that answer before changing any lamp state, preserving the required query order.

**Remove only the local neighborhood:** Examine the query cell and its eight neighboring coordinates. When one is active, remove it from the set and decrement all four corresponding line counters. There are always only nine candidate shutdown positions, so no grid-sized work is needed. The counters remain equal to the active-lamp incidence on every indexed line, which proves each subsequent answer is accurate.

#### Complexity detail

Deduplicating and indexing the $L$ listed lamps takes $O(L)$ time. Each of the $Q$ queries performs constant-time counter lookups and at most nine set removals, so total time is $O(L+Q)$. The active set and line counters use $O(L)$ space.

#### Alternatives and edge cases

- **Scan every active lamp per query:** Directly testing all rows, columns, and diagonals is correct but takes $O(LQ)$ time when shutdowns remove nothing.
- **Materialize the grid:** The side length can be $10^9$, so an $n\times n$ matrix is infeasible and unnecessary.
- **Duplicate lamp positions:** Count a coordinate once; one shutdown removes that lamp completely.
- **Answer-before-shutdown order:** A lamp in the queried cell illuminates that query before being turned off.
- **Repeated queries:** Their answers may change because earlier queries mutate the active lamp set.

</details>
