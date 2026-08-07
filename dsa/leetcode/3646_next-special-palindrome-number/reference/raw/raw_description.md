## Description

You are given an integer `n`.

A number is called **special** if:

	- It is a **<span data-keyword="palindrome-integer">palindrome</span>**.

	- Every digit `k` in the number appears **exactly** `k` times.

Return the **smallest** special number **strictly **greater than `n`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 2</span>

**Output:** <span class="example-io">22</span>

**Explanation:**

22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 33</span>

**Output:** <span class="example-io">212</span>

**Explanation:**

212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.

</div>

**Constraints:**

	- `0 <= n <= 10^15`
