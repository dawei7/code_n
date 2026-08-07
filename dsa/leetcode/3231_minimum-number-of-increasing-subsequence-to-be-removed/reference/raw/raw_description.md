## Description

Given an array of integers `nums`, you are allowed to perform the following operation any number of times:

	- Remove a **strictly increasing** <span data-keyword="subsequence-array">subsequence</span> from the array.

Your task is to find the **minimum** number of operations required to make the array **empty**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,3,1,4,2]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

We remove subsequences `[1, 2]`, `[3, 4]`, `[5]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5]</span>

**Output:** <span class="example-io">1</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,3,2,1]</span>

**Output:** <span class="example-io">5</span>

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
