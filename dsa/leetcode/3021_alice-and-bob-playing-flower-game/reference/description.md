## Description

Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are `x` flowers in the first lane between Alice and Bob, and `y` flowers in the second lane between them.

<img alt="" src="https://assets.leetcode.com/uploads/2025/08/27/3021.png" style="width: 300px; height: 150px;" />

The game proceeds as follows:

<ol>
	<li>Alice takes the first turn.</li>
	<li>In each turn, a player must choose either one of the lane and pick one flower from that side.</li>
	<li>At the end of the turn, if there are no flowers left at all in either lane, the **current** player captures their opponent and wins the game.</li>
</ol>

Given two integers, `n` and `m`, the task is to compute the number of possible pairs `(x, y)` that satisfy the conditions:

<ul>
	<li>Alice must win the game according to the described rules.</li>
	<li>The number of flowers `x` in the first lane must be in the range `[1,n]`.</li>
	<li>The number of flowers `y` in the second lane must be in the range `[1,m]`.</li>
</ul>

Return *the number of possible pairs* `(x, y)` *that satisfy the conditions mentioned in the statement*.
