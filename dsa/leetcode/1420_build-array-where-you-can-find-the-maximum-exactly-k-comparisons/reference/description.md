## Description

You are given three integers `n`, `m` and `k`. Consider the following algorithm to find the maximum element of an array of positive integers:

<img alt="" src="https://assets.leetcode.com/uploads/2020/04/02/e.png" style="width: 424px; height: 372px;" />
You should build the array arr which has the following properties:

<ul>
	<li>`arr` has exactly `n` integers.</li>
	<li>`1 <= arr[i] <= m` where `(0 <= i < n)`.</li>
	<li>After applying the mentioned algorithm to `arr`, the value `search_cost` is equal to `k`.</li>
</ul>

Return *the number of ways* to build the array `arr` under the mentioned conditions. As the answer may grow large, the answer **must be** computed modulo `10^9 + 7`.
