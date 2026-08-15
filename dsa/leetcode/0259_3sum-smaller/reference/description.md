### 1. Description

Given an array of `n` integers `nums` and an integer `target`, find the number of index triplets `i`, `j`, `k` with $0 \le i < j < k < n$ that satisfy the condition $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] < target$.

### 2. Function Contract

**Inputs**

- `nums`: An integer array.
- `target`: The exclusive upper bound for each selected triple's sum.

**Return value**

Return the number of qualifying index triplets.

### 3. Examples

#### Example 1

- **Input:** `nums = [-2,0,1,3], target = 2`
- **Output:** `2`
- **Explanation:** Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

#### Example 2

- **Input:** `nums = [], target = 0`
- **Output:** `0`

#### Example 3

- **Input:** `nums = [0], target = 0`
- **Output:** `0`

### 4. Constraints

- $n = \text{nums.length}$

- $0 \le n \le 3500$

- $-100 \le \text{nums}[i] \le 100$

- $-100 \le target \le 100$

- The input is generated such that the answer is less than or equal to $10^{9}$.
