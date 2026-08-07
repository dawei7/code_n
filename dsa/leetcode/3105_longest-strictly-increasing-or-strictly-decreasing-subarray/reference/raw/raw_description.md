## Description

You are given an array of integers `nums`. Return *the length of the **longest** <span data-keyword="subarray-nonempty">subarray</span> of *`nums`* which is either **<span data-keyword="strictly-increasing-array">strictly increasing</span>** or **<span data-keyword="strictly-decreasing-array">strictly decreasing</span>***.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,3,3,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The strictly increasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`.

The strictly decreasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`.

Hence, we return `2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,3,3,3]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The strictly increasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

Hence, we return `1`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,1]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The strictly increasing subarrays of `nums` are `[3]`, `[2]`, and `[1]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[2]`, `[1]`, `[3,2]`, `[2,1]`, and `[3,2,1]`.

Hence, we return `3`.

</div>

**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`
