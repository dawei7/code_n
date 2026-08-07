## Description

You are given an integer array `nums`.

You are allowed to replace **at most** one element in the array with any other integer value of your choice.

Return the length of the **longest non-decreasing <span data-keyword="subarray">subarray</span>** that can be obtained after performing at most one replacement.

An array is said to be **non-decreasing** if each element is greater than or equal to its previous one (if it exists).

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,1,2]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Replacing `nums[3] = 1` with 3 gives the array [1, 2, 3, 3, 2].

The longest non-decreasing subarray is [1, 2, 3, 3], which has a length of 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,2,2,2]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

All elements in `nums` are equal, so it is already non-decreasing and the entire `nums` forms a subarray of length 5.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`​​​​​​​
