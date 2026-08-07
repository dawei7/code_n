## Description

You are given an integer `n`.

A sequence is formed as follows:

	- The `1^st` block contains `1`.

	- The `2^nd` block contains `2 * 3`.

	- The `i^th` block is the product of the next `i` consecutive integers.

Let `F(n)` be the sum of the first `n` blocks.

Return an integer denoting `F(n)` **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">127</span>

**Explanation:**​​​​​​​

	- Block 1: `1`

	- Block 2: `2 * 3 = 6`

	- Block 3: `4 * 5 * 6 = 120`

`F(3) = 1 + 6 + 120 = 127`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 7</span>

**Output:** <span class="example-io">6997165</span>

**Explanation:**

	- Block 1: `1`

	- Block 2: `2 * 3 = 6`

	- Block 3: `4 * 5 * 6 = 120`

	- Block 4: `7 * 8 * 9 * 10 = 5040`

	- Block 5: `11 * 12 * 13 * 14 * 15 = 360360`

	- Block 6: `16 * 17 * 18 * 19 * 20 * 21 = 39070080`

	- Block 7: `22 * 23 * 24 * 25 * 26 * 27 * 28 = 5967561600`

`F(7) = 6006997207 % (10^9 + 7) = 6997165`

</div>

**Constraints:**

	- `1 <= n <= 1000`
