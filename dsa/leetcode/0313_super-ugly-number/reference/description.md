### 1. Description

A **super ugly number** is a positive integer whose prime factors are in the array `primes`.

Given an integer `n` and an array of integers `primes`, return *the* $$n^{\text{th}}$$ ***super ugly number***.

The $$n^{\text{th}}$$ **super ugly number** is **guaranteed** to fit in a **32-bit** signed integer.

### 2. Function Contract

**Inputs**

- `n`: The one-based position in the increasing super-ugly-number sequence.
- `primes`: The sorted array of distinct allowed prime factors.

**Return value**

Return the $n$th positive integer whose prime factors all occur in `primes`.

### 3. Examples

#### Example 1

- **Input:** $n = 12, primes = [2,7,13,19]$
- **Output:** `32`
- **Explanation:** [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

#### Example 2

- **Input:** $n = 1, primes = [2,3,5]$
- **Output:** `1`
- **Explanation:** 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].

### 4. Constraints

- $1 \le n \le 10^{5}$

- $1 \le \text{primes.length} \le 100$

- $2 \le \text{primes}[i] \le 1000$

- $\text{primes}[i]$ is **guaranteed** to be a prime number.

- All the values of `primes` are **unique** and sorted in **ascending order**.
