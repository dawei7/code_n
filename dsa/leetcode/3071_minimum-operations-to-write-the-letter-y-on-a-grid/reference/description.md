## Description

You are given a **0-indexed** `n x n` grid where `n` is odd, and `grid[r][c]` is `0`, `1`, or `2`.

We say that a cell belongs to the Letter **Y** if it belongs to one of the following:

<ul>
	<li>The diagonal starting at the top-left cell and ending at the center cell of the grid.</li>
	<li>The diagonal starting at the top-right cell and ending at the center cell of the grid.</li>
	<li>The vertical line starting at the center cell and ending at the bottom border of the grid.</li>
</ul>

The Letter **Y** is written on the grid if and only if:

<ul>
	<li>All values at cells belonging to the Y are equal.</li>
	<li>All values at cells not belonging to the Y are equal.</li>
	<li>The values at cells belonging to the Y are different from the values at cells not belonging to the Y.</li>
</ul>

Return *the **minimum** number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to* `0`*,* `1`*,* *or* `2`*.*
