## Description

You are given two arrays, `nums` and `target`.

In a single operation, you may increment any element of `nums` by 1.

Return **the minimum number** of operations required so that each element in `target` has **at least** one multiple in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], target = [4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The minimum number of operations required to satisfy the condition is 1.

	- Increment 3 to 4 with just one operation, making 4 a multiple of itself.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [8,4], target = [10,5]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The minimum number of operations required to satisfy the condition is 2.

	- Increment 8 to 10 with 2 operations, making 10 a multiple of both 5 and 10.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,9,10], target = [7]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Target 7 already has a multiple in nums, so no additional operations are needed.

</div>

**Constraints:**

	- `1 <= nums.length <= 5 * 10^4`

	- `1 <= target.length <= 4`

	- `target.length <= nums.length`

	- `1 <= nums[i], target[i] <= 10^4`
