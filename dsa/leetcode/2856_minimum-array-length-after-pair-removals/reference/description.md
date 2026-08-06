## Description

Given an integer array `num` sorted in non-decreasing order.

You can perform the following operation any number of times:

<ul>
	<li>Choose **two** indices, `i` and `j`, where `nums[i] < nums[j]`.</li>
	<li>Then, remove the elements at indices `i` and `j` from `nums`. The remaining elements retain their original order, and the array is re-indexed.</li>
</ul>

Return the **minimum** length of `nums` after applying the operation zero or more times.
