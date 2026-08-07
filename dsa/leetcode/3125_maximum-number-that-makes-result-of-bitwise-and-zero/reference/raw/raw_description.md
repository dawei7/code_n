## Description

Given an integer `n`, return the **maximum** integer `x` such that `x <= n`, and the bitwise `AND` of all the numbers in the range `[x, n]` is 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 7</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The bitwise `AND` of `[6, 7]` is 6.

The bitwise `AND` of `[5, 6, 7]` is 4.

The bitwise `AND` of `[4, 5, 6, 7]` is 4.

The bitwise `AND` of `[3, 4, 5, 6, 7]` is 0.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 9</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

The bitwise `AND` of `[7, 8, 9]` is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 17</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

The bitwise `AND` of `[15, 16, 17]` is 0.

</div>

**Constraints:**

	- `1 <= n <= 10^15`
