## Description

You are given an integer array `nums`.

Return `true` if the frequency of any element of the array is **prime**, otherwise, return `false`.

The **frequency** of an element `x` is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5,4]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

4 has a frequency of two, which is a prime number.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

All elements have a frequency of one.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,2,4,4]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

Both 2 and 4 have a prime frequency.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`
