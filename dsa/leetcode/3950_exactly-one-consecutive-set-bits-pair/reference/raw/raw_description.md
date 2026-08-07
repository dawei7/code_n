## Description

You are given an integer `n`.

Return `true` if its binary representation contains **exactly one adjacent pair** of <span data-keyword="set-bit">set bits</span>, and `false` otherwise.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 6</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

	- Binary representation of 6 is `110`.

	- There is exactly one adjacent pair of set bits (`"11"`). Thus, the answer is `true`​​​​​​​.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

	- Binary representation of 5 is `101`.

	- There is no adjacent pair of set bits. Thus, the answer is `false`​​​​​​​.

</div>

**Constraints:**

	- `0 <= n <= 10^5`
