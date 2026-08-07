### 1. Description

Given a **0-indexed** integer array `nums` and an integer `d`, return *the number of triplets* `(i, j, k)` *such that* `i < j < k` *and* $(\text{nums}[i] + \text{nums}[j] + \text{nums}[k]) \% d = 0$.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** `nums = [3,3,4,7,8], d = 5`
- **Output:** `3`
- **Explanation:** The triplets which are divisible by 5 are: (0, 1, 2), (0, 2, 4), (1, 2, 4).
It can be shown that no other triplet is divisible by 5. Hence, the answer is 3.
#### Example 2

- **Input:** `nums = [3,3,3,3], d = 3`
- **Output:** `4`
- **Explanation:** Any triplet chosen here has a sum of 9, which is divisible by 3. Hence, the answer is the total number of triplets which is 4.
#### Example 3

- **Input:** `nums = [3,3,3,3], d = 6`
- **Output:** `0`
- **Explanation:** Any triplet chosen here has a sum of 9, which is not divisible by 6. Hence, the answer is 0.

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le d \le 10^{9}$