## Description

Given an array `nums`, return the number of <span data-keyword="subsequence-array">subsequences</span> with an odd sum of elements.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The odd-sum subsequences are: `[<u>**1**</u>, 1, 1]`, `[1, <u>**1**</u>, 1],` `[1, 1, <u>**1**</u>]`, `[<u>**1, 1, 1**</u>]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The odd-sum subsequences are: `[<u>**1**</u>, 2, 2]`, `[<u>**1, 2**</u>, 2],` `[<u>**1**</u>, 2, **<u>2</u>**]`, `[<u>**1, 2, 2**</u>]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`
