## Description

You are given a binary array `nums` (**0-indexed**).

We define `x_i` as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).

<ul>
	<li>For example, if `nums = [1,0,1]`, then `x_0 = 1`, `x_1 = 2`, and `x_2 = 5`.</li>
</ul>

Return *an array of booleans *`answer`* where *`answer[i]`* is *`true`* if *`x_i`* is divisible by *`5`.
