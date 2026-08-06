## Description

You are given a positive integer `p`. Consider an array `nums` (**1-indexed**) that consists of the integers in the **inclusive** range `[1, 2^p - 1]` in their binary representations. You are allowed to do the following operation **any** number of times:

<ul>
	<li>Choose two elements `x` and `y` from `nums`.</li>
	<li>Choose a bit in `x` and swap it with its corresponding bit in `y`. Corresponding bit refers to the bit that is in the **same position** in the other integer.</li>
</ul>

For example, if `x = 11<u>0</u>1` and `y = 00<u>1</u>1`, after swapping the `2^nd` bit from the right, we have `x = 11<u>1</u>1` and `y = 00<u>0</u>1`.

Find the **minimum non-zero** product of `nums` after performing the above operation **any** number of times. Return *this product****modulo***`10^9 + 7`.

**Note:** The answer should be the minimum product **before** the modulo operation is done.
