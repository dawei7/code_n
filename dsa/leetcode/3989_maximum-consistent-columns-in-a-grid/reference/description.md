## Description

You are given a 2D integer array `grid` of size `m x n`, and an integer `limit`.

You may remove zero or more columns from the grid, but at least one column must remain. The **relative** order of the remaining columns must be preserved.

A grid is called **consistent** if for every row `i`, and for every pair of adjacent remaining columns `a` and `b` with `a < b`, the following holds: $|\text{grid}[i][b] - \text{grid}[i][a]| \le limit$.

Return the **maximum** number of columns that can remain such that the resulting grid is **consistent**.
### Function Contract

`solve(grid, limit) -> int`

Let $m=\lvert\texttt{grid}\rvert$ and $n=\lvert\texttt{grid[0]}\rvert$.

**Inputs**

- `grid`: A nonempty rectangular matrix of integers with `m` rows and `n` columns.
- `limit`: The inclusive maximum absolute difference allowed between adjacent retained columns in each row.

Column removal preserves relative order, and at least one column must remain. A pair of retained columns is compatible only when its absolute difference is at most `limit` in all `m` rows.

**Output**

Return the largest number of columns that can be retained while every adjacent retained pair is compatible.

### Examples
#### Example 1

<div class="example-block">
**Input:** grid = [[-2,0,3]], limit = 2

**Output:** 2

**Explanation:**

- Remove column 2 and keep columns 0 and 1, which gives $|\text{grid}[0][1] − \text{grid}[0][0]| = |0 − (−2)| = 2 \le limit$.

- Thus, the maximum number of columns that can remain is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** grid = [[1,-1,1],[2,2,2]], limit = 1

**Output:** 2

**Explanation:**

- Remove column 1 and keep columns 0 and 2, which gives

		<li>$|\text{grid}[0][2] − \text{grid}[0][0]| = |1 − 1| = 0 \le limit$ and

- $|\text{grid}[1][2] − \text{grid}[1][0]| = |2 − 2| = 0 \le limit$.

	</li>
- Thus, the maximum number of columns that can remain is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** grid = [[-5,5]], limit = 9

**Output:** 1

**Explanation:**

- Remove either column 0 or column 1, since $|\text{grid}[0][1] − \text{grid}[0][0]| = |5 − (−5)| = 10 > limit$.

- Thus, the maximum number of columns that can remain is 1.

</div>
### Constraints

- $1 \le m = \text{grid.length} \le 250$

- $1 \le n = \text{grid}[i].length \le 250$

- $-10^{5} \le \text{grid}[i][j] \le 10^{5}$

- $0 \le limit \le 10^{5}​​​​​​​​​​​​​​​​$