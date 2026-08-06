## Description

You are given an `n x m` integer matrix `matrix` containing non-negative integers.

A **non-zero **cell `(row, col)` checks the cells near it as follows:

<ul>
	<li>Let `x = matrix[row][col]`.</li>
	<li>Consider every cell within `x` rows and `x` columns of `(row, col)`.</li>
	<li>Ignore cells that are outside the matrix.</li>
	<li>Ignore the cells where both the row distance and column distance are exactly `x`.</li>
</ul>

The cell `(row, col)` is a **local maximum** if it is **non-zero** and no considered cell has a value **greater than** `x`.

Return an integer denoting the number of **local maximums** in `matrix`.

 

<strong class="example">​​​​​​​Example 1:</strong>

<div class="example-block">
**Input:** <span class="example-io">matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]</span>

**Output:** <span class="example-io">1</span>

<img alt="" src="https://assets.leetcode.com/uploads/2026/05/13/chatgpt-image-may-14-2026-01_53_19-am.png" style="width: 300px; height: 300px;" />​​​​​​​​​​​​​​​​​​​​​

**Explanation:**

<ul>
	<li>For the non-zero cell `(3, 3)`, `x = matrix[3][3] = 2`.</li>
	<li>The highlighted cells are the considered cells within `x` rows and `x` columns of `(3, 3)`.</li>
	<li>The four cells with both row and column distances equal to `x = 2` are ignored.</li>
	<li>No considered cell has a value greater than 2, so `(3, 3)` is a local maximum.</li>
	<li>There are no other non-zero cells, so the answer is 1.</li>
</ul>
</div>
