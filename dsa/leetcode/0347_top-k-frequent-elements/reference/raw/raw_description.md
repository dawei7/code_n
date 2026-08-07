## Description

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,2,2,3], k = 2</span>

**Output:** <span class="example-io">[1,2]</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1], k = 1</span>

**Output:** <span class="example-io">[1]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,1,2,1,2,3,1,3,2], k = 2</span>

**Output:** <span class="example-io">[1,2]</span>

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

	- `k` is in the range `[1, the number of unique elements in the array]`.

	- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.
