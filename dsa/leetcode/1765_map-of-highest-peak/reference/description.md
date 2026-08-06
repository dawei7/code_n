## Description

You are given an integer matrix `isWater` of size `m x n` that represents a map of **land** and **water** cells.

<ul>
	<li>If `isWater[i][j] == 0`, cell `(i, j)` is a **land** cell.</li>
	<li>If `isWater[i][j] == 1`, cell `(i, j)` is a **water** cell.</li>
</ul>

You must assign each cell a height in a way that follows these rules:

<ul>
	<li>The height of each cell must be non-negative.</li>
	<li>If the cell is a **water** cell, its height must be `0`.</li>
	<li>Any two adjacent cells must have an absolute height difference of **at most** `1`. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).</li>
</ul>

Find an assignment of heights such that the maximum height in the matrix is **maximized**.

Return *an integer matrix *`height`* of size *`m x n`* where *`height[i][j]`* is cell *`(i, j)`*'s height. If there are multiple solutions, return **any** of them*.
