## Description

You are given a **positive** integer `n`.

Let `s` be the **binary representation** of `n` without leading zeros.

The **reverse** of a binary string `s` is obtained by writing the characters of `s` in the opposite order.

You may flip any bit in `s` (change `0 → 1` or `1 → 0`). Each flip affects **exactly** one bit.

Return the **minimum** number of flips required to make `s` equal to the reverse of its original form.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 7</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The binary representation of 7 is `"111"`. Its reverse is also `"111"`, which is the same. Hence, no flips are needed.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 10</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The binary representation of 10 is `"1010"`. Its reverse is `"0101"`. All four bits must be flipped to make them equal. Thus, the minimum number of flips required is 4.

</div>

**Constraints:**

	- `1 <= n <= 10^9`
