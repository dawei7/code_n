## Description

You are given a `rows x cols` matrix `grid` representing a field of cherries where `grid[i][j]` represents the number of cherries that you can collect from the `(i, j)` cell.

You have two robots that can collect cherries for you:

<ul>
	<li>**Robot #1** is located at the **top-left corner** `(0, 0)`, and</li>
	<li>**Robot #2** is located at the **top-right corner** `(0, cols - 1)`.</li>
</ul>

Return *the maximum number of cherries collection using both robots by following the rules below*:

<ul>
	<li>From a cell `(i, j)`, robots can move to cell `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`.</li>
	<li>When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.</li>
	<li>When both robots stay in the same cell, only one takes the cherries.</li>
	<li>Both robots cannot move outside of the grid at any moment.</li>
	<li>Both robots should reach the bottom row in `grid`.</li>
</ul>
