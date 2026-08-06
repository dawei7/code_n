## Description

You are given a 2D integer array `points` where `points[i] = [x_i, y_i, z_i]` represents a point in 3D space, and an integer array `target` representing a target point.

Define **generation** 0 as the initial list of points. For each integer `k >= 1`, form generation `k` as follows:

<ul>
	<li>Consider every pair of two **distinct** points `a = [x_1, y_1, z_1]` and `b = [x_2, y_2, z_2]` taken from all points produced in generations 0 through `k - 1`.</li>
	<li>For each such pair, compute `c = [floor((x_1 + x_2) / 2), floor((y_1 + y_2) / 2), floor((z_1 + z_2) / 2)]` and collect every such `c` into a generation `k`.</li>
	<li>All points in the generation `k` are produced **simultaneously** from points in generations 0 through​​​​​​​ `k - 1`.</li>
	<li>After generation `k` is formed, the points in the generation `k` are considered available for forming later generations.</li>
</ul>

Return the **smallest** integer `k` such that the `target` appears in one of the generations 0 through `k`. If the `target` is already in the initial points, return 0. If it is impossible to obtain the `target`, return -1.

Notes:

<ul>
	<li>**floor** denotes rounding **down** to the nearest integer.</li>
	<li>"Two **distinct** points" means the two chosen points must have **different** `(x, y, z)` coordinates. A point cannot be paired with itself, and pairing two points with **identical** coordinates is not possible.</li>
</ul>
