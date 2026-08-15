### 1. Description

You are given an integer array `nums` of length `n` and an integer `k`.

A pair of indices `(i, j)` is called **valid** if:

- $0 \le i < j < n$

- $j - i \ge k$

Return the **maximum** value of $\text{nums}[i] + \text{nums}[j]$ among all valid pairs.

### 2. Function Contract

`solve(nums, k) -> int`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: A positive integer array whose values contribute to the pair sum.
- `k`: The minimum allowed index distance between the first and second selected positions.

**Output**

Return the maximum $\text{nums}[i] + \text{nums}[j]$ over all indices satisfying $0 \le i < j < n$ and $j - i \ge k$. Indices, rather than value differences, determine validity.

### 3. Examples

#### Example 1

- **Input:** nums = [1,3,5,2,8], k = 2

- **Output:** 13

- **Explanation:** The valid pairs are:

- `(0, 2)`: $\text{nums}[0] + \text{nums}[2] = 6$

- `(0, 3)`: $\text{nums}[0] + \text{nums}[3] = 3$

- `(0, 4)`: $\text{nums}[0] + \text{nums}[4] = 9$

- `(1, 3)`: $\text{nums}[1] + \text{nums}[3] = 5$

- `(1, 4)`: $\text{nums}[1] + \text{nums}[4] = 11$

- `(2, 4)`: $\text{nums}[2] + \text{nums}[4] = 13$

Thus, the answer is 13.​​​​​​​

#### Example 2

- **Input:** nums = [5,1,9], k = 1

- **Output:** 14

- **Explanation:** 

- Since $k = 1$, every pair is valid.

- The maximum value is obtained from a pair `(0, 2)`​​​​​​​, which is $\text{nums}[0] + \text{nums}[2] = 5 + 9 = 14$.

- Thus, the answer is 14.

### 4. Constraints

- $2 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le n - 1$
