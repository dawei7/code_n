## Description

You are given an integer array `nums` of length `n` and an integer `p`.

A **non-empty <span data-keyword="subsequence-sequence">subsequence</span>** of `nums` is called **good** if:

<ul>
	<li>Its length is **strictly less** than `n`.</li>
	<li>The **greatest common divisor (GCD)** of its elements is **exactly** `p`.</li>
</ul>

You are also given a 2D integer array `queries` of length `q`, where each `queries[i] = [ind_i, val_i]` indicates that you should update `nums[ind_i]` to `val_i`.

After each query, determine whether there exists **any good subsequence** in the current array.

Return the **number** of queries for which a **good subsequence** exists.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.
