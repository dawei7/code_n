## Description

You are given two integer arrays `nums1` and `nums0`, each of size `n`.

<ul>
	<li>`nums1[i]` represents the number of `'1'`s in the `i^th` segment.</li>
	<li>`nums0[i]` represents the number of `'0'`s in the `i^th` segment.</li>
</ul>

For each index `i`, construct a binary segment consisting of:

<ul>
	<li>`nums1[i]` occurrences of `'1'` followed by</li>
	<li>`nums0[i]` occurrences of `'0'`.</li>
</ul>

You may **rearrange** the order of these **segments** in any way. After rearranging, **concatenate** all segments to form a single binary string.

Return the **maximum** possible integer value of the concatenated binary string.

Since the result can be very large, return the answer **modulo** `10^9 + 7`.
