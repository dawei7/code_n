## Description

You are given an integer array `nums` and two integers, `k` and `m`.

Return the **maximum** sum of `k` non-overlapping <span data-keyword="subarray">subarrays</span> of `nums`, where each subarray has a length of **at least** `m`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,-1,3,3,4], k = 2, m = 2</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

The optimal choice is:

	- Subarray `nums[3..5]` with sum `3 + 3 + 4 = 10` (length is `3 >= m`).

	- Subarray `nums[0..1]` with sum `1 + 2 = 3` (length is `2 >= m`).

The total sum is `10 + 3 = 13`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-10,3,-1,-2], k = 4, m = 1</span>

**Output:** <span class="example-io">-10</span>

**Explanation:**

The optimal choice is choosing each element as a subarray. The output is `(-10) + 3 + (-1) + (-2) = -10`.

</div>

**Constraints:**

	- `1 <= nums.length <= 2000`

	- `-10^4 <= nums[i] <= 10^4`

	- `1 <= k <= floor(nums.length / m)`

	- `1 <= m <= 3`
