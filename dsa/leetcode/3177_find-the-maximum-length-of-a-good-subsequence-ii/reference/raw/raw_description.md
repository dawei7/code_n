## Description

You are given an integer array `nums` and a **non-negative** integer `k`. A sequence of integers `seq` is called **good** if there are **at most** `k` indices `i` in the range `[0, seq.length - 2]` such that `seq[i] != seq[i + 1]`.

Return the **maximum** possible length of a **good** <span data-keyword="subsequence-array">subsequence</span> of `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,1,3], k = 2</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The maximum length subsequence is `[<u>1</u>,<u>2</u>,<u>1</u>,<u>1</u>,3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5,1], k = 0</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The maximum length subsequence is `[<u>1</u>,2,3,4,5,<u>1</u>]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 5 * 10^3`

	- `1 <= nums[i] <= 10^9`

	- `0 <= k <= min(50, nums.length)`
