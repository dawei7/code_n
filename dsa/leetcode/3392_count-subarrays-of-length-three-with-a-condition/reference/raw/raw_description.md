## Description

Given an integer array `nums`, return the number of <span data-keyword="subarray-nonempty">subarrays</span> of length 3 such that the sum of the first and third numbers equals *exactly* half of the second number.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,4,1]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Only the subarray `[1,4,1]` contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

`[1,1,1]` is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

</div>

**Constraints:**

	- `3 <= nums.length <= 100`

	- `<font face="monospace">-100 <= nums[i] <= 100</font>`
