## Description

You are given an array of integers `nums` and an integer `k`.

Return the **maximum** sum of a <span data-keyword="subarray-nonempty">subarray</span> of `nums`, such that the size of the subarray is **divisible** by `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2], k = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The subarray `[1, 2]` with sum 3 has length equal to 2 which is divisible by 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-1,-2,-3,-4,-5], k = 4</span>

**Output:** <span class="example-io">-10</span>

**Explanation:**

The maximum sum subarray is `[-1, -2, -3, -4]` which has length equal to 4 which is divisible by 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-5,1,2,-3,4], k = 2</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The maximum sum subarray is `[1, 2, -3, 4]` which has length equal to 4 which is divisible by 2.

</div>

**Constraints:**

	- `1 <= k <= nums.length <= 2 * 10^5`

	- `-10^9 <= nums[i] <= 10^9`
