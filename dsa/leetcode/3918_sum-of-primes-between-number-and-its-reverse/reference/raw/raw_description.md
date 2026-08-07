## Description

You are given an integer `n`.

Let `r` be the integer formed by reversing the digits of `n`.

Return the **sum** of all <span data-keyword="prime-number">prime numbers</span> between `min(n, r)` and `max(n, r)`, inclusive.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 13</span>

**Output:** <span class="example-io">132</span>

**Explanation:**

	- The reverse of 13 is 31. Thus, the range is `[13, 31]`.

	- The prime numbers in this range are 13, 17, 19, 23, 29, and 31.

	- The sum of these prime numbers is `13 + 17 + 19 + 23 + 29 + 31 = 132`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 10</span>

**Output:** <span class="example-io">17</span>

**Explanation:**

	- The reverse of 10 is 1. Thus, the range is `[1, 10]`.

	- The prime numbers in this range are 2, 3, 5, and 7.

	- The sum of these prime numbers is `2 + 3 + 5 + 7 = 17`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 8</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The reverse of 8 is 8. Thus, the range is `[8, 8]`.

	- There are no prime numbers in this range, so the sum is 0.

</div>

**Constraints:**

	- `1 <= n <= 1000`
