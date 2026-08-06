## Description

You are given an integer array `nums` of length `n` and an integer `k`.

A pair of indices `(i, j)` is called **valid** if:

<ul>
	<li>`0 <= i < j < n`</li>
	<li>`j - i >= k`</li>
</ul>

Return the **maximum** value of `nums[i] + nums[j]` among all valid pairs.
