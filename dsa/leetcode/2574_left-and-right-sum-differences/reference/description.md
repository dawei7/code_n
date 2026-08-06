## Description

You are given a **0-indexed** integer array `nums` of size `n`.

Define two arrays `leftSum` and `rightSum` where:

<ul>
	<li>`leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`.</li>
	<li>`rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.</li>
</ul>

Return an integer array `answer` of size `n` where `answer[i] = |leftSum[i] - rightSum[i]|`.
