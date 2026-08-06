## Description

You are given an integer array `nums`.

Your task is to find the number of pairs of **non-empty** <span data-keyword="subsequence-array">subsequences</span> `(seq1, seq2)` of `nums` that satisfy the following conditions:

<ul>
	<li>The subsequences `seq1` and `seq2` are **disjoint**, meaning **no index** of `nums` is common between them.</li>
	<li>The <span data-keyword="gcd-function">GCD</span> of the elements of `seq1` is equal to the GCD of the elements of `seq2`.</li>
</ul>

Return the total number of such pairs.

Since the answer may be very large, return it **modulo** `10^9 + 7`.
