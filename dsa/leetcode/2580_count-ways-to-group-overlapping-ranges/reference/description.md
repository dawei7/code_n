## Description

You are given a 2D integer array `ranges` where `ranges[i] = [start_i, end_i]` denotes that all integers between `start_i` and `end_i` (both **inclusive**) are contained in the `i^th` range.

You are to split `ranges` into **two** (possibly empty) groups such that:

<ul>
	<li>Each range belongs to exactly one group.</li>
	<li>Any two **overlapping** ranges must belong to the **same** group.</li>
</ul>

Two ranges are said to be **overlapping** if there exists at least **one** integer that is present in both ranges.

<ul>
	<li>For example, `[1, 3]` and `[2, 5]` are overlapping because `2` and `3` occur in both ranges.</li>
</ul>

Return *the **total number** of ways to split* `ranges` *into two groups*. Since the answer may be very large, return it **modulo** `10^9 + 7`.
