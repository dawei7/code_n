### 1. Description

You are given two positive integers, `l` and `r`. A positive integer is called **beautiful** if the product of its digits is divisible by the sum of its digits.

Return the count of **beautiful** numbers between `l` and `r`, inclusive.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** l = 10, r = 20

**Output:** 2

**Explanation:**

The beautiful numbers in the range are 10 and 20.

</div>
#### Example 2

<div class="example-block">
**Input:** l = 1, r = 15

**Output:** 10

**Explanation:**

The beautiful numbers in the range are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

</div>

### 4. Constraints

- $1 \le l \le r < 10^{9}$