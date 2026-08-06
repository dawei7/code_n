## Description

You are given an integer array `nums`.

Consider all pairs of **distinct** values `x` and `y` from `nums` such that:

<ul>
	<li>`x < y`</li>
	<li>`x` and `y` have different <span data-keyword="frequency-array">frequencies</span> in `nums`.</li>
</ul>

Among all such pairs:

<ul>
	<li>Choose the pair with the smallest possible value of `x`.</li>
	<li>If multiple pairs have the same `x`, choose the one with the smallest possible value of `y`.</li>
</ul>

Return an integer array `[x, y]`. If no valid pair exists, return `[-1, -1]`.
