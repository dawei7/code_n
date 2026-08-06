## Description

You are given an `n x n` `grid` representing a field of cherries, each cell is one of three possible integers.

<ul>
	<li>`0` means the cell is empty, so you can pass through,</li>
	<li>`1` means the cell contains a cherry that you can pick up and pass through, or</li>
	<li>`-1` means the cell contains a thorn that blocks your way.</li>
</ul>

Return *the maximum number of cherries you can collect by following the rules below*:

<ul>
	<li>Starting at the position `(0, 0)` and reaching `(n - 1, n - 1)` by moving right or down through valid path cells (cells with value `0` or `1`).</li>
	<li>After reaching `(n - 1, n - 1)`, returning to `(0, 0)` by moving left or up through valid path cells.</li>
	<li>When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell `0`.</li>
	<li>If there is no valid path between `(0, 0)` and `(n - 1, n - 1)`, then no cherries can be collected.</li>
</ul>
