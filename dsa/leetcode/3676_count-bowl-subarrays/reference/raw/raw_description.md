## Description

You are given an integer array `nums` with **distinct** elements.

A <span data-keyword="subarray">subarray</span> `nums[l...r]` of `nums` is called a **bowl** if:

	- The subarray has length at least 3. That is, `r - l + 1 >= 3`.

	- The **minimum** of its two ends is **strictly greater** than the **maximum** of all elements in between. That is, `min(nums[l], nums[r]) > max(nums[l + 1], ..., nums[r - 1])`.

Return the number of **bowl** subarrays in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,5,3,1,4]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The bowl subarrays are `[3, 1, 4]` and `[5, 3, 1, 4]`.

	- `[3, 1, 4]` is a bowl because `min(3, 4) = 3 > max(1) = 1`.

	- `[5, 3, 1, 4]` is a bowl because `min(5, 4) = 4 > max(3, 1) = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,1,2,3,4]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The bowl subarrays are `[5, 1, 2]`, `[5, 1, 2, 3]` and `[5, 1, 2, 3, 4]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = </span>[1000000000,999999999,999999998]

**Output:** <span class="example-io">0</span>

**Explanation:**

No subarray is a bowl.

</div>

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `nums` consists of distinct elements.
