### 1. Description

You are given an array of integers `nums` **(0-indexed)** and an integer `k`.

The **score** of a subarray `(i, j)` is defined as $min(\text{nums}[i], nums[i+1], ..., \text{nums}[j]) * (j - i + 1)$. A **good** subarray is a subarray where $i \le k \le j$.

Return *the maximum possible **score** of a **good** subarray.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,4,3,7,4,5], k = 3`
- **Output:** `15`
- **Explanation:** The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
#### Example 2

- **Input:** `nums = [5,5,4,5,4,1,1,1], k = 0`
- **Output:** `20`
- **Explanation:** The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 2 * 10^{4}$

- $0 \le k < \text{nums.length}$