## Description

You are given an integer array `nums` and two integers `k` and `numOperations`.

You must perform an **operation** `numOperations` times on `nums`, where in each operation you:

<ul>
	<li>Select an index `i` that was **not** selected in any previous operations.</li>
	<li>Add an integer in the range `[-k, k]` to `nums[i]`.</li>
</ul>

Return the **maximum** possible <span data-keyword="frequency-array">frequency</span> of any element in `nums` after performing the **operations**.
