## Description

You are given a positive integer `n`.

Return the **maximum** product of any two digits in `n`.

**Note:** You may use the **same** digit twice if it appears more than once in `n`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 31</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The digits of `n` are `[3, 1]`.

	- The possible products of any two digits are: `3 * 1 = 3`.

	- The maximum product is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 22</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- The digits of `n` are `[2, 2]`.

	- The possible products of any two digits are: `2 * 2 = 4`.

	- The maximum product is 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 124</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

	- The digits of `n` are `[1, 2, 4]`.

	- The possible products of any two digits are: `1 * 2 = 2`, `1 * 4 = 4`, `2 * 4 = 8`.

	- The maximum product is 8.

</div>

**Constraints:**

	- `10 <= n <= 10^9`
