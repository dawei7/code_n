## Description

You are given four integers `sx`, `sy`, `tx`, and `ty`, representing two points `(sx, sy)` and `(tx, ty)` on an infinitely large 2D grid.

You start at `(sx, sy)`.

At any point `(x, y)`, define `m = max(x, y)`. You can either:

<ul>
	<li>Move to `(x + m, y)`, or</li>
	<li>Move to `(x, y + m)`.</li>
</ul>

Return the **minimum** number of moves required to reach `(tx, ty)`. If it is impossible to reach the target, return -1.
