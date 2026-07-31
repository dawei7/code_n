# Matrix Similarity After Cyclic Shifts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2946 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/) |

## Problem Description
### Goal
You are given an $R\times C$ integer matrix `mat` with 0-indexed rows and a
positive integer `k`. Repeat the following process `k` times: cyclically
shift every even-indexed row one position to the left and every odd-indexed row
one position to the right. A cyclic shift moves the element leaving one end
back to the other end.

Return `True` exactly when the matrix obtained after all `k` steps is
identical, entry for entry, to the original matrix. Otherwise return `False`.

### Function Contract
**Inputs**

- `mat`: the rectangular integer matrix
- `k`: the number of alternating-direction cyclic-shift steps

Let $R=\lvert\texttt{mat}\rvert$ and
$C=\lvert\texttt{mat[0]}\rvert$. The contract guarantees
$1\le R,C\le25$, $1\le\texttt{mat[i][j]}\le25$, and $1\le k\le50$.

**Return value**

A boolean indicating whether the shifted matrix equals `mat`.

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4`
- Output: `False`
- Explanation: Four steps are equivalent to one position modulo three, and
  the rows are not invariant under that shift.

**Example 2**

- Input: `mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2`
- Output: `True`
- Explanation: Each row repeats with a period compatible with a two-position
  shift.

**Example 3**

- Input: `mat = [[2,2],[2,2]], k = 3`
- Output: `True`
- Explanation: Every row is constant, so no cyclic shift changes it.
