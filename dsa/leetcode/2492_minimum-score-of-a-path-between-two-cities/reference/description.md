## Description

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads` where `roads[i] = [a_i, b_i, distance_i]` indicates that there is a **bidirectional **road between cities `a_i` and `b_i` with a distance equal to `distance_i`. The cities graph is not necessarily connected.

The **score** of a path between two cities is defined as the **minimum **distance of a road in this path.

Return the **minimum **possible score of a path between cities 1 and `n`.

**Note**:

<ul>
	<li>A path is a sequence of roads between two cities.</li>
	<li>It is allowed for a path to contain the same road **multiple** times, and you can visit cities 1 and `n` multiple times along the path.</li>
	<li>The test cases are generated such that there is **at least** one path between 1 and `n`.</li>
</ul>
