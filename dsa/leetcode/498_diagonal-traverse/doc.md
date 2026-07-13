# Diagonal Traverse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 498 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/diagonal-traverse/) |

## Problem Description
### Goal
Given a nonempty $m \times n$ matrix `mat`, traverse diagonals whose cells share the same row-plus-column index, beginning at the top-left cell. Visit the first diagonal upward-right, reverse direction at a boundary, then alternate downward-left and upward-right for successive diagonals.

Return all $m \cdot n$ elements in that diagonal order, including each cell exactly once. Rectangular matrices, single rows, and single columns must follow the same boundary transitions. The function returns element values rather than coordinates and may not skip or repeat a boundary cell when changing direction.

### Function Contract
**Inputs**

- `mat`: a nonempty rectangular integer matrix

**Return value**

- All matrix values in the required alternating diagonal order

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,2,4,7,5,3,6,8,9]`

**Example 2**

- Input: `mat = [[1,2],[3,4]]`
- Output: `[1,2,3,4]`

**Example 3**

- Input: `mat = [[1,2,3]]`
- Output: `[1,2,3]`

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(rows \cdot cols)$

<details>
<summary>Approach</summary>

#### General

**Group cells by coordinate sum**

Every cell on one top-right-to-bottom-left diagonal has the same `row + col`. The possible sums run from zero through `rows + cols - 2`, which fixes the order in which diagonals appear.

**Enumerate one diagonal without scanning the matrix**

For a sum `d`, start at row `max(0, d - cols + 1)` and column `d - row`. Increase the row and decrease the column until leaving the matrix. This visits exactly the cells of that diagonal.

**Reverse alternating diagonals**

The direct enumeration moves downward-left. Odd-numbered diagonals keep that order, while even-numbered diagonals are reversed to move upward-right. Append each oriented diagonal to the answer.

**Why every cell appears once**

Each matrix coordinate has one unique sum and is therefore assigned to exactly one diagonal. The bounded row-and-column walk reaches every coordinate with that sum once, and parity changes only its order, not its membership.

#### Complexity detail

Every matrix cell is collected and appended once, giving $O(rows \cdot cols)$ time. The returned list and the largest temporary diagonal together use $O(rows \cdot cols)$ space, with $O(\min(rows, cols))$ auxiliary storage beyond the output.

#### Alternatives and edge cases

- **Direction simulation:** move a cursor upward-right or downward-left and change direction at boundaries with the same linear bounds.
- **Scan all cells for every diagonal:** is correct but takes $O(rows \cdot cols \cdot (rows + cols))$ time.
- **Map sums to lists:** simplifies grouping but stores all cells in an additional dictionary of diagonals.
- **Single row:** returns left-to-right order.
- **Single column:** returns top-to-bottom order.
- **Rectangular matrix:** diagonal lengths grow only to the shorter dimension, then shrink.
- **Parity:** diagonal zero is traversed in the upward-right orientation, though it contains one cell.

</details>
