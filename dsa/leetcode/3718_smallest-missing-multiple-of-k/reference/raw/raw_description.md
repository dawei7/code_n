## Description

Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A **multiple** of `k` is any positive integer divisible by `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [8,2,3,4,6], k = 2</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

The multiples of `k = 2` are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,7,10,15], k = 5</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The multiples of `k = 5` are 5, 10, 15, 20... and the smallest multiple missing from `nums` is 5.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 100`
