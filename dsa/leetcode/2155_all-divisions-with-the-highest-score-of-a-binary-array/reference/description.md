## Description

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i` (where `0 <= i <= n)` into two arrays (possibly empty) `nums_left` and `nums_right`:

<ul>
	<li>`nums_left` has all the elements of `nums` between index `0` and `i - 1` **(inclusive)**, while `nums_right` has all the elements of nums between index `i` and `n - 1` **(inclusive)**.</li>
	<li>If `i == 0`, `nums_left` is **empty**, while `nums_right` has all the elements of `nums`.</li>
	<li>If `i == n`, `nums_left` has all the elements of nums, while `nums_right` is **empty**.</li>
</ul>

The **division score** of an index `i` is the **sum** of the number of `0`'s in `nums_left` and the number of `1`'s in `nums_right`.

Return ***all distinct indices</strong> that have the **highest** possible **division score***. You may return the answer in <strong>any order**.
