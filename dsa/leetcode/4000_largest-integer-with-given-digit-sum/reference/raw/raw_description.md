## Description

You are given two non-negative integers `n` and `s`.

Return the **largest** integer that has **at most** `n` digits and whose sum of digits is `s`. If no such integer exists, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, s = 9</span>

**Output:** <span class="example-io">90</span>

**Explanation:**

The largest integer with at most 2 digits that has a sum of digits of 9 is 90.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, s = 19</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

There is no integer with at most 2 digits that has a sum of digits of 19, so the answer is -1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, s = 0</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The only non-negative integer whose digits sum to 0 is 0.

</div>

**Constraints:**

	- `1 <= n <= 5`

	- `0 <= s <= 100`
