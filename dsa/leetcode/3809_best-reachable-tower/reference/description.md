## Description

You are given a 2D integer array `towers`, where `towers[i] = [x_i, y_i, q_i]` represents the coordinates `(x_i, y_i)` and quality factor `q_i` of the `i^th` tower.

You are also given an integer array `center = [cx, cy​​​​​​​]` representing your location, and an integer `radius`.

A tower is **reachable** if its **Manhattan distance** from `center` is **less than or equal** to `radius`.

Among all reachable towers:

<ul>
	<li>Return the coordinates of the tower with the **maximum** quality factor.</li>
	<li>If there is a tie, return the tower with the **lexicographically smallest** coordinate. If no tower is reachable, return `[-1, -1]`.</li>
</ul>
The **Manhattan Distance** between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.

A coordinate `[x_i, y_i]` is **lexicographically smaller** than `[x_j, y_j]` if `x_i < x_j`, or `x_i == x_j` and `y_i < y_j`.

`|x|` denotes the **absolute** **value** of `x`.
