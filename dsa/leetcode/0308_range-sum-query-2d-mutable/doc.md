# Range Sum Query 2D - Mutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 308 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Design, Binary Indexed Tree, Segment Tree, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

## Problem Description
### Goal
Construct a mutable range-sum structure from a nonempty rectangular integer matrix. `update(row, column, value)` assigns a new value to one cell, and `sumRegion(row1, col1, row2, col2)` queries the current matrix after all earlier updates.

Return each rectangle's sum including both corner rows and columns, with update calls producing no output. Updates replace rather than add to the old cell value. Support an interleaved operation sequence efficiently without rebuilding all prefix information or scanning every queried cell. The app collects query results in order, while the native `NumMatrix` persists the changing matrix across method calls.

### Function Contract
**Inputs**

- `matrix`: the initial nonempty rectangular integer matrix
- `operations`: ordered commands `["update", row, column, value]` or `["sum", row1, col1, row2, col2]`

**Return value**

The result of every `sum` command in operation order. Updates produce no output.

### Examples
**Example 1**

- Input: the standard 5×5 matrix, then `sum(2,1,4,3)`, `update(3,2,2)`, `sum(2,1,4,3)`
- Output: `[8,10]`

**Example 2**

- Input: `matrix = [[5]], operations = [["sum",0,0,0,0],["update",0,0,-2],["sum",0,0,0,0]]`
- Output: `[5,-2]`

**Example 3**

- Input: `matrix = [[1,2],[3,4]], operations = [["sum",0,0,1,1],["update",0,1,5],["sum",0,1,1,1]]`
- Output: `[10,9]`

### Required Complexity

- **Time:** $O((mn + q) \log m \log n)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**A two-dimensional Fenwick entry owns a power-of-two rectangle**

Use one-based row and column indices. Entry `tree[r][c]` represents a rectangle ending at `(r,c)` whose height is $r \mathbin{\&} - r$ and width is $c \mathbin{\&} - c$. Following both low-bit parent directions tiles the prefix rectangle from the origin through a requested cell.

A prefix query nests the usual Fenwick walks: subtract the row low bit in the outer loop and the column low bit in the inner loop, accumulating the disjoint stored rectangles. Any requested subrectangle is then obtained from four prefix sums by two-dimensional inclusion–exclusion.

**Point assignment propagates one delta through both dimensions**

Retain the current matrix values because `update` assigns rather than increments. Compute `delta = new_value - old_value`, replace the stored value, and add that delta to every Fenwick rectangle containing the cell. These rectangles are reached by repeatedly adding the row low bit and, for each row ancestor, repeatedly adding the column low bit.

For the standard sample, the rectangle `(2,1)..(4,3)` initially sums to eight. Changing cell `(3,2)` from zero to two propagates delta two to every covering Fenwick rectangle, and the same query then returns ten.

**Stored rectangles remain exact after every operation**

Construction adds every cell to precisely its row and column ancestors, establishing the defined rectangle sum at each Fenwick entry. A point update changes only rectangles containing that point and adjusts each by the exact delta, so the representation remains valid.

Each prefix walk decomposes its target area into nonoverlapping Fenwick rectangles, counting every prefix cell once. Applying inclusion–exclusion to four exact prefixes cancels cells above or left of the requested rectangle and restores their doubly removed overlap. Thus every reported sum is correct after any update sequence.

#### Complexity detail

The straightforward construction performs one $O(\log m \log n)$ Fenwick addition per cell, taking $O(mn \log m \log n)$. Each update and rectangle query also takes $O(\log m \log n)$, so `q` operations give the stated $O((mn + q) \log m \log n)$ bound. Current values and the tree use $O(mn)$ space.

#### Alternatives and edge cases

- **Mutate the matrix and rescan each rectangle:** gives constant-time updates but up to $O(mn)$ per query.
- **Rebuild a 2D prefix table after every update:** gives constant-time queries but $O(mn)$ assignments.
- **2D segment tree:** can provide comparable polylogarithmic operations with more complex storage and traversal.
- Single-cell, single-row, and full-matrix rectangles all use the same four-prefix formula. Reassigning a cell to its existing value propagates a zero delta.

</details>
