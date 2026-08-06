## Description

You are given a **0-indexed** integer array `nums` of size `n`, and a **0-indexed** integer array `pattern` of size `m` consisting of integers `-1`, `0`, and `1`.

A <span data-keyword="subarray">subarray</span> `nums[i..j]` of size `m + 1` is said to match the `pattern` if the following conditions hold for each element `pattern[k]`:

<ul>
	<li>`nums[i + k + 1] > nums[i + k]` if `pattern[k] == 1`.</li>
	<li>`nums[i + k + 1] == nums[i + k]` if `pattern[k] == 0`.</li>
	<li>`nums[i + k + 1] < nums[i + k]` if `pattern[k] == -1`.</li>
</ul>

Return *the** count** of subarrays in* `nums` *that match the* `pattern`.
