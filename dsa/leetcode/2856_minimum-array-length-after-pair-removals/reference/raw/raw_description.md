## Description

Given an integer array `num` sorted in non-decreasing order.

You can perform the following operation any number of times:

	- Choose **two** indices, `i` and `j`, where `nums[i] < nums[j]`.

	- Then, remove the elements at indices `i` and `j` from `nums`. The remaining elements retain their original order, and the array is re-indexed.

Return the **minimum** length of `nums` after applying the operation zero or more times.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

![](images/tcase1.gif)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,2,2,3,3]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

![](images/tcase2.gif)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1000000000,1000000000]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Since both numbers are equal, they cannot be removed.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,4,4,4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/tcase3.gif)

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `nums` is sorted in **non-decreasing** order.
