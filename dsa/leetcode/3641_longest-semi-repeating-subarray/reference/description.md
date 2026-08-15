### 1. Description

You are given an integer array `nums` of length `n` and an integer `k`.

A **semi‑repeating** subarray is a contiguous subarray in which at most `k` elements repeat (i.e., appear more than once).

Return the length of the longest **semi‑repeating** subarray in `nums`.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,1,2,3,4], k = 2

- **Output:** 6

- **Explanation:** The longest semi-repeating subarray is `[2, 3, 1, 2, 3, 4]`, which has two repeating elements (2 and 3).

#### Example 2

- **Input:** nums = [1,1,1,1,1], k = 4

- **Output:** 5

- **Explanation:** The longest semi-repeating subarray is `[1, 1, 1, 1, 1]`, which has only one repeating element (1).

#### Example 3

- **Input:** nums = [1,1,1,1,1], k = 0

- **Output:** 1

- **Explanation:** The longest semi-repeating subarray is `[1]`, which has no repeating elements.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $0 \le k \le \text{nums.length}$
