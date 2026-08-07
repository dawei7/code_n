## Description

You are given an integer `n`.

Define its **mirror distance** as: `abs(n - reverse(n))`​​​​​​​ where `reverse(n)` is the integer formed by reversing the digits of `n`.

Return an integer denoting the mirror distance of `n`​​​​​​​.

`abs(x)` denotes the absolute value of `x`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 25</span>

**Output:** <span class="example-io">27</span>

**Explanation:**

	- `reverse(25) = 52`.

	- Thus, the answer is `abs(25 - 52) = 27`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 10</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

	- `reverse(10) = 01` which is 1.

	- Thus, the answer is `abs(10 - 1) = 9`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 7</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- `reverse(7) = 7`.

	- Thus, the answer is `abs(7 - 7) = 0`.

</div>

**Constraints:**

	- `1 <= n <= 10^9`
