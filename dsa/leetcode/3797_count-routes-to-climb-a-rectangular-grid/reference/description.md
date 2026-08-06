## Description

You are given a string array `grid` of size `n`, where each string `grid[i]` has length `m`. The character `grid[i][j]` is one of the following symbols:

<ul>
	<li>`'.'`: The cell is available.</li>
	<li>`'#'`: The cell is blocked.</li>
</ul>

You want to count the number of different routes to climb `grid`. Each route must start from *any cell* in the bottom row (row `n - 1`) and end in the top row (row 0).

However, there are some constraints on the route.

<ul>
	<li>You can only move from one available cell to **another** available cell.</li>
	<li>The **Euclidean distance** of each move is **at most** `d`, where `d` is an integer parameter given to you. The Euclidean distance between two cells `(r1, c1)`, `(r2, c2)` is `sqrt((r1 - r2)^2 + (c1 - c2)^2)`.</li>
	<li>Each move either stays on the same row or moves to the row directly above (from row `r` to `r - 1`).</li>
	<li>You cannot stay on the same row for two consecutive turns. If you stay on the same row in a move (and this move is not the last move), your next move must go to the row above.</li>
</ul>

Return an integer denoting the number of such routes. Since the answer may be very large, return it **modulo** `10^9 + 7`.
