### 1. Description

Given an integer `n`, return `true`* if *`n`* has **exactly three positive divisors**. Otherwise, return *`false`.

An integer `m` is a **divisor** of `n` if there exists an integer `k` such that $n = k * m$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $n = 2$
- **Output:** `false`
**Explantion:** 2 has only two divisors: 1 and 2.
#### Example 2

- **Input:** $n = 4$
- **Output:** `true`
**Explantion:** 4 has three divisors: 1, 2, and 4.

### 4. Constraints

- $1 \le n \le 10^{4}$