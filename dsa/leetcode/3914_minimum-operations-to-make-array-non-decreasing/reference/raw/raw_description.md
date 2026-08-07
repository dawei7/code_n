## Description

You are given an integer array `nums` of length `n`.

In one operation, you may choose any **<span data-keyword="subarray-nonempty">subarray</span>** `nums[l..r]` and **increase** each element in that **subarray** by `x`, where `x` is any **positive** integer.

Return the **minimum** possible **sum** of the values of `x` across all operations required to make the array **non-decreasing**.

An array is **non-decreasing** if `nums[i] <= nums[i + 1]` for all `0 <= i < n - 1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,3,2,1]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One optimal set of operations:

	- Choose subarray `[2..3]` and add `x = 1` resulting in `[3, 3, 3, 2]`

	- Choose subarray `[3..3]` and add `x = 1` resulting in `[3, 3, 3, 3]`

The array becomes non-decreasing, and the total sum of chosen `x` values is `1 + 1 = 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,1,2,3]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

One optimal set of operations:

	- Choose subarray `[1..3]` and add `x = 4` resulting in `[5, 5, 6, 7]`

The array becomes non-decreasing, and the total sum of chosen `x` values is `4`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`
