## Description

You are given a string `s` consisting of characters `'U'`, `'D'`, `'L'`, and `'R'`, representing moves on an infinite 2D Cartesian grid.

<ul>
	<li>`'U'`: Move from `(x, y)` to `(x, y + 1)`.</li>
	<li>`'D'`: Move from `(x, y)` to `(x, y - 1)`.</li>
	<li>`'L'`: Move from `(x, y)` to `(x - 1, y)`.</li>
	<li>`'R'`: Move from `(x, y)` to `(x + 1, y)`.</li>
</ul>

You are also given a positive integer `k`.

You **must** choose and remove **exactly one** contiguous substring of length `k` from `s`. Then, start from coordinate `(0, 0)` and perform the remaining moves in order.

Return an integer denoting the number of **distinct** final coordinates reachable.
