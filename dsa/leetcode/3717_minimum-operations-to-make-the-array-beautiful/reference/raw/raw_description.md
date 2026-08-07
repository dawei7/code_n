## Description

You are given an integer array `nums`.

An array is called **beautiful** if for every index `i > 0`, the value at `nums[i]` is **divisible** by `nums[i - 1]`.

In one operation, you may **increment** any element `nums[i]` (with `i > 0`) by `1`.

Return the **minimum number of operations** required to make the array beautiful.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,7,9]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Applying the operation twice on `nums[1]` makes the array beautiful: `[3,9,9]`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The given array is already beautiful.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The array has only one element, so it's already beautiful.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 50​​​`
