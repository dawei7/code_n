## Description

You are given an integer array `nums` of length `n` and an integer `k`.

A **semi‑repeating** subarray is a contiguous subarray in which at most `k` elements repeat (i.e., appear more than once).

Return the length of the longest **semi‑repeating** subarray in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,1,2,3,4], k = 2</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

The longest semi-repeating subarray is `[2, 3, 1, 2, 3, 4]`, which has two repeating elements (2 and 3).

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,1,1], k = 4</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The longest semi-repeating subarray is `[1, 1, 1, 1, 1]`, which has only one repeating element (1).

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,1,1], k = 0</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The longest semi-repeating subarray is `[1]`, which has no repeating elements.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `0 <= k <= nums.length`
