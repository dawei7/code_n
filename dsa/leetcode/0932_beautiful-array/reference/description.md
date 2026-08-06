## Description

An array `nums` of length `n` is **beautiful** if:

<ul>
	<li>`nums` is a permutation of the integers in the range `[1, n]`.</li>
	<li>For every `0 <= i < j < n`, there is no index `k` with `i < k < j` where `2 * nums[k] == nums[i] + nums[j]`.</li>
</ul>

Given the integer `n`, return *any **beautiful** array *`nums`* of length *`n`. There will be at least one valid answer for the given `n`.
