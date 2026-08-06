## Description

You are given an integer array `nums` of length `n` which represents a permutation of all the integers in the range `[0, n - 1]`.

The number of **global inversions** is the number of the different pairs `(i, j)` where:

<ul>
	<li>`0 <= i < j < n`</li>
	<li>`nums[i] > nums[j]`</li>
</ul>

The number of **local inversions** is the number of indices `i` where:

<ul>
	<li>`0 <= i < n - 1`</li>
	<li>`nums[i] > nums[i + 1]`</li>
</ul>

Return `true` *if the number of **global inversions** is equal to the number of **local inversions***.
