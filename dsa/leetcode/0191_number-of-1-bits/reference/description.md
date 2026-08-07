### 1. Description

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).

### 2. Function Contract

**Inputs**

- `n`: A positive integer in the permitted signed 32-bit range.

**Return value**

Return the count of binary positions whose value is `1`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 11

**Output:** 3

**Explanation:**

The input binary string **1011** has a total of three set bits.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 128

**Output:** 1

**Explanation:**

The input binary string **10000000** has a total of one set bit.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 2147483645

**Output:** 30

**Explanation:**

The input binary string **1111111111111111111111111111101** has a total of thirty set bits.

</div>

### 4. Constraints

- $1 \le n \le 2^{31} - 1$

**Follow up:** If this function is called many times, how would you optimize it?