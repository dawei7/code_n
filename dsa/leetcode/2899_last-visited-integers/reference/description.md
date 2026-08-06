## Description

Given an integer array `nums` where `nums[i]` is either a positive integer or `-1`. We need to find for each `-1` the respective positive integer, which we call the last visited integer.

To achieve this goal, let's define two empty arrays: `seen` and `ans`.

Start iterating from the beginning of the array `nums`.

<ul>
	<li>If a positive integer is encountered, prepend it to the **front** of `seen`.</li>
	<li>If `-1` is encountered, let `k` be the number of **consecutive** `-1`s seen so far (including the current `-1`),
	<ul>
		<li>If `k` is less than or equal to the length of `seen`, append the `k`-th element of `seen` to `ans`.</li>
		<li>If `k` is strictly greater than the length of `seen`, append `-1` to `ans`.</li>
	</ul>
	</li>
</ul>

Return the array* *`ans`.
