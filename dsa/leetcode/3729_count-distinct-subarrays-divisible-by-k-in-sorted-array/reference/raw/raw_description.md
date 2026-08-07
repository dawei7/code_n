## Description

You are given an integer array `nums` **sorted** in **non-descending** order and a positive integer `k`.

A **<span data-keyword="subarray-nonempty">subarray</span>** of `nums` is **good** if the sum of its elements is **divisible** by `k`.

Return an integer denoting the number of **distinct** **good** subarrays of `nums`.

Subarrays are **distinct** if their sequences of values are. For example, there are 3 **distinct** subarrays in `[1, 1, 1]`, namely `[1]`, `[1, 1]`, and `[1, 1, 1]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], k = 3</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The good subarrays are `[1, 2]`, `[3]`, and `[1, 2, 3]`. For example, `[1, 2, 3]` is good because the sum of its elements is `1 + 2 + 3 = 6`, and `6 % k = 6 % 3 = 0`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,2,2,2,2], k = 6</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The good subarrays are `[2, 2, 2]` and `[2, 2, 2, 2, 2, 2]`. For example, `[2, 2, 2]` is good because the sum of its elements is `2 + 2 + 2 = 6`, and `6 % k = 6 % 6 = 0`.

Note that `[2, 2, 2]` is counted only once.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `nums` is sorted in non-descending order.

	- `1 <= k <= 10^9`
