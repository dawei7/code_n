## Description

You are given two integer arrays, `nums` and `cost`, of the same size, and an integer `k`.

You can divide `nums` into <span data-keyword="subarray-nonempty">subarrays</span>. The cost of the `i^th` subarray consisting of elements `nums[l..r]` is:

<ul>
	<li>`(nums[0] + nums[1] + ... + nums[r] + k * i) * (cost[l] + cost[l + 1] + ... + cost[r])`.</li>
</ul>

**Note** that `i` represents the order of the subarray: 1 for the first subarray, 2 for the second, and so on.

Return the **minimum** total cost possible from any valid division.
