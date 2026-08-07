## Description

You are given an integer array `nums`.

In one operation, you may choose **any** element `nums[i]` and perform one of the following:

	- **Multiply** `nums[i]` by an integer `k`, where `k >= 2`.

	- **Divide** `nums[i]` by an integer `k`, where `2 <= k < nums[i]`, provided that `nums[i]` is divisible by `k`.

Return the **minimum** number of operations required to make all elements of `nums` **equal**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [6,12,8]</span>

**Output:** 3

**Explanation:**

We can perform following operates to make all numbers to 6:

	- Divide `nums[1] = 12` by 2 to get 6.

	- Divide `nums[2] = 8` by 4 to get 2.

	- Multiply `nums[2] = 2` by 3 to get 6.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,15,20]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can perform following operates to make all numbers to 5:

	- Divide `nums[1] = 15` by 3 to get 5.

	- Divide `nums[2] = 20` by 4 to get 5.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,7,7]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

All elements are already equal, so no operations are needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^​​​​​​​9`
