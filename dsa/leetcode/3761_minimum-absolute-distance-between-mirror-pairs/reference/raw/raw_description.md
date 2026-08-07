## Description

You are given an integer array `nums`.

A **mirror pair** is a pair of indices `(i, j)` such that:

	- `0 <= i < j < nums.length`, and

	- `reverse(nums[i]) == nums[j]`, where `reverse(x)` denotes the integer formed by reversing the digits of `x`. Leading zeros are omitted after reversing, for example `reverse(120) = 21`.

Return the **minimum** absolute distance between the indices of any mirror pair. The absolute distance between indices `i` and `j` is `abs(i - j)`.

If no mirror pair exists, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [12,21,45,33,54]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The mirror pairs are:

	- (0, 1) since `reverse(nums[0]) = reverse(12) = 21 = nums[1]`, giving an absolute distance `abs(0 - 1) = 1`.

	- (2, 4) since `reverse(nums[2]) = reverse(45) = 54 = nums[4]`, giving an absolute distance `abs(2 - 4) = 2`.

The minimum absolute distance among all pairs is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [120,21]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

There is only one mirror pair (0, 1) since `reverse(nums[0]) = reverse(120) = 21 = nums[1]`.

The minimum absolute distance is 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [21,120]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

There are no mirror pairs in the array.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`​​​​​​​
