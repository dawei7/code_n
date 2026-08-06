## Description

Given an array `nums` of `n` integers, your task is to find the **maximum** value of `k` for which there exist **two** adjacent <span data-keyword="subarray-nonempty">subarrays</span> of length `k` each, such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

<ul>
	<li>Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.</li>
	<li>The subarrays must be **adjacent**, meaning `b = a + k`.</li>
</ul>

Return the **maximum** *possible* value of `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.
