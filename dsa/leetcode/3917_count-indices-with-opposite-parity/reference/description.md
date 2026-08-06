## Description

You are given an integer array `nums` of length `n`.

The **score** of an index `i` is defined as the number of indices `j` such that:

<ul>
	<li>`i < j < n`, and</li>
	<li>`nums[i]` and `nums[j]` have different parity (one is even and the other is odd).</li>
</ul>

Return an integer array `answer` of length `n`, where `answer[i]` is the score of index `i`.
