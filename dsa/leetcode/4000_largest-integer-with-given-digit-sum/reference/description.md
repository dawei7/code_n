### 1. Description

You are given two non-negative integers `n` and `s`.

Return the **largest** integer that has **at most** `n` digits and whose sum of digits is `s`. If no such integer exists, return -1.

### 2. Function Contract

**Inputs**

- `n`: The maximum number of decimal digits allowed in the result.
- `s`: The required sum of the result's decimal digits.

A returned positive integer has no leading zero. The integer `0` is a valid non-negative integer with digit sum zero.

**Return value**

Return the largest non-negative integer with at most `n` digits and digit sum `s`. Return `-1` when no such integer exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 2, s = 9

**Output:** 90

**Explanation:**

The largest integer with at most 2 digits that has a sum of digits of 9 is 90.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2, s = 19

**Output:** -1

**Explanation:**

There is no integer with at most 2 digits that has a sum of digits of 19, so the answer is -1.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5, s = 0

**Output:** 0

**Explanation:**

The only non-negative integer whose digits sum to 0 is 0.

</div>

### 4. Constraints

- $1 \le n \le 5$

- $0 \le s \le 100$