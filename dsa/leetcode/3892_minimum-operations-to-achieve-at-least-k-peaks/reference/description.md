## Description

You are given a ​​​​​​​circular integer array​​​​​​​ `nums` of length `n`.

An index `i` is a **peak** if its value is **strictly greater** than its neighbors:

<ul>
	<li>The **previous** neighbor of `i` is `nums[i - 1]` if `i > 0`, otherwise `nums[n - 1]`.</li>
	<li>The **next** neighbor of `i` is `nums[i + 1]` if `i < n - 1`, otherwise `nums[0]`.</li>
</ul>

You are allowed to perform the following operation **any** number of times:

<ul>
	<li>Choose any index `i` and **increase** `nums[i]` by 1.</li>
</ul>

Return an integer denoting the **minimum** number of operations required to make the array contain **at least** `k` peaks. If it is impossible, return -1.
