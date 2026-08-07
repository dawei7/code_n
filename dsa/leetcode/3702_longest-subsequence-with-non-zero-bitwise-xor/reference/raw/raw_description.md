## Description

You are given an integer array `nums`.

Return the length of the **longest <span data-keyword="subsequence-array-nonempty">subsequence</span>** in `nums` whose bitwise **XOR** is **non-zero**. If no such **subsequence** exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One longest subsequence is `[2, 3]`. The bitwise XOR is computed as `2 XOR 3 = 1`, which is non-zero.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,3,4]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The longest subsequence is `[2, 3, 4]`. The bitwise XOR is computed as `2 XOR 3 XOR 4 = 5`, which is non-zero.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`
