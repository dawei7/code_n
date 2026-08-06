## Description

You are given an integer array `nums`.

You must **repeatedly** apply the following merge operation until no more changes can be made:

<ul>
	<li>If any **two adjacent elements are equal**, choose the **leftmost** such adjacent pair in the current array and replace them with a single element equal to their **sum**.</li>
</ul>

After each merge operation, the array size **decreases** by 1. Repeat the process on the updated array until no more changes can be made.

Return the final array after all possible merge operations.
