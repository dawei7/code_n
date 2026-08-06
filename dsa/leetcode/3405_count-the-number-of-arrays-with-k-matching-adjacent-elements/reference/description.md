## Description

You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is defined as follows:

<ul>
	<li>Each element in `arr` is in the **inclusive** range `[1, m]`.</li>
	<li>*Exactly* `k` indices `i` (where `1 <= i < n`) satisfy the condition `arr[i - 1] == arr[i]`.</li>
</ul>

Return the number of **good arrays** that can be formed.

Since the answer may be very large, return it **modulo **`10^9 + 7`.
