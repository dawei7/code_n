# Matrix Block Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1314 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/matrix-block-sum/) |

## Problem Description
### Goal
Given an $m\times n$ integer matrix `mat` and a positive integer `k`, produce an answer matrix with the same dimensions. For each output cell `answer[i][j]`, sum every `mat[r][c]` whose row lies from $i-k$ through $i+k$ and whose column lies from $j-k$ through $j+k$.

Only valid matrix positions contribute. In other words, the square block centered at `(i, j)` is clipped at the top, bottom, left, and right boundaries rather than padded with additional values.

### Function Contract
**Inputs**

- `mat`: an $m\times n$ matrix, where $1\le m,n\le100$.
- Every `mat[i][j]` is between 1 and 100 inclusive.
- `k`: the block radius, where $1\le k\le100$.

**Return value**

An $m\times n$ matrix `answer` satisfying

$$
\texttt{answer[i][j]}
=
\sum_{r=\max(0,i-k)}^{\min(m-1,i+k)}
\sum_{c=\max(0,j-k)}^{\min(n-1,j+k)}
\texttt{mat[r][c]}.
$$

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`
- Output: `[[12,21,16],[27,45,33],[24,39,28]]`

**Example 2**

- Input: the same matrix, `k = 2`
- Output: `[[45,45,45],[45,45,45],[45,45,45]]`

**Example 3**

- Input: `mat = [[5]]`, `k = 1`
- Output: `[[5]]`

### Required Complexity
- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Build a padded two-dimensional prefix table**

Create `prefix` with $m+1$ rows and $n+1$ columns of zeros. Define `prefix[r + 1][c + 1]` as the sum of the rectangle from `mat[0][0]` through `mat[r][c]`. Inclusion-exclusion gives the update from the cell value, the prefix above, and the prefix to the left, subtracting the overlap counted twice.

**Answer each clipped rectangle with four lookups**

For output position `(i, j)`, convert the clipped inclusive bounds to half-open bounds `[top, bottom)` and `[left, right)`. Its block sum is

`prefix[bottom][right] - prefix[top][right] - prefix[bottom][left] + prefix[top][left]`.

The full prefix at `bottom, right` contains the desired rectangle plus cells above and left. Subtracting those two outside strips removes them, while their shared corner was removed twice and must be added back. This leaves exactly the valid cells within $k$ rows and columns of the center. Applying the formula independently to every cell produces the required matrix.

#### Complexity detail

Constructing the prefix table visits all $mn$ cells. Each of the $mn$ answers uses constant-time bound calculations and four prefix lookups, so total time is $O(mn)$. The prefix and answer matrices each occupy $O(mn)$ space.

#### Alternatives and edge cases

- **Direct neighborhood enumeration:** Iterating through every cell in every clipped block is correct but can take $O(mn(2k+1)^2)$ time.
- **Two one-dimensional sliding passes:** Horizontal window sums followed by vertical window sums also achieve $O(mn)$ time, but require careful changing boundary widths.
- **Radius covers the matrix:** Every answer equals the complete matrix sum when the clipped block includes all rows and columns.
- **Corner cells:** Both row and column ranges clip on one side, which the half-open bounds handle uniformly.
- **Rectangular matrices:** Row and column limits are calculated separately; no square-shape assumption is valid.
- **Single cell:** Any legal positive radius still returns that one value.

</details>
