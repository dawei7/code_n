### 1. Description

Given an integer `n`, return *the number of prime numbers that are strictly less than* `n`.

### 2. Function Contract

**Inputs**

- `n`: The exclusive upper bound for the prime numbers being counted.

**Return value**

Return the number of primes in the half-open interval $[0,n)$.

### 3. Examples

#### Example 1

- **Input:** $n = 10$
- **Output:** `4`
- **Explanation:** There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#### Example 2

- **Input:** $n = 0$
- **Output:** `0`
#### Example 3

- **Input:** $n = 1$
- **Output:** `0`

### 4. Constraints

- $0 \le n \le 5 * 10^{6}$