### 1. Description

You are given an integer array `nums`, an integer array `queries`, and an integer `x`.

For each $\text{queries}[i]$, you need to find the index of the $\text{queries}[i]^th$ occurrence of `x` in the `nums` array. If there are fewer than $\text{queries}[i]$ occurrences of `x`, the answer should be -1 for that query.

Return an integer array `answer` containing the answers to all queries.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[int]`).
- `x`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,3,1,7], queries = [1,3,2,4], x = 1

- **Output:** [0,-1,2,-1]

- **Explanation:** 

- For the 1^st query, the first occurrence of 1 is at index 0.

- For the 2^nd query, there are only two occurrences of 1 in `nums`, so the answer is -1.

- For the 3^rd query, the second occurrence of 1 is at index 2.

- For the 4^th query, there are only two occurrences of 1 in `nums`, so the answer is -1.

#### Example 2

- **Input:** nums = [1,2,3], queries = [10], x = 5

- **Output:** [-1]

- **Explanation:** 

- For the 1^st query, 5 doesn't exist in `nums`, so the answer is -1.

### 4. Constraints

- $1 \le \text{nums.length}, \text{queries.length} \le 10^{5}$

- $1 \le \text{queries}[i] \le 10^{5}$

- $1 \le \text{nums}[i], x \le 10^{4}$
