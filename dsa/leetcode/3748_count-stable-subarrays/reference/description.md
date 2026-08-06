## Description

You are given an integer array `nums`.

A **<span data-keyword="subarray-nonempty">subarray</span>** of `nums` is called **stable** if it contains **no inversions**, i.e., there is no pair of indices `i < j` such that `nums[i] > nums[j]`.

You are also given a **2D integer array** `queries` of length `q`, where each `queries[i] = [l_i, r_i]` represents a query. For each query `[l_i, r_i]`, compute the number of **stable subarrays** that lie entirely within the segment `nums[l_i..r_i]`.

Return an integer array `ans` of length `q`, where `ans[i]` is the answer to the `i^th` query.​​​​​​​​​​​​​​

**Note**:

<ul>
	<li>A single element subarray is considered stable.</li>
</ul>
