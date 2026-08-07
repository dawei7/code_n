## Description

You are given a **positive** integer `n`.

Let `even` denote the number of even indices in the binary representation of `n` with value 1.

Let `odd` denote the number of odd indices in the binary representation of `n` with value 1.

Note that bits are indexed from **right to left** in the binary representation of a number.

Return the array `[even, odd]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 50</span>

**Output:** <span class="example-io">[1,2]</span>

**Explanation:**

The binary representation of 50 is `110010`.

It contains 1 on indices 1, 4, and 5.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2</span>

**Output:** <span class="example-io">[0,1]</span>

**Explanation:**

The binary representation of 2 is `10`.

It contains 1 only on index 1.

</div>

**Constraints:**

	- `1 <= n <= 1000`
