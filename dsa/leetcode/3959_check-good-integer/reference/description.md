## Description

You are given a positive integer `n`.

Let `digitSum` be the sum of the digits of `n`, and let `squareSum` be the sum of the squares of the digits of `n`.

An integer is called **good** if $squareSum - digitSum \ge 50$.

Return `true` if `n` is good. Otherwise, return `false`.
### Function Contract

**Inputs**

- `n`: The positive integer whose decimal digits are examined.

Leading zeroes are not part of the integer's decimal representation. Zeroes that occur inside the representation contribute zero to both sums.

**Return value**

Return `true` when `squareSum - digitSum >= 50`; otherwise, return `false`.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 1000

**Output:** false

**Explanation:**

- The digits of 1000 are 1, 0, 0, and 0.

- The `digitSum` is $1 + 0 + 0 + 0 = 1$.

- The `squareSum` is $1^{2} + 0^{2} + 0^{2} + 0^{2} = 1$.

- The $squareSum - digitSum$ is $1 - 1 = 0$. As 0 is not greater than or equal to 50, the output is `false`.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 19

**Output:** true

**Explanation:**

- The digits of 19 are 1 and 9.

- The `digitSum` is $1 + 9 = 10$.

- The `squareSum` is $1^{2} + 9^{2} = 1 + 81 = 82$.

- The $squareSum - digitSum$ is $82 - 10 = 72$. As 72 is greater than or equal to 50, the output is `true`.

</div>
### Constraints

- $1 \le n \le 10^{9}$