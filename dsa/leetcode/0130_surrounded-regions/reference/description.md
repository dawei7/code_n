## Description

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

<ul>
	<li>**Connect**: A cell is connected to adjacent cells horizontally or vertically.</li>
	<li>**Region**: To form a region **connect every** `'O'` cell.</li>
	<li>**Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed **by `'X'` cells.</li>
</ul>

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.
