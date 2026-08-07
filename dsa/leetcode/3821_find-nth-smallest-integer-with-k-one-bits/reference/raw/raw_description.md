## Description

You are given two positive integers `n` and `k`.

Return an integer denoting the `n^th` smallest positive integer that has **exactly** `k` ones in its binary representation. It is guaranteed that the answer is **strictly less** than `2^50`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, k = 2</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

The 4 smallest positive integers that have exactly `k = 2` ones in their binary representations are:

	- `3 = 11_2`

	- `5 = 101_2`

	- `6 = 110_2`

	- `9 = 1001_2`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, k = 1</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The 3 smallest positive integers that have exactly `k = 1` one in their binary representations are:

	- `1 = 1_2`

	- `2 = 10_2`

	- `4 = 100_2`

</div>

**Constraints:**

	- `1 <= n <= 2^50`

	- `1 <= k <= 50`

	- The answer is strictly less than `2^50`.
