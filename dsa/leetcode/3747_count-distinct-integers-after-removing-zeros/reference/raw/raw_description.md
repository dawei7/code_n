## Description

You are given a **positive** integer `n`.

For every integer `x` from 1 to `n`, we write down the integer obtained by removing all zeros from the decimal representation of `x`.

Return an integer denoting the number of **distinct** integers written down.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 10</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).

</div>

**Constraints:**

	- `1 <= n <= 10^15`
