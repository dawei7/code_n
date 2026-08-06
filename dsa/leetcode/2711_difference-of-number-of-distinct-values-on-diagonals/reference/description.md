## Description

Given a 2D `grid` of size `m x n`, you should find the matrix `answer` of size `m x n`.

The cell `answer[r][c]` is calculated by looking at the diagonal values of the cell `grid[r][c]`:

<ul>
	<li>Let `leftAbove[r][c]` be the number of **distinct** values on the diagonal to the left and above the cell `grid[r][c]` not including the cell `grid[r][c]` itself.</li>
	<li>Let `rightBelow[r][c]` be the number of **distinct** values on the diagonal to the right and below the cell `grid[r][c]`, not including the cell `grid[r][c]` itself.</li>
	<li>Then `answer[r][c] = |leftAbove[r][c] - rightBelow[r][c]|`.</li>
</ul>

A **matrix diagonal** is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until the end of the matrix is reached.

<ul>
	<li>For example, in the below diagram the diagonal is highlighted using the cell with indices `(2, 3)` colored gray:

	<ul>
		<li>Red-colored cells are left and above the cell.</li>
		<li>Blue-colored cells are right and below the cell.</li>
	</ul>
	</li>
</ul>

<img alt="" src="https://assets.leetcode.com/uploads/2024/05/26/diagonal.png" style="width: 200px; height: 160px;" />

Return the matrix `answer`.
