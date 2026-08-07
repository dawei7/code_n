## Description

You are given an `m x n` integer matrix `grid` and an integer `k`.

For every contiguous `k x k` **submatrix** of `grid`, compute the **minimum absolute** difference between any two **distinct** values within that **submatrix**.

Return a 2D array `ans` of size $(m - k + 1) x (n - k + 1)$, where $\text{ans}[i][j]$ is the minimum absolute difference in the submatrix whose top-left corner is `(i, j)` in `grid`.

**Note**: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix `(x1, y1, x2, y2)` is a matrix that is formed by choosing all cells $\text{matrix}[x][y]$ where $x1 \le x \le x2$ and $y1 \le y \le y2$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** grid = [[1,8],[3,-2]], k = 2

**Output:** [[2]]

**Explanation:**

- There is only one possible `k x k` submatrix: `[[1, 8], [3, -2]]`.

- Distinct values in the submatrix are `[1, 8, 3, -2]`.

- The minimum absolute difference in the submatrix is $|1 - 3| = 2$. Thus, the answer is `[[2]]`.

</div>
#### Example 2

<div class="example-block">
**Input:** grid = [[3,-1]], k = 1

**Output:** [[0,0]]

**Explanation:**

- Both `k x k` submatrix has only one distinct element.

- Thus, the answer is `[[0, 0]]`.

</div>
#### Example 3

<div class="example-block">
**Input:** grid = [[1,-2,3],[2,3,5]], k = 2

**Output:** [[1,2]]

**Explanation:**

- There are two possible `k × k` submatrix:

		<li>Starting at `(0, 0)`: `[[1, -2], [2, 3]]`.

			<li>Distinct values in the submatrix are `[1, -2, 2, 3]`.

- The minimum absolute difference in the submatrix is $|1 - 2| = 1$.

		</li>
- Starting at `(0, 1)`: `[[-2, 3], [3, 5]]`.

			<li>Distinct values in the submatrix are `[-2, 3, 5]`.

- The minimum absolute difference in the submatrix is $|3 - 5| = 2$.

		</li>

	</li>
- Thus, the answer is `[[1, 2]]`.

</div>
### Constraints

- $1 \le m = \text{grid.length} \le 30$

- $1 \le n = \text{grid}[i].length \le 30$

- $-10^{5} \le \text{grid}[i][j] \le 10^{5}$

- $1 \le k \le min(m, n)$