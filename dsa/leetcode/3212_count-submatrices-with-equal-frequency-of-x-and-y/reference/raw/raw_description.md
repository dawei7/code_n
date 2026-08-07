## Description

Given a 2D character matrix `grid`, where `grid[i][j]` is either `'X'`, `'Y'`, or `'.'`, return the number of <span data-keyword="submatrix">submatrices</span> that contain:

	- `grid[0][0]`

	- an **equal** frequency of `'X'` and `'Y'`.

	- **at least** one `'X'`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [["X","Y","."],["Y",".","."]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

**

![](images/examplems.png)

**

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [["X","X"],["X","Y"]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No submatrix has an equal frequency of `'X'` and `'Y'`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[".","."],[".","."]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No submatrix has at least one `'X'`.

</div>

**Constraints:**

	- `1 <= grid.length, grid[i].length <= 1000`

	- `grid[i][j]` is either `'X'`, `'Y'`, or `'.'`.
