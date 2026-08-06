## Description

You are given an integer `n` and a 2D array `requirements`, where `requirements[i] = [end_i, cnt_i]` represents the end index and the **inversion** count of each requirement.

A pair of indices `(i, j)` from an integer array `nums` is called an **inversion** if:

<ul>
	<li>`i < j` and `nums[i] > nums[j]`</li>
</ul>

Return the number of <span data-keyword="permutation">permutations</span> `perm` of `[0, 1, 2, ..., n - 1]` such that for **all** `requirements[i]`, `perm[0..end_i]` has exactly `cnt_i` inversions.

Since the answer may be very large, return it **modulo** `10^9 + 7`.
