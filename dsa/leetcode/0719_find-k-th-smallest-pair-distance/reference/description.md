### 1. Description

The **distance of a pair** of integers `a` and `b` is defined as the absolute difference between `a` and `b`.

Given an integer array `nums` and an integer `k`, return *the* $$k^{\text{th}}$$ *smallest **distance among all the pairs*** $\text{nums}[i]$ *and* $\text{nums}[j]$ *where* $0 \le i < j < \text{nums.length}$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,3,1], k = 1`
- **Output:** `0`
- **Explanation:** Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1^st smallest distance pair is (1,1), and its distance is 0.
#### Example 2

- **Input:** `nums = [1,1,1], k = 2`
- **Output:** `0`
#### Example 3

- **Input:** `nums = [1,6,1], k = 3`
- **Output:** `5`

### 4. Constraints

- $n = \text{nums.length}$

- $2 \le n \le 10^{4}$

- $0 \le \text{nums}[i] \le 10^{6}$

- $1 \le k \le n * (n - 1) / 2$