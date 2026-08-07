## Description

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

- Each element lies in the range `[l, r]`.

- No **two** adjacent elements are equal.

- No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** $10^{9} + 7$.
### Function Contract

**Inputs**

- `n`: The required length of every counted array.
- `l`: The smallest value permitted in an array.
- `r`: The largest value permitted in an array.

Let $m=	exttt{r}-	exttt{l}+1$ be the number of available values.

**Return value**

Return, modulo $10^9+7$, the number of length-`n` arrays over `[l, r]` in which adjacent entries differ and every pair of consecutive comparison directions is opposite.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, l = 4, r = 5

**Output:** 2

**Explanation:**

There are only 2 valid ZigZag arrays of length $n = 3$ using values in the range `[4, 5]`:

- `[4, 5, 4]`

- `[5, 4, 5]`

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, l = 1, r = 3

**Output:** 10

**Explanation:**

There are 10 valid ZigZag arrays of length $n = 3$ using values in the range `[1, 3]`:

- `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`

- `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`

- `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`

All arrays meet the ZigZag conditions.

</div>
### Constraints

- $3 \le n \le 200$

- $1 \le l < r \le 10^​​​​​​​9$