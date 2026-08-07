## Description

You are given a 2D integer array `grid` of size `m x n`.

You must select **exactly one** integer from each row of the grid.

Return an integer denoting the **minimum possible bitwise OR** of the selected integers from each row.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,5],[2,4]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Choose 1 from the first row and 2 from the second row.

	- The bitwise OR of `1 | 2 = 3`​​​​​​​, which is the minimum possible.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[3,5],[6,4]]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- Choose 5 from the first row and 4 from the second row.

	- The bitwise OR of `5 | 4 = 5`​​​​​​​, which is the minimum possible.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[7,9,8]]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

	- Choosing 7 gives the minimum bitwise OR.

</div>

**Constraints:**

	- `1 <= m == grid.length <= 10^5`

	- `1 <= n == grid[i].length <= 10^5`

	- `m * n <= 10^5`

	- `1 <= grid[i][j] <= 10^5​​​​​​​`
