## Description

You are given an integer array `nums`.

Start by selecting a starting position `curr` such that `nums[curr] == 0`, and choose a movement **direction** of either left or right.

After that, you repeat the following process:

<ul>
	<li>If `curr` is out of the range `[0, n - 1]`, this process ends.</li>
	<li>If `nums[curr] == 0`, move in the current direction by **incrementing** `curr` if you are moving right, or **decrementing** `curr` if you are moving left.</li>
	<li>Else if `nums[curr] > 0`:
	<ul>
		<li>Decrement `nums[curr]` by 1.</li>
		<li>**Reverse** your movement direction (left becomes right and vice versa).</li>
		<li>Take a step in your new direction.</li>
	</ul>
	</li>
</ul>

A selection of the initial position `curr` and movement direction is considered **valid** if every element in `nums` becomes 0 by the end of the process.

Return the number of possible **valid** selections.
