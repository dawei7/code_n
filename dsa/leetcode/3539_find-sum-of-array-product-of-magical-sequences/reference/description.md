## Description

You are given two integers, `m` and `k`, and an integer array `nums`.

A sequence of integers `seq` is called **magical** if:

<ul>
	<li>`seq` has a size of `m`.</li>
	<li>`0 <= seq[i] < nums.length`</li>
	<li>The **binary representation** of `2^seq[0] + 2^seq[1] + ... + 2^seq[m - 1]` has `k` **set bits**.</li>
</ul>

The **array product** of this sequence is defined as `prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]])`.

Return the **sum** of the **array products** for all valid **magical** sequences.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **set bit** refers to a bit in the binary representation of a number that has a value of 1.
