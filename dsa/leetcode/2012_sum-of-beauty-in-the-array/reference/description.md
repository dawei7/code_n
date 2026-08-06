## Description

You are given a **0-indexed** integer array `nums`. For each index `i` (`1 <= i <= nums.length - 2`) the **beauty** of `nums[i]` equals:

<ul>
	<li>`2`, if `nums[j] < nums[i] < nums[k]`, for **all** `0 <= j < i` and for **all** `i < k <= nums.length - 1`.</li>
	<li>`1`, if `nums[i - 1] < nums[i] < nums[i + 1]`, and the previous condition is not satisfied.</li>
	<li>`0`, if none of the previous conditions holds.</li>
</ul>

Return* the **sum of beauty** of all *`nums[i]`* where *`1 <= i <= nums.length - 2`.
