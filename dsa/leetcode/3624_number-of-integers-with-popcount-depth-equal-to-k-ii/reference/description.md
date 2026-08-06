## Description

You are given an integer array `nums`.

For any positive integer `x`, define the following sequence:

<ul>
	<li>`p_0 = x`</li>
	<li>`p_i+1 = popcount(p_i)` for all `i >= 0`, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.</li>
</ul>

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer `d >= 0` such that `p_d = 1`.

For example, if `x = 7` (binary representation `"111"`). Then, the sequence is: `7 → 3 → 2 → 1`, so the popcount-depth of 7 is 3.

You are also given a 2D integer array `queries`, where each `queries[i]` is either:

<ul>
	<li>`[1, l, r, k]` - **Determine** the number of indices `j` such that `l <= j <= r` and the **popcount-depth** of `nums[j]` is equal to `k`.</li>
	<li>`[2, idx, val]` - **Update** `nums[idx]` to `val`.</li>
</ul>

Return an integer array `answer`, where `answer[i]` is the number of indices for the `i^th` query of type `[1, l, r, k]`.
