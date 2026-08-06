## Description

You are given a **1-indexed** array of integers `nums` of length `n`.

We define a function `greaterCount` such that `greaterCount(arr, val)` returns the number of elements in `arr` that are **strictly greater** than `val`.

You need to distribute all the elements of `nums` between two arrays `arr1` and `arr2` using `n` operations. In the first operation, append `nums[1]` to `arr1`. In the second operation, append `nums[2]` to `arr2`. Afterwards, in the `i^th` operation:

<ul>
	<li>If `greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i])`, append `nums[i]` to `arr1`.</li>
	<li>If `greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i])`, append `nums[i]` to `arr2`.</li>
	<li>If `greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i])`, append `nums[i]` to the array with a **lesser** number of elements.</li>
	<li>If there is still a tie, append `nums[i]` to `arr1`.</li>
</ul>

The array `result` is formed by concatenating the arrays `arr1` and `arr2`. For example, if `arr1 == [1,2,3]` and `arr2 == [4,5,6]`, then `result = [1,2,3,4,5,6]`.

Return *the integer array* `result`.
