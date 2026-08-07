### 1. Description

You are given a **0-indexed** integer array `nums` containing `n` **distinct** positive integers. A permutation of `nums` is called special if:

- For all indexes $0 \le i < n - 1$, either $\text{nums}[i] \% nums[i+1] = 0$ or $nums[i+1] \% \text{nums}[i] = 0$.

Return *the total number of special permutations. *As the answer could be large, return it **modulo **$10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [2,3,6]`
- **Output:** `2`
- **Explanation:** [3,6,2] and [2,6,3] are the two special permutations of nums.
#### Example 2

- **Input:** `nums = [1,4,3]`
- **Output:** `2`
- **Explanation:** [3,1,4] and [4,1,3] are the two special permutations of nums.

### 4. Constraints

- $2 \le \text{nums.length} \le 14$

- $1 \le \text{nums}[i] \le 10^{9}$