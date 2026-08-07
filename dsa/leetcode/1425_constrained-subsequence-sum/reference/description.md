### 1. Description

Given an integer array `nums` and an integer `k`, return the maximum sum of a **non-empty** subsequence of that array such that for every two **consecutive** integers in the subsequence, $\text{nums}[i]$ and $\text{nums}[j]$, where `i < j`, the condition $j - i \le k$ is satisfied.

A *subsequence* of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [10,2,-10,5,20], k = 2`
- **Output:** `37`
- **Explanation:** The subsequence is [10, 2, 5, 20].
#### Example 2

- **Input:** `nums = [-1,-2,-3], k = 1`
- **Output:** `-1`
- **Explanation:** The subsequence must be non-empty, so we choose the largest number.
#### Example 3

- **Input:** `nums = [10,-2,-10,-5,20], k = 2`
- **Output:** `23`
- **Explanation:** The subsequence is [10, -2, -5, 20].

### 4. Constraints

- $1 \le k \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$