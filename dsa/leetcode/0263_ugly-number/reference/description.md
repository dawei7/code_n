### 1. Description

An **ugly number** is a *positive* integer which does not have a prime factor other than 2, 3, and 5.

Given an integer `n`, return `true` *if* `n` *is an **ugly number***.

### 2. Function Contract

**Inputs**

- `n`: An integer to classify.

**Return value**

Return `true` exactly when `n` is positive and has no prime factor other than `2`, `3`, or `5`.

### 3. Examples

#### Example 1

- **Input:** $n = 6$
- **Output:** `true`
- **Explanation:** 6 = 2 × 3
#### Example 2

- **Input:** $n = 1$
- **Output:** `true`
- **Explanation:** 1 has no prime factors.
#### Example 3

- **Input:** $n = 14$
- **Output:** `false`
- **Explanation:** 14 is not ugly since it includes the prime factor 7.

### 4. Constraints

- $-2^{31} \le n \le 2^{31} - 1$