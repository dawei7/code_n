## Description

You are given an integer array `nums`.

The **factor score** of an array is defined as the *product* of the LCM and GCD of all elements of that array.

Return the **maximum factor score** of `nums` after removing **at most** one element from it.

**Note** that *both* the <span data-keyword="lcm-function">LCM</span> and <span data-keyword="gcd-function">GCD</span> of a single number are the number itself, and the *factor score* of an **empty** array is 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,4,8,16]</span>

**Output:** <span class="example-io">64</span>

**Explanation:**

On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of `4 * 16 = 64`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5]</span>

**Output:** <span class="example-io">60</span>

**Explanation:**

The maximum factor score of 60 can be obtained without removing any elements.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3]</span>

**Output:** 9

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 30`
