## Description

You are given an integer array `nums` where `nums` is **<span data-keyword="strictly-increasing-array">strictly increasing</span>**.

For each index `x`, let `closest(x)` be the **adjacent** index `y` such that `abs(nums[x] - nums[y])` is **minimized**. If both **adjacent** indices exist and give the same difference, choose the **smaller** index.

From any index `x`, you can move in two ways:

<ul>
	<li>To any index `y` with cost `abs(nums[x] - nums[y])`, or</li>
	<li>To `closest(x)` with cost 1.</li>
</ul>

You are also given a 2D integer array `queries`, where each `queries[i] = [l_i, r_i]`.

For each query, calculate the **minimum total cost** to move from index `l_i` to index `r_i`.

Return an integer array `ans`, where `ans[i]` is the answer for the `i^th` query.

The **absolute difference** between two values `x` and `y` is defined as `abs(x - y)`.
