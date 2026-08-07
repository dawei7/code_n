## Description

Given a positive integer `n`, write a function that returns the number of <span data-keyword="set-bit">set bits</span> in its binary representation (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 11</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The input binary string **1011** has a total of three set bits.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 128</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The input binary string **10000000** has a total of one set bit.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 2147483645</span>

**Output:** <span class="example-io">30</span>

**Explanation:**

The input binary string **1111111111111111111111111111101** has a total of thirty set bits.

</div>

**Constraints:**

	- `1 <= n <= 2^31 - 1`

**Follow up:** If this function is called many times, how would you optimize it?
