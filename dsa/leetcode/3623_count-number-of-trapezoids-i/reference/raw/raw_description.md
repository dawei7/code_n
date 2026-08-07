## Description

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point on the Cartesian plane.

A **horizontal** **trapezoid** is a convex quadrilateral with **at least one pair** of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the * number of unique ****horizontal* *trapezoids*** that can be formed by choosing any four distinct points from `points`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">points = [[1,0],[2,0],[3,0],[2,2],[3,2]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

![](images/desmos-graph-6.png)

![](images/desmos-graph-7.png)

![](images/desmos-graph-8.png)

There are three distinct ways to pick four points that form a horizontal trapezoid:

	- Using points `[1,0]`, `[2,0]`, `[3,2]`, and `[2,2]`.

	- Using points `[2,0]`, `[3,0]`, `[3,2]`, and `[2,2]`.

	- Using points `[1,0]`, `[3,0]`, `[3,2]`, and `[2,2]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">points = [[0,0],[1,0],[0,1],[2,1]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/desmos-graph-5.png)

There is only one horizontal trapezoid that can be formed.

</div>

**Constraints:**

	- `4 <= points.length <= 10^5`

	- `–10^8 <= x_i, y_i <= 10^8`

	- All points are pairwise distinct.
