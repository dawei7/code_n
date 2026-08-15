### 1. Description

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return *the* $$n^{\text{th}}$$ ***ugly number***.

### 2. Function Contract

**Inputs**

- `n`: A one-based position in the increasing ugly-number sequence.

**Return value**

Return the ugly number at position `n`, counting `1` as the first value.

### 3. Examples

#### Example 1

- **Input:** $n = 10$
- **Output:** `12`
- **Explanation:** [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

#### Example 2

- **Input:** $n = 1$
- **Output:** `1`
- **Explanation:** 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

### 4. Constraints

- $1 \le n \le 1690$
