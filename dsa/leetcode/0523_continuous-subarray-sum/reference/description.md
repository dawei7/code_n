### 1. Description

Given an integer array nums and an integer k, return `true` *if *`nums`* has a **good subarray** or *`false`* otherwise*.

A **good subarray** is a subarray where:

- its length is **at least two**, and

- the sum of the elements of the subarray is a multiple of `k`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that:

- A **subarray** is a contiguous part of the array.

- An integer `x` is a multiple of `k` if there exists an integer `n` such that $x = n * k$. `0` is **always** a multiple of `k`.

### 4. Examples

#### Example 1

- **Input:** `nums = [23,<u>2,4</u>,6,7], k = 6`
- **Output:** `true`
- **Explanation:** [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
#### Example 2

- **Input:** `nums = [<u>23,2,6,4,7</u>], k = 6`
- **Output:** `true`
- **Explanation:** [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#### Example 3

- **Input:** `nums = [23,2,6,4,7], k = 13`
- **Output:** `false`

### 5. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$

- $0 \le sum(\text{nums}[i]) \le 2^{31} - 1$

- $1 \le k \le 2^{31} - 1$