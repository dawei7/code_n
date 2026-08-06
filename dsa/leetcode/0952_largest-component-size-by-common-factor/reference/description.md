## Description

You are given an integer array of unique positive integers `nums`. Consider the following graph:

<ul>
	<li>There are `nums.length` nodes, labeled `nums[0]` to `nums[nums.length - 1]`,</li>
	<li>There is an undirected edge between `nums[i]` and `nums[j]` if `nums[i]` and `nums[j]` share a common factor greater than `1`.</li>
</ul>

Return *the size of the largest connected component in the graph*.
