## Description

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point. All coordinates in `points` are **distinct**.

If a point is **activated**, then all points that have the **same** x-coordinate **or** y-coordinate become **activated** as well.

Activation continues until no additional points can be activated.

You may add **one additional** point at any integer coordinate `(x, y)` not already present in `points`. Activation begins by **activating** this **newly added point**.

Return an integer denoting the **maximum** number of points that can be activated, including the newly added point.
