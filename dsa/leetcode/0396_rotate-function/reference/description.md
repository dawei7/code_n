## Description

You are given an integer array `nums` of length `n`.

Assume `arr_k` to be an array obtained by rotating `nums` by `k` positions clock-wise. We define the **rotation function** `F` on `nums` as follow:

<ul>
	<li>`F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1].`</li>
</ul>

Return *the maximum value of* `F(0), F(1), ..., F(n-1)`.

The test cases are generated so that the answer fits in a **32-bit** integer.
