## Description

You are given an integer array `nums` of length `n` and a 2D array `queries`, where `queries[i] = [l_i, r_i, val_i]`.

Each `queries[i]` represents the following action on `nums`:

<ul>
	<li>Select a <span data-keyword="subset">subset</span> of indices in the range `[l_i, r_i]` from `nums`.</li>
	<li>Decrement the value at each selected index by **exactly** `val_i`.</li>
</ul>

A **Zero Array** is an array with all its elements equal to 0.

Return the **minimum** possible **non-negative** value of `k`, such that after processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**. If no such `k` exists, return -1.
