## Description

You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`, extract the **<span data-keyword="substring-nonempty">substring</span>** `s[l_i..r_i]`. Then, perform the following:

<ul>
	<li>Form a new integer `x` by concatenating all the **non-zero digits** from the substring in their original order. If there are no non-zero digits, `x = 0`.</li>
	<li>Let `sum` be the **sum of digits** in `x`. The answer is `x * sum`.</li>
</ul>

Return an array of integers `answer` where `answer[i]` is the answer to the `i^th` query.

Since the answers may be very large, return them **modulo** `10^9 + 7`.
