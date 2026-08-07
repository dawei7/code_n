## Description

You are given two **positive** integers `n` and `k`.

An integer `x` is called **k-palindromic** if:

	- `x` is a <span data-keyword="palindrome-integer">palindrome</span>.

	- `x` is divisible by `k`.

Return the** largest** integer having `n` digits (as a string) that is **k-palindromic**.

**Note** that the integer must **not** have leading zeros.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, k = 5</span>

**Output:** <span class="example-io">"595"</span>

**Explanation:**

595 is the largest k-palindromic integer with 3 digits.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 1, k = 4</span>

**Output:** <span class="example-io">"8"</span>

**Explanation:**

4 and 8 are the only k-palindromic integers with 1 digit.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, k = 6</span>

**Output:** <span class="example-io">"89898"</span>

</div>

**Constraints:**

	- `1 <= n <= 10^5`

	- `1 <= k <= 9`
