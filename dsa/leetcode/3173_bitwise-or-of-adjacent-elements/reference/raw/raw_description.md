## Description

Given an array `nums` of length `n`, return an array `answer` of length `n - 1` such that `answer[i] = nums[i] | nums[i + 1]` where `|` is the bitwise `OR` operation.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,7,15]</span>

**Output:** <span class="example-io">[3,7,15]</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [8,4,2]</span>

**Output:** <span class="example-io">[12,6]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,9,11]</span>

**Output:** <span class="example-io">[5,13,11]</span>

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`
