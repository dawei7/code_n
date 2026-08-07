## Description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is **exactly** `1`.

Given an integer array `nums`, return the length of its longest harmonious <span data-keyword="subsequence-array">subsequence</span> among all its possible subsequences.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2,2,5,2,3,7]</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The longest harmonious subsequence is `[3,2,2,2,3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of 2.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,1]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No harmonic subsequence exists.

</div>

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`
