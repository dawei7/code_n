## Description

You are given an integer array `nums`. A **good **<span data-keyword="subsequence-array">subsequence</span> is defined as a subsequence of `nums` where the absolute difference between any **two** consecutive elements in the subsequence is **exactly** 1.

Return the **sum** of all *possible* **good subsequences** of `nums`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Note **that a subsequence of size 1 is considered good by definition.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1]</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

	- Good subsequences are: `[1]`, `[2]`, `[1]`, `[1,2]`, `[2,1]`, `[1,2,1]`.

	- The sum of elements in these subsequences is 14.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,4,5]</span>

**Output:** <span class="example-io">40</span>

**Explanation:**

	- Good subsequences are: `[3]`, `[4]`, `[5]`, `[3,4]`, `[4,5]`, `[3,4,5]`.

	- The sum of elements in these subsequences is 40.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`
