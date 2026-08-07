## Description

You are given an integer array `nums`. You have to find the **maximum** sum of a pair of numbers from `nums` such that the **largest digit **in both numbers is equal.

For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

Return the **maximum** sum or -1 if no such pair exists.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [112,131,411]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

Each numbers largest digit in order is [2,3,4].

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2536,1613,3366,162]</span>

**Output:** <span class="example-io">5902</span>

**Explanation:**

All the numbers have 6 as their largest digit, so the answer is <span class="example-io">2536 + 3366 = 5902.</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [51,71,17,24,42]</span>

**Output:** <span class="example-io">88</span>

**Explanation:**

Each number's largest digit in order is [5,7,7,4,4].

So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 10^4`
