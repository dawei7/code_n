## Description

You are given an array `nums` of `n` positive integers and an integer `k`.

Initially, you start with a score of `1`. You have to maximize your score by applying the following operation at most `k` times:

<ul>
	<li>Choose any **non-empty** subarray `nums[l, ..., r]` that you haven't chosen previously.</li>
	<li>Choose an element `x` of `nums[l, ..., r]` with the highest **prime score**. If multiple such elements exist, choose the one with the smallest index.</li>
	<li>Multiply your score by `x`.</li>
</ul>

Here, `nums[l, ..., r]` denotes the subarray of `nums` starting at index `l` and ending at the index `r`, both ends being inclusive.

The **prime score** of an integer `x` is equal to the number of distinct prime factors of `x`. For example, the prime score of `300` is `3` since `300 = 2 * 2 * 3 * 5 * 5`.

Return *the **maximum possible score** after applying at most *`k`* operations*.

Since the answer may be large, return it modulo `10^9 + 7`.
