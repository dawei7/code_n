## Description

Given an integer array `arr`, return *the length of a maximum size turbulent subarray of* `arr`.

A subarray is **turbulent** if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray `[arr[i], arr[i + 1], ..., arr[j]]` of `arr` is said to be turbulent if and only if:

<ul>
	<li>For `i <= k < j`:

	<ul>
		<li>`arr[k] > arr[k + 1]` when `k` is odd, and</li>
		<li>`arr[k] < arr[k + 1]` when `k` is even.</li>
	</ul>
	</li>
	<li>Or, for `i <= k < j`:
	<ul>
		<li>`arr[k] > arr[k + 1]` when `k` is even, and</li>
		<li>`arr[k] < arr[k + 1]` when `k` is odd.</li>
	</ul>
	</li>
</ul>
