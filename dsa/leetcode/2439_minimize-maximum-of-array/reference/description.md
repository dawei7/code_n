## Description

You are given a **0-indexed** array `nums` comprising of `n` non-negative integers.

In one operation, you must:

<ul>
	<li>Choose an integer `i` such that `1 <= i < n` and `nums[i] > 0`.</li>
	<li>Decrease `nums[i]` by 1.</li>
	<li>Increase `nums[i - 1]` by 1.</li>
</ul>

Return* the **minimum** possible value of the **maximum** integer of *`nums`* after performing **any** number of operations*.
