## Description

You are given an integer array `nums` of length `n` and an integer `k`.

An **inversion** is a pair of indices `(i, j)` from `nums` such that `i < j` and `nums[i] > nums[j]`.

The **inversion count** of a **<span data-keyword="subarray-nonempty">subarray</span>** is the number of inversions within it.

Return the **minimum** inversion count among all **subarrays** of `nums` with length `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2,5,4], k = 3</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

We consider all subarrays of length `k = 3` (indices below are relative to each subarray):

	- `[3, 1, 2]` has 2 inversions: `(0, 1)` and `(0, 2)`.

	- `[1, 2, 5]` has 0 inversions.

	- `[2, 5, 4]` has 1 inversion: `(1, 2)`.

The minimum inversion count among all subarrays of length `3` is 0, achieved by subarray `[1, 2, 5]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,3,2,1], k = 4</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

There is only one subarray of length `k = 4`: `[5, 3, 2, 1]`.

Within this subarray, the inversions are: `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)`, and `(2, 3)`.

Total inversions is 6, so the minimum inversion count is 6.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1], k = 1</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

All subarrays of length `k = 1` contain only one element, so no inversions are possible.

The minimum inversion count is therefore 0.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= n`
