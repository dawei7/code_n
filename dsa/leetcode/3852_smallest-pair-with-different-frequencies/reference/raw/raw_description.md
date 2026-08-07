## Description

You are given an integer array `nums`.

Consider all pairs of **distinct** values `x` and `y` from `nums` such that:

	- `x < y`

	- `x` and `y` have different <span data-keyword="frequency-array">frequencies</span> in `nums`.

Among all such pairs:

	- Choose the pair with the smallest possible value of `x`.

	- If multiple pairs have the same `x`, choose the one with the smallest possible value of `y`.

Return an integer array `[x, y]`. If no valid pair exists, return `[-1, -1]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,2,2,3,4]</span>

**Output:** <span class="example-io">[1,3]</span>

**Explanation:**

The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is `[1, 3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,5]</span>

**Output:** <span class="example-io">[-1,-1]</span>

**Explanation:**

Both values have the same frequency, so no valid pair exists. Return `[-1, -1]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7]</span>

**Output:** <span class="example-io">[-1,-1]</span>

**Explanation:**

There is only one value in the array, so no valid pair exists. Return `[-1, -1]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
