## Description

You are given a **0-indexed** array of non-negative integers `nums`. For each integer in `nums`, you must find its respective **second greater** integer.

The **second greater** integer of `nums[i]` is `nums[j]` such that:

<ul>
	<li>`j > i`</li>
	<li>`nums[j] > nums[i]`</li>
	<li>There exists **exactly one** index `k` such that `nums[k] > nums[i]` and `i < k < j`.</li>
</ul>

If there is no such `nums[j]`, the second greater integer is considered to be `-1`.

<ul>
	<li>For example, in the array `[1, 2, 4, 3]`, the second greater integer of `1` is `4`, `2` is `3`, and that of `3` and `4` is `-1`.</li>
</ul>

Return* an integer array *`answer`*, where *`answer[i]`* is the second greater integer of *`nums[i]`*.*
