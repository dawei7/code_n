## Description

You are playing a game involving a **circular** array of non-zero integers `nums`. Each `nums[i]` denotes the number of indices forward/backward you must move if you are located at index `i`:

<ul>
	<li>If `nums[i]` is positive, move `nums[i]` steps **forward**, and</li>
	<li>If `nums[i]` is negative, move `abs(nums[i])` steps **backward**.</li>
</ul>

Since the array is **circular**, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A **cycle** in the array consists of a sequence of indices `seq` of length `k` where:

<ul>
	<li>Following the movement rules above results in the repeating index sequence `seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...`</li>
	<li>Every `nums[seq[j]]` is either **all positive** or **all negative**.</li>
	<li>`k > 1`</li>
</ul>

Return `true`* if there is a **cycle** in *`nums`*, or *`false`* otherwise*.
