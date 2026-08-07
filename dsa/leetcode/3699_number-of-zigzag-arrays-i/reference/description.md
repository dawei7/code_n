### 1. Description

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

- Each element lies in the range `[l, r]`.

- No **two** adjacent elements are equal.

- No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** $10^{9} + 7$.

A **sequence** is said to be **strictly increasing** if each element is strictly greater than its previous one (if exists).

A **sequence** is said to be **strictly decreasing** if each element is strictly smaller than its previous one (if exists).

### 2. Function Contract

**Inputs**

- `n`: The required array length.
- `l`: The smallest permitted element value.
- `r`: The largest permitted element value.

Every element must lie in the inclusive integer interval `[l, r]`. Adjacent values cannot be equal, and the direction of successive adjacent comparisons cannot repeat.

**Return value**

Return the total number of valid length-`n` ZigZag arrays, reduced modulo $10^9+7$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, l = 4, r = 5

**Output:** 2

**Explanation:**

There are only 2 valid ZigZag arrays of length $n = 3$ using values in the range `[4, 5]`:

- `[4, 5, 4]`

- `[5, 4, 5]`​​​​​​​

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

### 4. Constraints

- $3 \le n \le 2000$

- $1 \le l < r \le 2000$