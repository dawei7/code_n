## Description

There is an `m x n` grid, where `(0, 0)` is the top-left cell and `(m - 1, n - 1)` is the bottom-right cell. You are given an integer array `startPos` where `startPos = [start_row, start_col]` indicates that **initially**, a **robot** is at the cell `(start_row, start_col)`. You are also given an integer array `homePos` where `homePos = [home_row, home_col]` indicates that its **home** is at the cell `(home_row, home_col)`.

The robot needs to go to its home. It can move one cell in four directions: **left**, **right**, **up**, or **down**, and it can not move outside the boundary. Every move incurs some cost. You are further given two **0-indexed** integer arrays: `rowCosts` of length `m` and `colCosts` of length `n`.

<ul>
	<li>If the robot moves **up** or **down** into a cell whose **row** is `r`, then this move costs `rowCosts[r]`.</li>
	<li>If the robot moves **left** or **right** into a cell whose **column** is `c`, then this move costs `colCosts[c]`.</li>
</ul>

Return *the **minimum total cost** for this robot to return home*.
