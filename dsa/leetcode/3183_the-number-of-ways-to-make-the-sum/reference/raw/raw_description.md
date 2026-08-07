## Description

You have an **infinite** number of coins with values 1, 2, and 6, and **only** 2 coins with value 4.

Given an integer `n`, return the number of ways to make the sum of `n` with the coins you have.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Note** that the order of the coins doesn't matter and `[2, 2, 3]` is the same as `[2, 3, 2]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Here are the four combinations: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[2, 2]`, `[4]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 12</span>

**Output:** <span class="example-io">22</span>

**Explanation:**

Note that `[4, 4, 4]` is **not** a valid combination since we cannot use 4 three times.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Here are the four combinations: `[1, 1, 1, 1, 1]`, `[1, 1, 1, 2]`, `[1, 2, 2]`, `[1, 4]`.

</div>

**Constraints:**

	- `1 <= n <= 10^5`
