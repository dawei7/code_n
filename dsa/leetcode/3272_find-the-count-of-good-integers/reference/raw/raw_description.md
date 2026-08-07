## Description

You are given two **positive** integers `n` and `k`.

An integer `x` is called **k-palindromic** if:

	- `x` is a <span data-keyword="palindrome-integer">palindrome</span>.

	- `x` is divisible by `k`.

An integer is called **good** if its digits can be *rearranged* to form a **k-palindromic** integer. For example, for `k = 2`, 2020 can be rearranged to form the *k-palindromic* integer 2002, whereas 1010 cannot be rearranged to form a *k-palindromic* integer.

Return the count of **good** integers containing `n` digits.

**Note** that *any* integer must **not** have leading zeros, **neither** before **nor** after rearrangement. For example, 1010 *cannot* be rearranged to form 101.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, k = 5</span>

**Output:** <span class="example-io">27</span>

**Explanation:**

*Some* of the good integers are:

	- 551 because it can be rearranged to form 515.

	- 525 because it is already k-palindromic.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 1, k = 4</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The two good integers are 4 and 8.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, k = 6</span>

**Output:** <span class="example-io">2468</span>

</div>

**Constraints:**

	- `1 <= n <= 10`

	- `1 <= k <= 9`
