## Description

You are given three integers `m`, `n`, and `k`.

Construct **any** `m x n` grid consisting only of the characters `'.'` and `'#'`, where:

<ul>
	<li>`'.'` represents a free cell.</li>
	<li>`'#'` represents an obstacle cell.</li>
</ul>

A **valid path** is a sequence of free cells that:

<ul>
	<li>Starts at the top-left cell `(0, 0)`.</li>
	<li>Ends at the bottom-right cell `(m - 1, n - 1)`.</li>
	<li>Moves only:
	<ul>
		<li>Right, from `(i, j)` to `(i, j + 1)`, or</li>
		<li>Down, from `(i, j)` to `(i + 1, j)`.</li>
	</ul>
	</li>
</ul>

Return any grid such that there are **exactly** `k` **valid paths** from the top-left cell to the bottom-right cell. If no such grid exists, return an empty array.
