## Description

You are given two **0-indexed** integer arrays `nums1` and `nums2` of equal length `n` and a positive integer `k`. You must choose a **subsequence** of indices from `nums1` of length `k`.

For chosen indices `i_0`, `i_1`, ..., `i_k - 1`, your **score** is defined as:

<ul>
	<li>The sum of the selected elements from `nums1` multiplied with the **minimum** of the selected elements from `nums2`.</li>
	<li>It can defined simply as: `(nums1[i_0] + nums1[i_1] +...+ nums1[i_k - 1]) * min(nums2[i_0] , nums2[i_1], ... ,nums2[i_k - 1])`.</li>
</ul>

Return *the **maximum** possible score.*

A **subsequence** of indices of an array is a set that can be derived from the set `{0, 1, ..., n-1}` by deleting some or no elements.
