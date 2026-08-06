## Description

Your country has 10^9 lakes. Initially, all the lakes are empty, but when it rains over the `n^th` lake, the `n^th` lake becomes full of water. If it rains over a lake that is **full of water**, there will be a **flood**. Your goal is to avoid floods in any lake.

Given an integer array `rains` where:

<ul>
	<li>`rains[i] > 0` means there will be rains over the `rains[i]` lake.</li>
	<li>`rains[i] == 0` means there are no rains this day and you **must** choose **one lake** this day and **dry it**.</li>
</ul>

Return *an array `ans`* where:

<ul>
	<li>`ans.length == rains.length`</li>
	<li>`ans[i] == -1` if `rains[i] > 0`.</li>
	<li>`ans[i]` is the lake you choose to dry in the `ith` day if `rains[i] == 0`.</li>
</ul>

If there are multiple valid answers return **any** of them. If it is impossible to avoid flood return **an empty array**.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.
