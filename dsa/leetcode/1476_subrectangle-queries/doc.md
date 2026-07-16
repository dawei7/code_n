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

### Required Complexity
- **Time:** $O(RC+U+Q)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Making the stored matrix the current source of truth**

Copy the constructor matrix into object-owned storage. This prevents app-local callers from observing or causing aliasing through the input rows. At every moment, `rectangle[r][c]` directly stores the value that a query for coordinate `(r,c)` must return.

Because updates are assignments rather than additions, no previous value is needed once a cell is covered. Writing updates immediately therefore gives point queries the simplest possible implementation: one indexed lookup.

**Applying an inclusive rectangle**

For an update, iterate `row` from `row1` through `row2`. Inside each selected row, iterate `col` from `col1` through `col2` and perform `rectangle[row][col] = newValue`.

Both endpoints are inclusive. The number of assignments is exactly

$$
(\texttt{row2}-\texttt{row1}+1)
(\texttt{col2}-\texttt{col1}+1).
$$

A one-row, one-column, or one-cell rectangle follows from the same loops without special handling.

**Why overlapping updates need no extra machinery**

Suppose a cell belongs to several update rectangles. The operations are processed in chronological order, and each covering update overwrites that cell. Consequently, after any prefix of operations, the stored value equals the value written by the latest covering update in that prefix, or its constructor value if no update covered it. This is exactly the object's required state.

A query performs no reconstruction: the invariant already makes the indexed cell current. Induction over operations proves correctness. Construction establishes the invariant from the initial matrix; an update changes precisely the coordinates specified and leaves every other cell intact; a query reads without changing state.

**Adapting the class to the local runner**

The `solve` adapter creates the class once, then dispatches operations in their given order. It appends `None` after each void update and appends the integer returned by each query, preserving the platform call trace in JSON-compatible form.

#### Complexity detail

Copying the initial matrix costs $O(RC)$. Across all updates, the nested loops perform exactly $U$ cell assignments. Dispatching $Q$ calls and answering each point query adds $O(Q)$ time, for $O(RC+U+Q)$ total.

The object-owned matrix contains $RC$ integers, so total storage is $O(RC)$. Aside from that state and the required output trace, each method uses only loop counters and arguments.

#### Alternatives and edge cases

- **Store updates lazily:** Append every update and answer a query by scanning updates backward for the most recent covering rectangle. This makes updates $O(1)$ but queries $O(k)$ after $k$ updates, which may be preferable only for update-heavy workloads with very few queries.
- **Copy the entire matrix for every update:** Persistent snapshots make historical versions available, but the source asks only for current state; copying all $RC$ cells for a one-cell update wastes time and space.
- **Two-dimensional difference array:** Range increments can be batched efficiently, but these are ordered assignments and queries may occur between updates, so overlapping last-write-wins semantics do not combine through a simple sum.
- **Quadtree or interval structures:** More advanced spatial structures can trade update and query costs, but their complexity is unjustified for dimensions and operation counts at most $100$ and $500$.
- **Single-cell update:** Equal corner coordinates must write exactly that one cell.
- **Whole-matrix update:** Coordinates `(0,0)` through `(R-1,C-1)` overwrite every entry.
- **Overlapping rectangles:** Only cells in the later rectangle change again; earlier values outside it remain current.
- **One-row or one-column matrix:** Inclusive loops work unchanged even when one dimension equals one.
- **Maximum values:** Values up to $10^9$ are stored directly; no arithmetic or overflow-sensitive aggregation is performed.
- **Input ownership:** Copying rows prevents mutations inside the class from unexpectedly changing the caller's original matrix in the app-local environment.

</details>
