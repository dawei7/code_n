### 1. Description

You are given an array `nums` consisting of integers. You are also given a 2D array `queries`, where $\text{queries}[i] = [\text{pos}_{i}, x_{i}]$.

For query `i`, we first set $nums[\text{pos}_{i}]$ equal to $x_{i}$, then we calculate the answer to query `i` which is the **maximum** sum of a subsequence of `nums` where **no two adjacent elements are selected**.

Return the *sum* of the answers to all queries.

Since the final answer may be very large, return it **modulo** $10^{9} + 7$.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [3,5,9], queries = [[1,-2],[0,-3]]

- **Output:** 21

- **Explanation:** After the 1^st query, `nums = [3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is $3 + 9 = 12$.

After the 2^nd query, `nums = [-3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is 9.

#### Example 2

- **Input:** nums = [0,-1], queries = [[0,-5]]

- **Output:** 0

- **Explanation:** After the 1^st query, `nums = [-5,-1]` and the maximum sum of a subsequence with non-adjacent elements is 0 (choosing an empty subsequence).

### 4. Constraints

- $1 \le \text{nums.length} \le 5 * 10^{4}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 5 * 10^{4}$

- $\text{queries}[i] = [\text{pos}_{i}, x_{i}]$

- $0 \le \text{pos}_{i} \le \text{nums.length} - 1$

- $-10^{5} \le x_{i} \le 10^{5}$
