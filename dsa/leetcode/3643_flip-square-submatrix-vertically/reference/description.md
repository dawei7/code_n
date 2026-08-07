## Description

You are given an `m x n` integer matrix `grid`, and three integers `x`, `y`, and `k`.

The integers `x` and `y` represent the row and column indices of the **top-left** corner of a **square** submatrix and the integer `k` represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

![](images/gridexmdrawio.png)

<div class="example-block">
**Input:** grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3

**Output:** [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

**Explanation:**

The diagram above shows the grid before and after the transformation.

</div>
#### Example 2

![](images/gridexm2drawio.png)

​​​​​​​
<div class="example-block">
**Input:** grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2

**Output:** [[3,4,4,2],[2,3,2,3]]

**Explanation:**

The diagram above shows the grid before and after the transformation.

</div>
### Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 50$

- $1 \le \text{grid}[i][j] \le 100$

- $0 \le x < m$

- $0 \le y < n$

- $1 \le k \le min(m - x, n - y)$