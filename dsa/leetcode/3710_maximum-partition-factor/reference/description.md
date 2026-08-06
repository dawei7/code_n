## Description

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `<font>i^th</font>` point on the Cartesian plane.

The **Manhattan distance** between two points `points[i] = [x_i, y_i]` and `points[j] = [x_j, y_j]` is `|x_i - x_j| + |y_i - y_j|`.

Split the `n` points into **exactly two non-empty** groups. The **partition factor** of a split is the **minimum** Manhattan distance among all unordered pairs of points that lie in the same group.

Return the **maximum** possible **partition factor** over all valid splits.

Note: A group of size 1 contributes no intra-group pairs. When `n = 2` (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.
