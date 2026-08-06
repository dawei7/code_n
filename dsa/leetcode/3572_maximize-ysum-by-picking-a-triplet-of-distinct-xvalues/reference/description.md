## Description

You are given two integer arrays `x` and `y`, each of length `n`. You must choose three **distinct** indices `i`, `j`, and `k` such that:

<ul>
	<li>`x[i] != x[j]`</li>
	<li>`x[j] != x[k]`</li>
	<li>`x[k] != x[i]`</li>
</ul>

Your goal is to **maximize** the value of `y[i] + y[j] + y[k]` under these conditions. Return the **maximum** possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.
