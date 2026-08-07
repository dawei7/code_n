## Description

You are given an integer array `nums`.

An element `nums[i]` is considered **valid** if it satisfies **at least** one of the following conditions:

	- It is **strictly greater** than every element to its left.

	- It is **strictly greater** than every element to its right.

The first and last elements are always valid.

Return an array of all valid elements in the same order as they appear in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,4,2,3,2]</span>

**Output:** <span class="example-io">[1,2,4,3,2]</span>

**Explanation:**

	- `nums[0]` and `nums[5]` are always valid.

	- `nums[1]` and `nums[2]` are strictly greater than every element to their left.

	- `nums[4]` is strictly greater than every element to its right.

	- Thus, the answer is `[1, 2, 4, 3, 2]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,5,5,5]</span>

**Output:** <span class="example-io">[5,5]</span>

**Explanation:**

	- The first and last elements are always valid.

	- No other elements are strictly greater than all elements to their left or to their right.

	- Thus, the answer is `[5, 5]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">[1]</span>

**Explanation:**

Since there is only one element, it is always valid. Thus, the answer is `[1]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
