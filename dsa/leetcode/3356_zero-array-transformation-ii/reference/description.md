## Description

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [l_i, r_i, val_i]`.

Each `queries[i]` represents the following action on `nums`:

<ul>
	<li>Decrement the value at each index in the range `[l_i, r_i]` in `nums` by **at most** `val_i`.</li>
	<li>The amount by which each value is decremented<!-- notionvc: b232c9d9-a32d-448c-85b8-b637de593c11 --> can be chosen **independently** for each index.</li>
</ul>

A **Zero Array** is an array with all its elements equal to 0.

Return the **minimum** possible **non-negative** value of `k`, such that after processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**. If no such `k` exists, return -1.
