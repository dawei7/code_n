## Description

You are given an integer `<font face="monospace">side</font>`, representing the edge length of a square with corners at `(0, 0)`, `(0, side)`, `(side, 0)`, and `(side, side)` on a Cartesian plane.

You are also given a **positive** integer `k` and a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinate of a point lying on the **boundary** of the square.

You need to select `k` elements among `points` such that the **minimum** Manhattan distance between any two points is **maximized**.

Return the **maximum** possible **minimum** Manhattan distance between the selected `k` points.

The Manhattan Distance between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/4080_example0_revised.png)

Select all four points.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/4080_example1_revised.png)

Select the points `(0, 0)`, `(2, 0)`, `(2, 2)`, and `(2, 1)`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/4080_example2_revised.png)

Select the points `(0, 0)`, `(0, 1)`, `(0, 2)`, `(1, 2)`, and `(2, 2)`.

</div>

**Constraints:**

	- `1 <= side <= 10^9`

	- `4 <= points.length <= min(4 * side, 15 * 10^3)`

	- `points[i] == [x_i, y_i]`

	- The input is generated such that:

		<li>`points[i]` lies on the boundary of the square.

		- All `points[i]` are **unique**.

	</li>
	- `4 <= k <= min(25, points.length)`
