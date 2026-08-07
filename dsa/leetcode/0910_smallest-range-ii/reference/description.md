### 1. Description

You are given an integer array `nums` and an integer `k`.

For each index `i` where $0 \le i < \text{nums.length}$, change $\text{nums}[i]$ to be either $\text{nums}[i] + k$ or $\text{nums}[i] - k$.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

Return *the minimum **score** of *`nums`* after changing the values at each index*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [1], k = 0`
- **Output:** `0`
- **Explanation:** The score is max(nums) - min(nums) = 1 - 1 = 0.
#### Example 2

- **Input:** `nums = [0,10], k = 2`
- **Output:** `6`
- **Explanation:** Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
#### Example 3

- **Input:** `nums = [1,3,6], k = 3`
- **Output:** `3`
- **Explanation:** Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $0 \le \text{nums}[i] \le 10^{4}$

- $0 \le k \le 10^{4}$