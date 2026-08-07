## Description

Given three integer arrays `a`, `b`, and `c`, return the number of triplets `(a[i], b[j], c[k])`, such that the bitwise `XOR` between the elements of each triplet has an **even** number of <span data-keyword="set-bit">set bits</span>.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">a = [1], b = [2], c = [3]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only triplet is `(a[0], b[0], c[0])` and their `XOR` is: `1 XOR 2 XOR 3 = 00_2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">a = [1,1], b = [2,3], c = [1,5]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Consider these four triplets:

	- `(a[0], b[1], c[0])`: `1 XOR 3 XOR 1 = 011_2`

	- `(a[1], b[1], c[0])`: `1 XOR 3 XOR 1 = 011_2`

	- `(a[0], b[0], c[1])`: `1 XOR 2 XOR 5 = 110_2`

	- `(a[1], b[0], c[1])`: `1 XOR 2 XOR 5 = 110_2`

</div>

**Constraints:**

	- `1 <= a.length, b.length, c.length <= 10^5`

	- `0 <= a[i], b[i], c[i] <= 10^9`
