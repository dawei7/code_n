## Description

You are given a **binary** string `s` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

<ul>
	<li>The number of `0`'s in the string is at most `k`.</li>
	<li>The number of `1`'s in the string is at most `k`.</li>
</ul>

Return an integer array `answer`, where `answer[i]` is the number of <span data-keyword="substring-nonempty">substrings</span> of `s[l_i..r_i]` that satisfy the **k-constraint**.
