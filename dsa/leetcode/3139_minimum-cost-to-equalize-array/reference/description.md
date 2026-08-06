## Description

You are given an integer array `nums` and two integers `cost1` and `cost2`. You are allowed to perform **either** of the following operations **any** number of times:

<ul>
	<li>Choose an index `i` from `nums` and **increase** `nums[i]` by `1` for a cost of `cost1`.</li>
	<li>Choose two **different** indices `i`, `j`, from `nums` and **increase** `nums[i]` and `nums[j]` by `1` for a cost of `cost2`.</li>
</ul>

Return the **minimum** **cost** required to make all elements in the array **equal***. *

Since the answer may be very large, return it **modulo** `10^9 + 7`.
