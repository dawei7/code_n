# Reshape the Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 566 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/reshape-the-matrix/) |

## Problem Description
### Goal
Given an $m \times n$ matrix `mat` and two requested dimensions `r` and `c`, reshape the matrix into `r` rows and `c` columns when that shape can hold exactly the same number of elements. Read the original matrix in row-traversing order and place the values into the new matrix in that same order.

Return the reshaped matrix when $m \cdot n$ equals $r \cdot c$. If the requested dimensions would lose elements or require additional ones, reshaping is impossible and you must return the original matrix unchanged.

### Function Contract
**Inputs**

- `mat`: a non-empty rectangular integer matrix
- `r`: the requested row count
- `c`: the requested column count

**Return value**

- The row-major reshaped matrix, or the original matrix when reshaping is impossible

### Examples
**Example 1**

- Input: `mat = [[1, 2], [3, 4]], r = 1, c = 4`
- Output: `[[1, 2, 3, 4]]`

**Example 2**

- Input: `mat = [[1, 2], [3, 4]], r = 2, c = 4`
- Output: `[[1, 2], [3, 4]]`

**Example 3**

- Input: `mat = [[1, 2, 3, 4]], r = 2, c = 2`
- Output: `[[1, 2], [3, 4]]`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(rc)$

<details>
<summary>Approach</summary>

#### General

**Check the cell counts first**

An `m × n` matrix contains `m n` elements. Reshaping is possible only when that equals `r c`; otherwise no arrangement can fill the requested rectangle without losing or inventing values.

**Preserve one row-major sequence**

When the counts match, visit source rows from top to bottom and columns from left to right. Append each value to the current output row, starting a new row whenever it reaches length `c`.

**Use the same flat position in both shapes**

Equivalently, a flat index `p` refers to source coordinates `(p // n, p % n)` and target coordinates `(p // c, p % c)`. Sequential construction implements this mapping without changing element order.

**Why the result is the required reshape**

Every source cell has one distinct flat index from zero through `mn - 1`. Equal cell counts give the same complete index range to the target. Placing each value at the target coordinates of its unchanged flat index is a bijection and preserves row-major order exactly.

#### Complexity detail

The valid case reads and writes all $m n = r c$ elements once, taking $O(mn)$ time. The returned matrix occupies $O(rc)$ space. An invalid shape is detected in constant time and returns the original object.

#### Alternatives and edge cases

- **Flat list then slice:** is also linear and concise, but temporarily stores another complete copy of the values.
- **Rescan from the beginning for every target cell:** is correct but repeats prefix work and takes $O((mn)^2)$ time.
- **Invalid dimensions:** return the original matrix rather than a partial result.
- **Same shape:** produces the same row-major values and may be returned unchanged or copied.
- **One row:** all values appear in their original row-major sequence.
- **One column:** each row-major value becomes its own output row.
- **Negative values:** are moved exactly like any other matrix entry.

</details>
