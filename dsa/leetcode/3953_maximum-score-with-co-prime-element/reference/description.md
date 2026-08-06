## Description

You are given an integer array `nums` of length `n` and an integer `maxVal`.

You **may** change any element in `nums` to any positive integer **less than or equal** to `maxVal`. Each such change costs 1.

Two integers are **co-prime** if their <span data-keyword="gcd-function">**greatest common divisor (GCD)**</span> is 1.

After all modifications, you **must** choose an index `i` such that, `nums[i]` is **co-prime** with every other element `nums[j]`.

Let:

<ul>
	<li>`selectedValue` be the final value of `nums[i]` after modifications.</li>
	<li>`modificationCost` be the total number of elements changed.</li>
</ul>

The score is defined as `score = selectedValue - modificationCost`.

Return the **maximum** possible score.
