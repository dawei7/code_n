## Description

You are given a 2D array of integers `coordinates` of length `n` and an integer `k`, where `0 <= k < n`.

`coordinates[i] = [x_i, y_i]` indicates the point `(x_i, y_i)` in a 2D plane.

An **increasing path** of length `m` is defined as a list of points `(x_1, y_1)`, `(x_2, y_2)`, `(x_3, y_3)`, ..., `(x_m, y_m)` such that:

<ul>
	<li>`x_i < x_i + 1` and `y_i < y_i + 1` for all `i` where `1 <= i < m`.</li>
	<li>`(x_i, y_i)` is in the given coordinates for all `i` where `1 <= i <= m`.</li>
</ul>

Return the **maximum** length of an **increasing path** that contains `coordinates[k]`.
