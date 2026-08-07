## Description

You are given an `m x n` matrix `grid` and a positive integer `k`. An **island** is a group of **positive** integers (representing land) that are **4-directionally** connected (horizontally or vertically).

The **total value** of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value **divisible by** `k`.

**Example 1:**

![](images/example1griddrawio-1.png)

<div class="example-block">
**Input:** <span class="example-io">grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

</div>

**Example 2:**

![](images/example2griddrawio.png)

<div class="example-block">
**Input:** <span class="example-io">grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

The grid contains six islands, each with a total value that is divisible by 3.

</div>

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 1000`

	- `1 <= m * n <= 10^5`

	- `0 <= grid[i][j] <= 10^6`

	- `1 <= k <= 10^6`
