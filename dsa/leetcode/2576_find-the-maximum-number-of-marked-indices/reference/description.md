## Description

You are given a **0-indexed** integer array `nums`.

Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:

<ul>
	<li>Pick two **different unmarked** indices `i` and `j` such that `2 * nums[i] <= nums[j]`, then mark `i` and `j`.</li>
</ul>

Return *the maximum possible number of marked indices in `nums` using the above operation any number of times*.
