## Description

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `<font>i^th</font>` point on the Cartesian plane.

The **Manhattan distance** between two points `points[i] = [x_i, y_i]` and `points[j] = [x_j, y_j]` is `|x_i - x_j| + |y_i - y_j|`.

Split the `n` points into **exactly two non-empty** groups. The **partition factor** of a split is the **minimum** Manhattan distance among all unordered pairs of points that lie in the same group.

Return the **maximum** possible **partition factor** over all valid splits.

Note: A group of size 1 contributes no intra-group pairs. When `n = 2` (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.

**Example 1:**

<div class="example-block">
**Input:** <span>points = [[0,0],[0,2],[2,0],[2,2]]</span>

**Output:** <span>4</span>

**Explanation:**

We split the points into two groups: `{[0, 0], [2, 2]}` and `{[0, 2], [2, 0]}`.

	- In the first group, the only pair has Manhattan distance `|0 - 2| + |0 - 2| = 4`.

	- In the second group, the only pair also has Manhattan distance `|0 - 2| + |2 - 0| = 4`.

The partition factor of this split is `min(4, 4) = 4`, which is maximal.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span>points = [[0,0],[0,1],[10,0]]</span>

**Output:** <span>11</span>

**Explanation:​​​​​​​**

We split the points into two groups: `{[0, 1], [10, 0]}` and `{[0, 0]}`.

	- In the first group, the only pair has Manhattan distance `|0 - 10| + |1 - 0| = 11`.

	- The second group is a singleton, so it contributes no pairs.

The partition factor of this split is `11`, which is maximal.

</div>

**Constraints:**

	- `2 <= points.length <= 500`

	- `points[i] = [x_i, y_i]`

	- `-10^8 <= x_i, y_i <= 10^8`
