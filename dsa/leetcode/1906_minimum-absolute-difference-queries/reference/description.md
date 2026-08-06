## Description

The **minimum absolute difference** of an array `a` is defined as the **minimum value** of `|a[i] - a[j]|`, where `0 <= i < j < a.length` and `a[i] != a[j]`. If all elements of `a` are the **same**, the minimum absolute difference is `-1`.

<ul>
	<li>For example, the minimum absolute difference of the array `[5,<u>2</u>,<u>3</u>,7,2]` is `|2 - 3| = 1`. Note that it is not `0` because `a[i]` and `a[j]` must be different.</li>
</ul>

You are given an integer array `nums` and the array `queries` where `queries[i] = [l_i, r_i]`. For each query `i`, compute the **minimum absolute difference** of the **subarray** `nums[l_i...r_i]` containing the elements of `nums` between the **0-based** indices `l_i` and `r_i` (**inclusive**).

Return *an **array** *`ans` *where* `ans[i]` *is the answer to the* `i^th` *query*.

A **subarray** is a contiguous sequence of elements in an array.

The value of `|x|` is defined as:

<ul>
	<li>`x` if `x >= 0`.</li>
	<li>`-x` if `x < 0`.</li>
</ul>
