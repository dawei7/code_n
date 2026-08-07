## Description

You are given an integer array `nums`.

Return the **smallest** index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- For `nums[2] = 2`, the sum of digits is 2, which is equal to index `i = 2`. Thus, the output is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,10,11]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- For `nums[1] = 10`, the sum of digits is `1 + 0 = 1`, which is equal to index `i = 1`.

	- For `nums[2] = 11`, the sum of digits is `1 + 1 = 2`, which is equal to index `i = 2`.

	- Since index 1 is the smallest, the output is 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- Since no index satisfies the condition, the output is -1.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 1000`
