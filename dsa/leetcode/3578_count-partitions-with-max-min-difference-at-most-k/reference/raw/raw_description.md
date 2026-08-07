## Description

You are given an integer array `nums` and an integer `k`. Your task is to partition `nums` into one or more **non-empty** contiguous segments such that in each segment, the difference between its **maximum** and **minimum** elements is **at most** `k`.

Return the total number of ways to partition `nums` under this condition.

Since the answer may be too large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [9,4,1,3,7], k = 4</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most `k = 4`:

	- `[[9], [4], [1], [3], [7]]`

	- `[[9], [4], [1], [3, 7]]`

	- `[[9], [4], [1, 3], [7]]`

	- `[[9], [4, 1], [3], [7]]`

	- `[[9], [4, 1], [3, 7]]`

	- `[[9], [4, 1, 3], [7]]`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,3,4], k = 0</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

There are 2 valid partitions that satisfy the given conditions:

	- `[[3], [3], [4]]`

	- `[[3, 3], [4]]`

</div>

**Constraints:**

	- `2 <= nums.length <= 5 * 10^4`

	- `1 <= nums[i] <= 10^9`

	- `0 <= k <= 10^9`
