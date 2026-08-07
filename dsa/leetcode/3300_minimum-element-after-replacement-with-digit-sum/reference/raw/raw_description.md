## Description

You are given an integer array `nums`.

You replace each element in `nums` with the **sum** of its digits.

Return the **minimum** element in `nums` after all replacements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,12,13,14]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

`nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

`nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [999,19,199]</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

`nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 10^4`
