# Maximum Non Negative Product in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1594 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/) |

## Problem Description
### Goal
You are given an $m \times n$ integer matrix `grid`. Begin at its top-left cell `(0, 0)`. Each move must go exactly one cell to the right or one cell down, and the path must finish at the bottom-right cell `(m - 1, n - 1)`. A path's product is obtained by multiplying every cell value visited, including both endpoints.

Among all such paths, find the greatest product that is non-negative. If every path product is negative, return `-1`. Otherwise, return the chosen product modulo $10^9 + 7$. The comparison must use the complete products: applying the modulus before selecting the maximum can change their ordering and is not valid.

### Function Contract
**Inputs**

- `grid`: an $m \times n$ matrix with $1 \le m,n \le 15$ and $-4 \le \texttt{grid[i][j]} \le 4$.

**Return value**

Return the maximum non-negative top-left-to-bottom-right path product modulo $10^9 + 7$, or `-1` if no path has a non-negative product.

### Examples
**Example 1**

- Input: `grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]`
- Output: `-1`

**Example 2**

- Input: `grid = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]`
- Output: `8`
- Explanation: One maximizing path has product `1 * 1 * -2 * -4 * 1 = 8`.

**Example 3**

- Input: `grid = [[1, 3], [0, -4]]`
- Output: `0`

### Required Complexity
- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**One extreme is insufficient.** A positive cell preserves product order, but a negative cell reverses it: the smallest negative product entering that cell can become the largest positive product leaving it. Therefore each cell needs both the minimum and maximum complete product of any path reaching it. A zero naturally makes both candidate extremes zero and needs no special transition.

**Combine the only possible predecessors.** Cell `(i, j)` can be entered only from `(i - 1, j)` or `(i, j - 1)`. Multiply the current value by both stored extremes from every predecessor that exists, then retain the smallest and largest results. Initialize both extremes at `(0, 0)` to its own value. Processing cells in row-major order guarantees that the required predecessor states are ready.

Every path into a cell ends at one of those predecessors, and multiplying an interval of possible incoming products by one fixed value places its new extremes at the incoming extremes (possibly swapping their order). Thus the transition retains the extremes of all and only valid paths to that cell. Inductively, the maximum stored at the bottom-right is the true greatest path product. Return `-1` when it is negative; otherwise apply the modulus only once to that already-selected value.

#### Complexity detail

Each of the $mn$ cells combines at most four candidate products, so the running time is $O(mn)$. Two $m \times n$ tables store the minimum and maximum reachable products, using $O(mn)$ auxiliary space. Rolling rows can reduce this to $O(n)$ without changing the recurrence.

#### Alternatives and edge cases

- **Enumerate every path:** Depth-first search is correct, but it explores $\binom{m+n-2}{m-1}$ paths in the worst case instead of sharing work between paths that reach the same cell.
- **Store only the maximum:** This loses a large-magnitude negative value that a later negative cell could turn into the optimum.
- **Reduce products modulo $10^9+7$ during the DP:** This is incorrect because residues do not preserve either numerical order or sign; reduce only the final non-negative maximum.
- A single-cell matrix has one path, whose product is that cell itself.
- A reachable zero makes `0` a valid answer and must beat the `-1` result used when every product is negative.
- Rows or columns of length one have exactly one path and are handled by the same predecessor rules.

</details>
