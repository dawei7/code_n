## Description

You are given a **0-indexed** integer array `nums` and an integer `threshold`.

Find the length of the **longest subarray** of `nums` starting at index `l` and ending at index `r` `(0 <= l <= r < nums.length)` that satisfies the following conditions:

<ul>
	<li>`nums[l] % 2 == 0`</li>
	<li>For all indices `i` in the range `[l, r - 1]`, `nums[i] % 2 != nums[i + 1] % 2`</li>
	<li>For all indices `i` in the range `[l, r]`, `nums[i] <= threshold`</li>
</ul>

Return *an integer denoting the length of the longest such subarray.*

**Note:** A **subarray** is a contiguous non-empty sequence of elements within an array.
