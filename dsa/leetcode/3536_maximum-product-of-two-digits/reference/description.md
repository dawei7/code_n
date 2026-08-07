## Description

You are given a positive integer `n`.

Return the **maximum** product of any two digits in `n`.

**Note:** You may use the **same** digit twice if it appears more than once in `n`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 31

**Output:** 3

**Explanation:**

- The digits of `n` are `[3, 1]`.

- The possible products of any two digits are: $3 * 1 = 3$.

- The maximum product is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 22

**Output:** 4

**Explanation:**

- The digits of `n` are `[2, 2]`.

- The possible products of any two digits are: $2 * 2 = 4$.

- The maximum product is 4.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 124

**Output:** 8

**Explanation:**

- The digits of `n` are `[1, 2, 4]`.

- The possible products of any two digits are: $1 * 2 = 2$, $1 * 4 = 4$, $2 * 4 = 8$.

- The maximum product is 8.

</div>
### Constraints

- $10 \le n \le 10^{9}$