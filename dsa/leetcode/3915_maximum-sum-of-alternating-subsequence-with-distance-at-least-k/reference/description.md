## Description

You are given an integer array `nums` of length `n` and an integer `k`.

Pick a **<span data-keyword="subsequence-sequence">subsequence</span>** with indices `0 <= i_1 < i_2 < ... < i_m < n` such that:

<ul>
	<li>For every `1 <= t < m`, `i_t+1 - i_t >= k`.</li>
	<li>The selected values form a **strictly alternating** sequence. In other words, either:
	<ul>
		<li>`nums[i_1] < nums[i_2] > nums[i_3] < ...`, or</li>
		<li>`nums[i_1] > nums[i_2] < nums[i_3] > ...`</li>
	</ul>
	</li>
</ul>

A **subsequence** of length 1 is also considered **strictly** alternating. The score of a **valid** subsequence is the **sum** of its selected values.

Return an integer denoting the **maximum** possible **score** of a valid subsequence.
