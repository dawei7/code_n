## Description

You are given a **0-indexed** integer array `nums` consisting of `n` non-negative integers.

You are also given an array `queries`, where $\text{queries}[i] = [x_{i}, y_{i}]$. The answer to the $$i^{\text{th}}$$query is the sum of all$\text{nums}[j]$where$x_{i} \le j < n$and$(j - x_{i})$is divisible by$y_{i}$.

Return *an array *`answer`* where *$\text{answer.length} = \text{queries.length}$* and *$\text{answer}[i]$* is the answer to the *$$i^{\text{th}}$$* query **modulo** *$10^{9} + 7$.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

- **Input:** `nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]]`
- **Output:** `[9,18,10]`
- **Explanation:** The answers of the queries are as follows:
1) The j indices that satisfy this query are 0, 3, and 6. nums[0] + nums[3] + nums[6] = 9
2) The j indices that satisfy this query are 5, 6, and 7. nums[5] + nums[6] + nums[7] = 18
3) The j indices that satisfy this query are 4 and 6. nums[4] + nums[6] = 10
#### Example 2

- **Input:** `nums = [100,200,101,201,102,202,103,203], queries = [[0,7]]`
- **Output:** `[303]`
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 5 * 10^{4}$

- $0 \le \text{nums}[i] \le 10^{9}$

- $1 \le \text{queries.length} \le 1.5 * 10^{5}$

- $0 \le x_{i} < n$

- $1 \le y_{i} \le 5 * 10^{4}$