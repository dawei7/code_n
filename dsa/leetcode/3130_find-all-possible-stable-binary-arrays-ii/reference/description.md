### 1. Description

You are given 3 positive integers $\text{num}_{zeros}$, $\text{num}_{ones}$, and `limit`.

A binary array `arr` is called **stable** if:

- The number of occurrences of 0 in `arr` is **exactly **$\text{num}_{zeros}$.

- The number of occurrences of 1 in `arr` is **exactly** $\text{num}_{ones}$.

- Each subarray of `arr` with a size greater than `limit` must contain **at least** one occurrence of **both** 0 and 1.

Return an integer denoting the *total* number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** zero = 1, one = 1, limit = 2

**Output:** 2

**Explanation:**

The two possible stable binary arrays are `[1,0]` and `[0,1]`.

</div>
#### Example 2

<div class="example-block">
**Input:** zero = 1, one = 2, limit = 1

**Output:** 1

**Explanation:**

The only possible stable binary array is `[1,0,1]`.

</div>
#### Example 3

<div class="example-block">
**Input:** zero = 3, one = 3, limit = 2

**Output:** 14

**Explanation:**

All the possible stable binary arrays are `[0,0,1,0,1,1]`, `[0,0,1,1,0,1]`, `[0,1,0,0,1,1]`, `[0,1,0,1,0,1]`, `[0,1,0,1,1,0]`, `[0,1,1,0,0,1]`, `[0,1,1,0,1,0]`, `[1,0,0,1,0,1]`, `[1,0,0,1,1,0]`, `[1,0,1,0,0,1]`, `[1,0,1,0,1,0]`, `[1,0,1,1,0,0]`, `[1,1,0,0,1,0]`, and `[1,1,0,1,0,0]`.

</div>

### 4. Constraints

- $1 \le zero, one, limit \le 1000$