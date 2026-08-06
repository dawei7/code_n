## Description

You are given an integer `n`. A **0-indexed** integer array `nums` of length `n + 1` is generated in the following way:

<ul>
	<li>`nums[0] = 0`</li>
	<li>`nums[1] = 1`</li>
	<li>`nums[2 * i] = nums[i]` when `2 <= 2 * i <= n`</li>
	<li>`nums[2 * i + 1] = nums[i] + nums[i + 1]` when `2 <= 2 * i + 1 <= n`</li>
</ul>

Return** ***the **maximum** integer in the array *`nums`​​​.
