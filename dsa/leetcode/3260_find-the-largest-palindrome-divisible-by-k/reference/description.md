### 1. Description

You are given two **positive** integers `n` and `k`.

An integer `x` is called **k-palindromic** if:

- `x` is a palindrome.

- `x` is divisible by `k`.

Return the** largest** integer having `n` digits (as a string) that is **k-palindromic**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that the integer must **not** have leading zeros.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, k = 5

**Output:** "595"

**Explanation:**

595 is the largest k-palindromic integer with 3 digits.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1, k = 4

**Output:** "8"

**Explanation:**

4 and 8 are the only k-palindromic integers with 1 digit.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5, k = 6

**Output:** "89898"

</div>

### 5. Constraints

- $1 \le n \le 10^{5}$

- $1 \le k \le 9$