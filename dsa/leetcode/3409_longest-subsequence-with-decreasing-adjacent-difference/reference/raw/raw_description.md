## Description

You are given an array of integers `nums`.

Your task is to find the length of the **longest** <span data-keyword="subsequence-array">subsequence</span> `seq` of `nums`, such that the **absolute differences** between* consecutive* elements form a **non-increasing sequence** of integers. In other words, for a subsequence `seq_0`, `seq_1`, `seq_2`, ..., `seq_m` of `nums`, `|seq_1 - seq_0| >= |seq_2 - seq_1| >= ... >= |seq_m - seq_m - 1|`.

Return the length of such a subsequence.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [16,6,3]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The longest subsequence is `[16, 6, 3]` with the absolute adjacent differences `[10, 3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [6,5,3,4,2,1]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The longest subsequence is `[6, 4, 2, 1]` with the absolute adjacent differences `[2, 2, 1]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,20,10,19,10,20]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The longest subsequence is `[10, 20, 10, 19, 10]` with the absolute adjacent differences `[10, 10, 9, 9]`.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^4`

	- `1 <= nums[i] <= 300`
