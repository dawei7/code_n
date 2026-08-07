## Description

You are given an integer array `nums`.

You are allowed to delete any number of elements from `nums` without making it **empty**. After performing the deletions, select a <span data-keyword="subarray-nonempty">subarray</span> of `nums` such that:

	- All elements in the subarray are **unique**.

	- The sum of the elements in the subarray is **maximized**.

Return the **maximum sum** of such a subarray.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5]</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

Select the entire array without deleting any element to obtain the maximum sum.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,0,1,1]</span>

**Output:** 1

**Explanation:**

Delete the element `nums[0] == 1`, `nums[1] == 1`, `nums[2] == 0`, and `nums[3] == 1`. Select the entire array `[1]` to obtain the maximum sum.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,-1,-2,1,0,-1]</span>

**Output:** 3

**Explanation:**

Delete the elements `nums[2] == -1` and `nums[3] == -2`, and select the subarray `[2, 1]` from `[1, 2, 1, 0, -1]` to obtain the maximum sum.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`
