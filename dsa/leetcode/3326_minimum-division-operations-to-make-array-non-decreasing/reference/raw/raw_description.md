## Description

You are given an integer array `nums`.

Any **positive** divisor of a natural number `x` that is **strictly less** than `x` is called a **proper divisor** of `x`. For example, 2 is a *proper divisor* of 4, while 6 is not a *proper divisor* of 6.

You are allowed to perform an **operation** any number of times on `nums`, where in each **operation** you select any *one* element from `nums` and divide it by its **greatest** **proper divisor**.

Return the **minimum** number of **operations** required to make the array **non-decreasing**.

If it is **not** possible to make the array *non-decreasing* using any number of operations, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [25,7]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Using a single operation, 25 gets divided by 5 and `nums` becomes `[5, 7]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,7,6]</span>

**Output:** <span class="example-io">-1</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1,1,1]</span>

**Output:** <span class="example-io">0</span>

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`
