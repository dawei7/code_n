## Description

Given an array of integers `nums` and an integer `k`, return the number of <span data-keyword="subarray-nonempty">subarrays</span> of `nums` where the bitwise `AND` of the elements of the subarray equals `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1], k = 1</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

All subarrays contain only 1's.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,2], k = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Subarrays having an `AND` value of 1 are: `[<u>**1**</u>,1,2]`, `[1,<u>**1**</u>,2]`, `[<u>**1,1**</u>,2]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], k = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Subarrays having an `AND` value of 2 are: `[1,**<u>2</u>**,3]`, `[1,<u>**2,3**</u>]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i], k <= 10^9`
