## Description

You are given an integer array `nums` and an integer `m`.

Return the **maximum** product of the first and last elements of any **<span data-keyword="subsequence-array">subsequence</span>** of `nums` of size `m`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-1,-9,2,3,-2,-3,1], m = 1</span>

**Output:** <span class="example-io">81</span>

**Explanation:**

The subsequence `[-9]` has the largest product of the first and last elements: `-9 * -9 = 81`. Therefore, the answer is 81.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,-5,5,6,-4], m = 3</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

The subsequence `[-5, 6, -4]` has the largest product of the first and last elements.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,-1,2,-6,5,2,-5,7], m = 2</span>

**Output:** <span class="example-io">35</span>

**Explanation:**

The subsequence `[5, 7]` has the largest product of the first and last elements.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`

	- `1 <= m <= nums.length`
