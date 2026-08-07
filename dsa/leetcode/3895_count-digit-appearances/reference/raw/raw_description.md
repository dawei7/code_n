## Description

You are given an integer array `nums` and an integer `digit`.

Return the total number of times `digit` appears in the decimal representation of all elements in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [12,54,32,22], digit = 2</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,34,7], digit = 9</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The digit 9 does not appear in the decimal representation of any element in `nums`, so the total number of times digit 9 appears is 0.

</div>

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^6​​​​​​​`

	- `0 <= digit <= 9`
