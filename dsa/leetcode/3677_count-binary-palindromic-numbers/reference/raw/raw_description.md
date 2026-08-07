## Description

You are given a **non-negative** integer `n`.

A **non-negative** integer is called **binary-palindromic** if its binary representation (written without leading zeros) reads the same forward and backward.

Return the number of integers `<font face="monospace">k</font>` such that `0 <= k <= n` and the binary representation of `<font face="monospace">k</font>` is a palindrome.

**Note:** The number 0 is considered binary-palindromic, and its representation is `"0"`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 9</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

The integers `k` in the range `[0, 9]` whose binary representations are palindromes are:

	- `0 → "0"`

	- `1 → "1"`

	- `3 → "11"`

	- `5 → "101"`

	- `7 → "111"`

	- `9 → "1001"`

All other values in `[0, 9]` have non-palindromic binary forms. Therefore, the count is 6.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 0</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Since `"0"` is a palindrome, the count is 1.

</div>

**Constraints:**

	- `0 <= n <= 10^15`
