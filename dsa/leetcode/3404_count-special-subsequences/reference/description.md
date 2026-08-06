## Description

You are given an array `nums` consisting of positive integers.

A **special subsequence** is defined as a <span data-keyword="subsequence-array">subsequence</span> of length 4, represented by indices `(p, q, r, s)`, where `p < q < r < s`. This subsequence **must** satisfy the following conditions:

<ul>
	<li>`nums[p] * nums[r] == nums[q] * nums[s]`</li>
	<li>There must be *at least* **one** element between each pair of indices. In other words, `q - p > 1`, `r - q > 1` and `s - r > 1`.</li>
</ul>

Return the *number* of different **special** **subsequences** in `nums`.
