### 1. Description

You are given an array `nums` consisting of non-negative integers. You are also given a `queries` array, where $\text{queries}[i] = [x_{i}, m_{i}]$.

The answer to the $$i^{\text{th}}$$ query is the maximum bitwise `XOR` value of $x_{i}$ and any element of `nums` that does not exceed $m_{i}$. In other words, the answer is $max(\text{nums}[j] XOR x_{i})$ for all `j` such that $\text{nums}[j] \le m_{i}$. If all elements in `nums` are larger than $m_{i}$, then the answer is `-1`.

Return *an integer array *`answer`* where *$\text{answer.length} = \text{queries.length}$* and *$\text{answer}[i]$* is the answer to the *$$i^{\text{th}}$$* query.*

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** `nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]`
- **Output:** `[3,3,7]`
- **Explanation:** 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

#### Example 2

- **Input:** `nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]`
- **Output:** `[15,-1,5]`

### 4. Constraints

- $1 \le \text{nums.length}, \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $0 \le \text{nums}[j], x_{i}, m_{i} \le 10^{9}$
