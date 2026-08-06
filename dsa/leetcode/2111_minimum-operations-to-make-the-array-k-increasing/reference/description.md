## Description

You are given a **0-indexed** array `arr` consisting of `n` positive integers, and a positive integer `k`.

The array `arr` is called **K-increasing** if `arr[i-k] <= arr[i]` holds for every index `i`, where `k <= i <= n-1`.

<ul>
	<li>For example, `arr = [4, 1, 5, 2, 6, 2]` is K-increasing for `k = 2` because:

	<ul>
		<li>`arr[0] <= arr[2] (4 <= 5)`</li>
		<li>`arr[1] <= arr[3] (1 <= 2)`</li>
		<li>`arr[2] <= arr[4] (5 <= 6)`</li>
		<li>`arr[3] <= arr[5] (2 <= 2)`</li>
	</ul>
	</li>
	<li>However, the same `arr` is not K-increasing for `k = 1` (because `arr[0] > arr[1]`) or `k = 3` (because `arr[0] > arr[3]`).</li>
</ul>

In one **operation**, you can choose an index `i` and **change** `arr[i]` into **any** positive integer.

Return *the **minimum number of operations** required to make the array K-increasing for the given *`k`.
