## Description

You are given an integer array `nums`.
A <span data-keyword="subsequence-array">subsequence</span> `sub` of `nums` with length `x` is called **valid** if it satisfies:

	- `(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.`

Return the length of the **longest** **valid** subsequence of `nums`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The longest valid subsequence is `[1, 2, 3, 4]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,1,2,1,2]</span>

**Output:** 6

**Explanation:**

The longest valid subsequence is `[1, 2, 1, 2, 1, 2]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The longest valid subsequence is `[1, 3]`.

</div>

**Constraints:**

	- `2 <= nums.length <= 2 * 10^5`

	- `1 <= nums[i] <= 10^7`
