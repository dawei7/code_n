## Description

You are given a **0-indexed** array `nums` consisting of `n` positive integers.

The array `nums` is called **alternating** if:

<ul>
	<li>`nums[i - 2] == nums[i]`, where `2 <= i <= n - 1`.</li>
	<li>`nums[i - 1] != nums[i]`, where `1 <= i <= n - 1`.</li>
</ul>

In one **operation**, you can choose an index `i` and **change** `nums[i]` into **any** positive integer.

Return *the **minimum number of operations** required to make the array alternating*.
