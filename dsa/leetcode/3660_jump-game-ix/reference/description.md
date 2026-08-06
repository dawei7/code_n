## Description

You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

<ul>
	<li>Jump to index `j` where `j > i` is allowed only if `nums[j] < nums[i]`.</li>
	<li>Jump to index `j` where `j < i` is allowed only if `nums[j] > nums[i]`.</li>
</ul>

For each index `i`, find the **maximum** **value** in `nums` that can be reached by following **any** sequence of valid jumps starting at `i`.

Return an array `ans` where `ans[i]` is the **maximum** **value** reachable starting from index `i`.
