## Description

You are given a **0-indexed** 2D matrix `grid` of size `m x n`, where `(r, c)` represents:

<ul>
	<li>A **land** cell if `grid[r][c] = 0`, or</li>
	<li>A **water** cell containing `grid[r][c]` fish, if `grid[r][c] > 0`.</li>
</ul>

A fisher can start at any **water** cell `(r, c)` and can do the following operations any number of times:

<ul>
	<li>Catch all the fish at cell `(r, c)`, or</li>
	<li>Move to any adjacent **water** cell.</li>
</ul>

Return *the **maximum** number of fish the fisher can catch if he chooses his starting cell optimally, or *`0` if no water cell exists.

An **adjacent** cell of the cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` or `(r - 1, c)` if it exists.
