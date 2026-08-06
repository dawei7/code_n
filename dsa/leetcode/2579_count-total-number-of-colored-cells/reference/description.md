## Description

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer `n`, indicating that you must do the following routine for `n` minutes:

<ul>
	<li>At the first minute, color **any** arbitrary unit cell blue.</li>
	<li>Every minute thereafter, color blue **every** uncolored cell that touches a blue cell.</li>
</ul>

Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png" style="width: 500px; height: 279px;" />
Return *the number of **colored cells** at the end of *`n` *minutes*.
