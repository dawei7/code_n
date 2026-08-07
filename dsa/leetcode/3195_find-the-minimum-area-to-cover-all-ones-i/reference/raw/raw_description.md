## Description

You are given a 2D **binary** array `grid`. Find a rectangle with horizontal and vertical sides with the** smallest** area, such that all the 1's in `grid` lie inside this rectangle.

Return the **minimum** possible area of the rectangle.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[0,1,0],[1,0,1]]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

![](images/examplerect0.png)

The smallest rectangle has a height of 2 and a width of 3, so it has an area of `2 * 3 = 6`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">grid = [[1,0],[0,0]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/examplerect1.png)

The smallest rectangle has both height and width 1, so its area is `1 * 1 = 1`.

</div>

**Constraints:**

	- `1 <= grid.length, grid[i].length <= 1000`

	- `grid[i][j]` is either 0 or 1.

	- The input is generated such that there is at least one 1 in `grid`.
