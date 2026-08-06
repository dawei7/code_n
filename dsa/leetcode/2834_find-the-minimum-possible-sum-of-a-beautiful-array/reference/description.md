## Description

You are given positive integers `n` and `target`.

An array `nums` is **beautiful** if it meets the following conditions:

<ul>
	<li>`nums.length == n`.</li>
	<li>`nums` consists of pairwise **distinct** **positive** integers.</li>
	<li>There doesn't exist two **distinct** indices, `i` and `j`, in the range `[0, n - 1]`, such that `nums[i] + nums[j] == target`.</li>
</ul>

Return *the **minimum** possible sum that a beautiful array could have modulo *`10^9 + 7`.
