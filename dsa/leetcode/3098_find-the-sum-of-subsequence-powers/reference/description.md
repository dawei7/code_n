### 1. Description

You are given an integer array `nums` of length `n`, and a **positive** integer `k`.

The **power** of a subsequence is defined as the **minimum** absolute difference between **any** two elements in the subsequence.

Return *the **sum** of **powers** of **all** subsequences of *`nums`* which have length* ***equal to*** `k`.

Since the answer may be large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,4], k = 3

- **Output:** 4

- **Explanation:** There are 4 subsequences in `nums` which have length 3: `[1,2,3]`, `[1,3,4]`, `[1,2,4]`, and `[2,3,4]`. The sum of powers is $|2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4$.

#### Example 2

- **Input:** nums = [2,2], k = 2

- **Output:** 0

- **Explanation:** The only subsequence in `nums` which has length 2 is `[2,2]`. The sum of powers is $|2 - 2| = 0$.

#### Example 3

- **Input:** nums = [4,3,-1], k = 2

- **Output:** 10

- **Explanation:** There are 3 subsequences in `nums` which have length 2: `[4,3]`, `[4,-1]`, and `[3,-1]`. The sum of powers is $|4 - 3| + |4 - (-1)| + |3 - (-1)| = 10$.

### 4. Constraints

- $2 \le n = \text{nums.length} \le 50$

- $-10^{8} \le \text{nums}[i] \le 10^{8}$

- $2 \le k \le n$
