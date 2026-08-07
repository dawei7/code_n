## Description

Given an integer array `nums`, return the **length** of the **longest <span data-keyword="subarray-nonempty">subarray</span>** that has a bitwise XOR of zero and contains an **equal** number of **even** and **odd** numbers. If no such subarray exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,3,2,0]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The subarray `[1, 3, 2, 0]` has bitwise XOR `1 XOR 3 XOR 2 XOR 0 = 0` and contains 2 even and 2 odd numbers.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,8,5,4,14,9,15]</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

The whole array has bitwise XOR `0` and contains 4 even and 4 odd numbers.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No non-empty subarray satisfies both conditions.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`
