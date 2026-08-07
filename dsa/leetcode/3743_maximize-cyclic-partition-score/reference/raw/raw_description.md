## Description

You are given a **cyclic** array `nums` and an integer `k`.

**Partition** `nums` into **at most** `k`** **<span data-keyword="subarray-nonempty">subarrays</span>. As `nums` is cyclic, these subarrays may wrap around from the end of the array back to the beginning.

The **range** of a subarray is the difference between its **maximum** and **minimum** values. The **score** of a partition is the sum of subarray **ranges**.

Return the **maximum** possible **score** among all cyclic partitions.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,3], k = 2</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Partition `nums` into `[2, 3]` and `[3, 1]` (wrapped around).

	- The range of `[2, 3]` is `max(2, 3) - min(2, 3) = 3 - 2 = 1`.

	- The range of `[3, 1]` is `max(3, 1) - min(3, 1) = 3 - 1 = 2`.

	- The score is `1 + 2 = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,3], k = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Partition `nums` into `[1, 2, 3, 3]`.

	- The range of `[1, 2, 3, 3]` is `max(1, 2, 3, 3) - min(1, 2, 3, 3) = 3 - 1 = 2`.

	- The score is 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,3], k = 4</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

Identical to Example 1, we partition `nums` into `[2, 3]` and `[3, 1]`. Note that `nums` may be partitioned into fewer than `k` subarrays.

</div>

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= nums.length`
