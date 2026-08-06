## Description

The **imbalance number** of a **0-indexed** integer array `arr` of length `n` is defined as the number of indices in `sarr = sorted(arr)` such that:

<ul>
	<li>`0 <= i < n - 1`, and</li>
	<li>`sarr[i+1] - sarr[i] > 1`</li>
</ul>

Here, `sorted(arr)` is the function that returns the sorted version of `arr`.

Given a **0-indexed** integer array `nums`, return *the **sum of imbalance numbers** of all its **subarrays***.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.
