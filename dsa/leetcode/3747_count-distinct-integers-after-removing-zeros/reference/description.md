### 1. Description

You are given a **positive** integer `n`.

For every integer `x` from 1 to `n`, we write down the integer obtained by removing all zeros from the decimal representation of `x`.

Return an integer denoting the number of **distinct** integers written down.

### 2. Function Contract

**Inputs**

- `n`: The positive inclusive upper bound of the source integers.

Removing zeros changes only a number's decimal digits; it does not remove or reorder any nonzero digit. Let $D$ be the number of decimal digits in `n`.

**Return value**

Return the number of distinct positive integers obtained after removing all decimal zeros from every `x` in the range $1 \leq x \leq n$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 10

**Output:** 9

**Explanation:**

The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3

**Output:** 3

**Explanation:**

The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).

</div>

### 4. Constraints

- $1 \le n \le 10^{15}$