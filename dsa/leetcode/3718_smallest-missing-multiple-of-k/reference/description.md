### 1. Description

Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A **multiple** of `k` is any positive integer divisible by `k`.

### 2. Function Contract

**Inputs**

- `nums`: The integer values in which to test membership.
- `k`: The positive divisor whose positive multiples are considered.

**Return value**

Return the first value in the sequence $k, 2k, 3k, \ldots$ that is absent from `nums`.

### 3. Examples

#### Example 1

- **Input:** nums = [8,2,3,4,6], k = 2

- **Output:** 10

- **Explanation:** The multiples of $k = 2$ are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

#### Example 2

- **Input:** nums = [1,4,7,10,15], k = 5

- **Output:** 5

- **Explanation:** The multiples of $k = 5$ are 5, 10, 15, 20... and the smallest multiple missing from `nums` is 5.

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$

- $1 \le k \le 100$
