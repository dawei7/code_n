## Description

You are given a `m x n` matrix `grid` consisting of **non-negative** integers.

In one operation, you can increment the value of any `grid[i][j]` by 1.

Return the **minimum** number of operations needed to make all columns of `grid` **strictly increasing**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[3,2],[1,3],[3,4],[0,1]]</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

	- To make the `0^th` column strictly increasing, we can apply 3 operations on `grid[1][0]`, 2 operations on `grid[2][0]`, and 6 operations on `grid[3][0]`.

	- To make the `1^st` column strictly increasing, we can apply 4 operations on `grid[3][1]`.

![](images/firstexample.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[3,2,1],[2,1,0],[1,2,3]]</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

	- To make the `0^th` column strictly increasing, we can apply 2 operations on `grid[1][0]`, and 4 operations on `grid[2][0]`.

	- To make the `1^st` column strictly increasing, we can apply 2 operations on `grid[1][1]`, and 2 operations on `grid[2][1]`.

	- To make the `2^nd` column strictly increasing, we can apply 2 operations on `grid[1][2]`.

![](images/secondexample.png)

</div>

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 50`

	- `0 <= grid[i][j] < 2500`

<div class="spoiler">
<div>

```

```

</div>
</div>
