## Description

We have `n` chips, where the position of the `i^th` chip is `position[i]`.

We need to move all the chips to **the same position**. In one step, we can change the position of the `i^th` chip from `position[i]` to:

<ul>
	<li>`position[i] + 2` or `position[i] - 2` with `cost = 0`.</li>
	<li>`position[i] + 1` or `position[i] - 1` with `cost = 1`.</li>
</ul>

Return *the minimum cost* needed to move all the chips to the same position.
