## Description

You are given a **0-indexed** array `nums` of `n` integers and an integer `target`.

You are initially positioned at index `0`. In one step, you can jump from index `i` to any index `j` such that:

<ul>
	<li>`0 <= i < j < n`</li>
	<li>`-target <= nums[j] - nums[i] <= target`</li>
</ul>

Return *the **maximum number of jumps** you can make to reach index* `n - 1`.

If there is no way to reach index `n - 1`, return `-1`.
