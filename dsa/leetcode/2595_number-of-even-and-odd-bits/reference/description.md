## Description

You are given a **positive** integer `n`.

Let `even` denote the number of even indices in the binary representation of `n` with value 1.

Let `odd` denote the number of odd indices in the binary representation of `n` with value 1.

Note that bits are indexed from **right to left** in the binary representation of a number.

Return the array `[even, odd]`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 50

**Output:** [1,2]

**Explanation:**

The binary representation of 50 is `110010`.

It contains 1 on indices 1, 4, and 5.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2

**Output:** [0,1]

**Explanation:**

The binary representation of 2 is `10`.

It contains 1 only on index 1.

</div>
### Constraints

- $1 \le n \le 1000$