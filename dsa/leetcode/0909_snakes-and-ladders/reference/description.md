## Description

You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a <a href="https://en.wikipedia.org/wiki/Boustrophedon" target="_blank">**Boustrophedon style**</a> starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square `1` of the board. In each move, starting from square `curr`, do the following:

<ul>
	<li>Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n^2)]`.

	<ul>
		<li>This choice simulates the result of a standard **6-sided die roll**: i.e., there are always at most 6 destinations, regardless of the size of the board.</li>
	</ul>
	</li>
	<li>If `next` has a snake or ladder, you **must** move to the destination of that snake or ladder. Otherwise, you move to `next`.</li>
	<li>The game ends when you reach the square `n^2`.</li>
</ul>

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n^2` are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do **not** follow the subsequent snake or ladder.

<ul>
	<li>For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do **not** follow the subsequent ladder to `4`.</li>
</ul>

Return *the least number of dice rolls required to reach the square *`n^2`*. If it is not possible to reach the square, return *`-1`.
