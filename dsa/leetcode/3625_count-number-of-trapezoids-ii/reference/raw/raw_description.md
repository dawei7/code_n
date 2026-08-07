## Description

You are given a 2D integer array `points` where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point on the Cartesian plane.

Return *the number of unique **trapezoids* that can be formed by choosing any four distinct points from `points`.

A** ****trapezoid** is a convex quadrilateral with **at least one pair** of parallel sides. Two lines are parallel if and only if they have the same slope.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/desmos-graph-4.png)

![](images/desmos-graph-3.png)

There are two distinct ways to pick four points that form a trapezoid:

	- The points `[-3,2], [2,3], [3,2], [2,-3]` form one trapezoid.

	- The points `[2,3], [3,2], [3,0], [2,-3]` form another trapezoid.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">points = [[0,0],[1,0],[0,1],[2,1]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/desmos-graph-5.png)

There is only one trapezoid which can be formed.

</div>

**Constraints:**

	- `4 <= points.length <= 500`

	- `–1000 <= x_i, y_i <= 1000`

	- All points are pairwise distinct.
