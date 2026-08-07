## Description

Given an array of positive integers `nums` of length `n` and a non‑negative integer `k`.

Return the number of **contiguous <span data-keyword="subarray">subarrays</span>** whose bitwise XOR of all elements is **greater** than or **equal** to `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2,3], k = 2</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

The valid subarrays with `XOR >= 2` are `[3]` at index 0, `[3, 1]` at indices 0 - 1, `[3, 1, 2, 3]` at indices 0 - 3, `[1, 2]` at indices 1 - 2, `[2]` at index 2, and `[3]` at index 3; there are 6 in total.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,0,0], k = 0</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

Every contiguous subarray yields `XOR = 0`, which meets `k = 0`. There are 6 such subarrays in total.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

	- `0 <= k <= 10^9`
