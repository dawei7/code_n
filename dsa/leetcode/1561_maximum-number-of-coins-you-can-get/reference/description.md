## Description

There are `3n` piles of coins of varying size, you and your friends will take piles of coins as follows:

<ul>
	<li>In each step, you will choose **any **`3` piles of coins (not necessarily consecutive).</li>
	<li>Of your choice, Alice will pick the pile with the maximum number of coins.</li>
	<li>You will pick the next pile with the maximum number of coins.</li>
	<li>Your friend Bob will pick the last pile.</li>
	<li>Repeat until there are no more piles of coins.</li>
</ul>

Given an array of integers `piles` where `piles[i]` is the number of coins in the `i^th` pile.

Return the maximum number of coins that you can have.
