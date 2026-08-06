## Description

Given an array `nums` of `n` integers and an integer `k`, determine whether there exist **two** **adjacent** <span data-keyword="subarray-nonempty">subarrays</span> of length `k` such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays starting at indices `a` and `b` (`a < b`), where:

<ul>
	<li>Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.</li>
	<li>The subarrays must be **adjacent**, meaning `b = a + k`.</li>
</ul>

Return `true` if it is *possible* to find **two **such subarrays, and `false` otherwise.
