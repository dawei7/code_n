# Check if Matrix Is X-Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2319 |
| Difficulty | Easy |
| Topics | Array, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-matrix-is-x-matrix/) |

## Problem Description
### Goal
An $n\times n$ square matrix forms an X when its main diagonal and secondary
diagonal contain only nonzero values. The main diagonal contains coordinates
with equal row and column indices; the secondary diagonal contains coordinates
whose indices sum to $n-1$. In an odd-sized matrix, the center belongs to both
diagonals.

Determine whether `grid` is an X-matrix. Every diagonal entry must be nonzero,
and every cell outside both diagonals must be exactly zero. A violation of
either requirement makes the answer false.

### Function Contract
**Inputs**

- `grid`: An $n\times n$ integer matrix.

The dimension satisfies $3\le n\le100$, and every entry is from $0$ through
$10^5$.

**Return value**

`true` exactly when both diagonals are entirely nonzero and every other entry
is zero.

### Examples
**Example 1**

- Input: `grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]`
- Output: `true`

**Example 2**

- Input: `grid = [[5,7,0],[0,3,1],[0,5,0]]`
- Output: `false`
- Explanation: The matrix contains both misplaced nonzero values and a zero on
  a diagonal.
