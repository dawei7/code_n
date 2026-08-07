## Description

You have an **infinite** number of coins with values 1, 2, and 6, and **only** 2 coins with value 4.

Given an integer `n`, return the number of ways to make the sum of `n` with the coins you have.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

**Note** that the order of the coins doesn't matter and `[2, 2, 3]` is the same as `[2, 3, 2]`.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 4

**Output:** 4

**Explanation:**

Here are the four combinations: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[2, 2]`, `[4]`.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 12

**Output:** 22

**Explanation:**

Note that `[4, 4, 4]` is **not** a valid combination since we cannot use 4 three times.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5

**Output:** 4

**Explanation:**

Here are the four combinations: `[1, 1, 1, 1, 1]`, `[1, 1, 1, 2]`, `[1, 2, 2]`, `[1, 4]`.

</div>
### Constraints

- $1 \le n \le 10^{5}$