### 1. Description

A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank">**perfect number**</a> is a **positive integer** that is equal to the sum of its **positive divisors**, excluding the number itself. A **divisor** of an integer `x` is an integer that can divide `x` evenly.

Given an integer `n`, return `true`* if *`n`* is a perfect number, otherwise return *`false`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $num = 28$
- **Output:** `true`
- **Explanation:** 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
#### Example 2

- **Input:** $num = 7$
- **Output:** `false`

### 4. Constraints

- $1 \le num \le 10^{8}$