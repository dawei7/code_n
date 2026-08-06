## Description

Given an integer array `nums`, your goal is to make all elements in `nums` equal. To complete one operation, follow these steps:

<ol>
	<li>Find the **largest** value in `nums`. Let its index be `i` (**0-indexed**) and its value be `largest`. If there are multiple elements with the largest value, pick the smallest `i`.</li>
	<li>Find the **next largest** value in `nums` **strictly smaller** than `largest`. Let its value be `nextLargest`.</li>
	<li>Reduce `nums[i]` to `nextLargest`.</li>
</ol>

Return *the number of operations to make all elements in *`nums`* equal*.
