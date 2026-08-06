## Description

You are given two integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively, and an integer `k`.

You must choose **exactly** `k` pairs of indices `(i_1, j_1), (i_2, j_2), ..., (i_k, j_k)` such that:

<ul>
	<li>`0 <= i_1 < i_2 < ... < i_k < n`</li>
	<li>`0 <= j_1 < j_2 < ... < j_k < m`</li>
</ul>

For each chosen pair `(i, j)`, you gain a score of `nums1[i] * nums2[j]`.

The total **score** is the **sum** of the products of all selected pairs.

Return an integer representing the **maximum** achievable total score.
