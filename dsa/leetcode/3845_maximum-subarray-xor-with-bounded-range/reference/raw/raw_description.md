## Description

You are given a non-negative integer array `nums` and an integer `k`.

You must select a **<span data-keyword="subarray-nonempty">subarray</span>** of `nums` such that the **difference** between its **maximum** and **minimum** elements is at most `k`. The **value** of this subarray is the bitwise XOR of all elements in the subarray.

Return an integer denoting the **maximum** possible **value** of the selected subarray.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,5,6], k = 2</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

	- Select the subarray `[5, <u>**4, 5, 6**</u>]`.

	- The difference between its maximum and minimum elements is `6 - 4 = 2 <= k`.

	- The value is `4 XOR 5 XOR 6 = 7`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,5,6], k = 1</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- Select the subarray `[5, 4, 5, <u>**6**</u>]`.

	- The difference between its maximum and minimum elements is `6 - 6 = 0 <= k`.

	- The value is 6.

</div>

**Constraints:**

	- `1 <= nums.length <= 4 * 10^4`

	- `0 <= nums[i] < 2^15`

	- `0 <= k < 2^15`
