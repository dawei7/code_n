## Description

You are given an integer array `nums`.

Return an integer denoting the first **even** integer (earliest by array index) that appears **exactly** once in `nums`. If no such integer exists, return -1.

An integer `x` is considered **even** if it is divisible by 2.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,4,2,5,4,6]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

No even integer appears exactly once, so return -1.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
