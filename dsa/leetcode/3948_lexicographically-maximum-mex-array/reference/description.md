## Description

You are given an integer array `nums`.

You want to construct an array `result` by repeatedly performing the following operation until `nums` becomes empty:

<ul>
	<li>Choose an integer `k` such that `1 <= k <= len(nums)`.</li>
	<li>Compute the **MEX** of the first `k` elements of `nums`.</li>
	<li>Append this **MEX** to `result`.</li>
	<li>Remove the first `k` elements from `nums`.</li>
</ul>

Return the **lexicographically maximum** array `result` that can be obtained after performing the operations.

The **MEX** of an array is the **smallest non-negative** integer not present in the array.

An array `a` is **lexicographically greater** than an array `b` if in the first position where `a` and `b` differ, array `a` has an element that is greater than the corresponding element in `b`. If the first `min(a.length, b.length)` elements do not differ, then the longer array is the **lexicographically greater** one.
