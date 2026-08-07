## Description

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where `points[i] = [x_i, y_i]`.

Count the number of pairs of points `(A, B)`, where

	- `A` is on the **upper left** side of `B`, and

	- there are no other points in the rectangle (or line) they make (**including the border**), except for the points `A` and `B`.

Return the count.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">points = [[1,1],[2,2],[3,3]]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

![](images/example1alicebob.png)

There is no way to choose `A` and `B` such that `A` is on the upper left side of `B`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">points = [[6,2],[4,4],[2,6]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/t2.jpg)

	- The left one is the pair `(points[1], points[0])`, where `points[1]` is on the upper left side of `points[0]` and the rectangle is empty.

	- The middle one is the pair `(points[2], points[1])`, same as the left one it is a valid pair.

	- The right one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]`, but `points[1]` is inside the rectangle so it's not a valid pair.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">points = [[3,1],[1,3],[1,1]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/t3.jpg)

	- The left one is the pair `(points[2], points[0])`, where `points[2]` is on the upper left side of `points[0]` and there are no other points on the line they form. Note that it is a valid state when the two points form a line.

	- The middle one is the pair `(points[1], points[2])`, it is a valid pair same as the left one.

	- The right one is the pair `(points[1], points[0])`, it is not a valid pair as `points[2]` is on the border of the rectangle.

</div>

**Constraints:**

	- `2 <= n <= 50`

	- `points[i].length == 2`

	- `0 <= points[i][0], points[i][1] <= 50`

	- All `points[i]` are distinct.
