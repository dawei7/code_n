## Description

You are given an integer array `nums`.

A **special triplet** is defined as a triplet of indices `(i, j, k)` such that:

<ul>
	<li>`0 <= i < j < k < n`, where `n = nums.length`</li>
	<li>`nums[i] == nums[j] * 2`</li>
	<li>`nums[k] == nums[j] * 2`</li>
</ul>

Return the total number of **special triplets** in the array.

Since the answer may be large, return it **modulo** `10^9 + 7`.
