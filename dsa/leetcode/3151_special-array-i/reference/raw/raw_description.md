## Description

An array is considered **special** if the *parity* of every pair of adjacent elements is different. In other words, one element in each pair **must** be even, and the other **must** be odd.

You are given an array of integers `nums`. Return `true` if `nums` is a **special** array, otherwise, return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

There is only one element. So the answer is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,4]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

There is only two pairs: `(2,1)` and `(1,4)`, and both of them contain numbers with different parity. So the answer is `true`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,1,6]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

`nums[1]` and `nums[2]` are both odd. So the answer is `false`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`
