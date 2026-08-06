## Description

You are given an integer array `nums` of length `n`.

Alice and Bob are playing a game. Alice chooses:

<ul>
	<li>An integer `k` such that `k > 1`.</li>
	<li>Two integers `l` and `r` such that `0 <= l <= r < n`.</li>
</ul>

Initially, both Alice's and Bob's scores are 0.

For each index `i` in the range `[l, r]` (inclusive):

<ul>
	<li>If `nums[i]` is divisible by `k`, Alice's score **increases** by `nums[i]`.</li>
	<li>Otherwise, Bob's score **increases** by `nums[i]`.</li>
</ul>

The **score difference** is Alice's score **minus** Bob's score.

Alice wants to **maximize** the score difference. If there are multiple values of `k` that achieve the **maximum** score difference, she chooses the **smallest** such `k`.

Return the **product** of the **maximum** score difference and the chosen value of `k`. Since the result can be large, return it **modulo** `10^9 + 7`.
