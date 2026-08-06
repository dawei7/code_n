## Description

You are given an integer array `nums` with **distinct** elements.

A <span data-keyword="subarray">subarray</span> `nums[l...r]` of `nums` is called a **bowl** if:

<ul>
	<li>The subarray has length at least 3. That is, `r - l + 1 >= 3`.</li>
	<li>The **minimum** of its two ends is **strictly greater** than the **maximum** of all elements in between. That is, `min(nums[l], nums[r]) > max(nums[l + 1], ..., nums[r - 1])`.</li>
</ul>

Return the number of **bowl** subarrays in `nums`.
