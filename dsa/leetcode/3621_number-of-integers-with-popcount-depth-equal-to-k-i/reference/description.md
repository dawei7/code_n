## Description

You are given two integers `n` and `k`.

For any positive integer `x`, define the following sequence:

<ul>
	<li>`p_0 = x`</li>
	<li>`p_i+1 = popcount(p_i)` for all `i >= 0`, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.</li>
</ul>

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer `d >= 0` such that `p_d = 1`.

For example, if `x = 7` (binary representation `"111"`). Then, the sequence is: `7 → 3 → 2 → 1`, so the popcount-depth of 7 is 3.

Your task is to determine the number of integers in the range `[1, n]` whose popcount-depth is **exactly** equal to `k`.

Return the number of such integers.
