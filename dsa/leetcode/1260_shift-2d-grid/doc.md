# Shift 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1260 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shift-2d-grid/) |

## Problem Description

### Goal

You are given an $m \times n$ integer `grid`. One shift moves every element one position forward in row-major order: a cell moves to the next column, the final cell of a row moves to the first column of the following row, and the bottom-right cell wraps to the top-left cell.

Apply this operation `k` times and return the resulting two-dimensional grid with the same dimensions. Values are moved rather than changed, and shifts wrap around the complete matrix rather than wrapping independently within each row.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ integer matrix, where $1 \le m,n \le 50$.
- `k`: the number of shifts, with $0 \le k \le 100$.
- Let $N=mn$ be the number of grid cells.

**Return value**

- Return the matrix after `k` cyclic row-major shifts.

### Examples

**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[9,1,2],[3,4,5],[6,7,8]]`

**Example 2**

- Input: `grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]`, `k = 4`
- Output: `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]`

**Example 3**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 9`
- Output: `[[1,2,3],[4,5,6],[7,8,9]]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

View the matrix in row-major order as one cyclic array of length $N$. Cell `(r, c)` corresponds to flat index `r * n + c`, and one grid shift is exactly a right rotation of this flat array by one position.

**Collapse all shifts into one rotation**

After `k` shifts, an element moves `k` positions around the same cycle. Reduce `k` with `k %= N`; complete cycles make no change. Flatten the grid once, then form the right rotation by concatenating `flat[-k:]` with `flat[:-k]`. When the reduced shift is zero, retain the flat sequence unchanged.

**Restore the original shape**

Split the rotated sequence into $m$ consecutive slices of length $n$. Row-major flattening and the inverse slicing preserve exactly the transition rules between columns, rows, and the final wrap. Every input element appears once, at flat position `(old_index + k) % N`, so the result is the requested shift.

#### Complexity detail

Flattening, rotating, and reshaping each process $N$ values, for $O(N)$ time. The flattened sequence and returned grid contain $O(N)$ values, so auxiliary and output space are $O(N)$.

#### Alternatives and edge cases

- **Simulate one shift at a time:** Rebuilding or moving the matrix for every operation costs $O(kN)$ time.
- **Direct destination mapping:** Allocate the result and place each value at `(index + k) % N`; it has the same $O(N)$ bounds without an explicit rotated flat list.
- **Shift by zero:** Return an equal-shaped copy with the same values.
- **Whole cycles:** When `k` is divisible by $N$, the grid is unchanged.
- **Single row or column:** The same flat cyclic rotation handles both shapes without special cases.
- **Negative values:** Values are opaque payloads and do not affect index calculations.

</details>
