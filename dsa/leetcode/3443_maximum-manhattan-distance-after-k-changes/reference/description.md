## Description

You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`, where `s[i]` indicates movements in an infinite grid:

<ul>
	<li>`'N'` : Move north by 1 unit.</li>
	<li>`'S'` : Move south by 1 unit.</li>
	<li>`'E'` : Move east by 1 unit.</li>
	<li>`'W'` : Move west by 1 unit.</li>
</ul>

Initially, you are at the origin `(0, 0)`. You can change **at most** `k` characters to any of the four directions.

Find the **maximum** **Manhattan distance** from the origin that can be achieved **at any time** while performing the movements **in order**.

The **Manhattan Distance** between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.
