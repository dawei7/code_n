## Description

You are given an `m x n` integer matrix `mat` and an integer `k`. The matrix rows are 0-indexed.

The following proccess happens `k` times:

<ul>
	<li>**Even-indexed** rows (0, 2, 4, ...) are cyclically shifted to the left.</li>
</ul>

<img src="https://assets.leetcode.com/uploads/2024/05/19/lshift.jpg" style="width: 283px; height: 90px;" />

<ul>
	<li>**Odd-indexed** rows (1, 3, 5, ...) are cyclically shifted to the right.</li>
</ul>

<img src="https://assets.leetcode.com/uploads/2024/05/19/rshift-stlone.jpg" style="width: 283px; height: 90px;" />

Return `true` if the final modified matrix after `k` steps is identical to the original matrix, and `false` otherwise.
