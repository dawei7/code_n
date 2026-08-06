## Description

You are given an integer array `nums` of length `n`.

An integer `k` is called **sortable** if `k` **divides** `n` and you can sort `nums` in **non-decreasing** order by sequentially performing the following operations:

<ul>
	<li>Partition `nums` into **consecutive <span data-keyword="subarray-nonempty">subarrays</span>** of length `k`.</li>
	<li>**Cyclically rotate each subarray independently** any number of times to the left or to the right.</li>
</ul>

Return an integer denoting the sum of all possible sortable integers `k`.
