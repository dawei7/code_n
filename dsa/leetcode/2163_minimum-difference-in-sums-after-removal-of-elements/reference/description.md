## Description

You are given a **0-indexed** integer array `nums` consisting of `3 * n` elements.

You are allowed to remove any **subsequence** of elements of size **exactly** `n` from `nums`. The remaining `2 * n` elements will be divided into two **equal** parts:

<ul>
	<li>The first `n` elements belonging to the first part and their sum is `sum_first`.</li>
	<li>The next `n` elements belonging to the second part and their sum is `sum_second`.</li>
</ul>

The **difference in sums** of the two parts is denoted as `sum_first - sum_second`.

<ul>
	<li>For example, if `sum_first = 3` and `sum_second = 2`, their difference is `1`.</li>
	<li>Similarly, if `sum_first = 2` and `sum_second = 3`, their difference is `-1`.</li>
</ul>

Return *the **minimum difference** possible between the sums of the two parts after the removal of *`n`* elements*.
