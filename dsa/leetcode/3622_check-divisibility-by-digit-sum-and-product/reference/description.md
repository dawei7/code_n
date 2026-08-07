## Description

You are given a positive integer `n`. Determine whether `n` is divisible by the **sum **of the following two values:

- The **digit sum** of `n` (the sum of its digits).

- The **digit** **product** of `n` (the product of its digits).

Return `true` if `n` is divisible by this sum; otherwise, return `false`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 99

**Output:** true

**Explanation:**

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 23

**Output:** false

**Explanation:**

Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

</div>
### Constraints

- $1 \le n \le 10^{6}$