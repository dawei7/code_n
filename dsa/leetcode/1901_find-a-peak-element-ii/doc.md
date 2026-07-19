# Find a Peak Element II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1901 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/) |

## Problem Description

### Goal

Given an $m \times n$ integer matrix `mat`, find any cell whose value is strictly greater than each orthogonally adjacent cell: above, below, left, and right. Diagonal cells are not neighbors. The matrix has no equal values in horizontally or vertically adjacent cells.

Treat every position just outside the matrix boundary as having value $-1$. Return the zero-based row and column of any qualifying peak. The solution must exploit the matrix structure rather than inspect every cell, running in $O(m\log n)$ or $O(n\log m)$ time.

### Function Contract

**Inputs**

- `mat`: a nonempty rectangular matrix with $m$ rows and $n$ columns, where $1 \le m,n \le 500$.
- Every entry is an integer from $1$ through $10^5$.
- No two cells sharing an edge have equal values.

**Return value**

Return `[row, column]` for any cell strictly larger than all of its existing orthogonal neighbors.

### Examples

**Example 1**

- Input: `mat = [[1, 4], [3, 2]]`
- Output: `[0, 1]`
- Explanation: Both `[0, 1]` and `[1, 0]` are valid peaks, so either answer is accepted.

**Example 2**

- Input: `mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]`
- Output: `[1, 1]`
- Explanation: The values `30` and `32` are both peaks.

**Example 3**

- Input: `mat = [[7]]`
- Output: `[0, 0]`

### Required Complexity

- **Time:** $O(m\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Choose a column maximum.** Binary-search the column range. In the middle column, scan all $m$ rows and select a row containing that column's maximum. Because vertically adjacent values are unequal, this cell is strictly larger than its existing upper and lower neighbors.

**Follow a larger horizontal neighbor.** Compare the selected value with the cells immediately left and right, using $-1$ beyond a boundary. If it exceeds both, it is also horizontally dominant and therefore is a peak. If the right neighbor is larger, discard the middle column and everything left of it; repeatedly moving toward larger values on that side must eventually reach a peak. Otherwise the left neighbor is larger, and the symmetric argument permits discarding the middle and right side.

Each decision preserves at least one peak in the retained columns. The interval shrinks by half, and selecting a column maximum guarantees that the returned coordinate satisfies all four strict comparisons.

#### Complexity detail

Let $m$ and $n$ be the row and column counts. Each of $O(\log n)$ binary-search iterations scans one full column in $O(m)$ time, for $O(m\log n)$ total time. Only indices and neighboring values are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Scan every cell:** Checking all four neighbors finds a valid peak but costs $O(mn)$ time and violates the requested bound.
- **Binary-search rows:** The transposed method scans a row maximum per iteration and runs in $O(n\log m)$ time.
- **Multiple peaks:** Any valid coordinate is correct; output must be validated semantically rather than against one fixed reference coordinate.
- **Single cell:** With only the $-1$ perimeter as neighbors, `[0, 0]` is a peak.
- **Single row or column:** The same search reduces to the ordinary one-dimensional peak argument.
- **Strictness guarantee:** Adjacent inequality prevents a column maximum from tying its vertical neighbor and avoids plateaus during directional reasoning.

</details>
