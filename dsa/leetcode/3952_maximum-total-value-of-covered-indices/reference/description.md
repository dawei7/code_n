### 1. Description

You are given an integer array `nums` of length `n` and a binary string `s` of length `n`, where $s[i] = '1'$ means index `i` initially contains a **token** and $s[i] = '0'$ means it does not.

You may perform the following operation any number of times:

- Choose a token currently located at index `i`, where `i > 0`, such that this token has **not** been moved before.

- Move this token from index `i` to index $i - 1$.

An index is considered **covered** if it contains a token after all moves.

Return an integer denoting the **maximum total value** of `nums` at the covered indices after optimally performing the operations.

### 2. Function Contract

**Inputs**

- `nums`: Positive values associated with the indexed positions.
- `s`: A same-length binary string indicating the initial token positions.

Let $n=\texttt{nums.length}=\texttt{s.length}$.

**Return value**

Return the largest sum of values at distinct covered indices obtainable when every token moves left at most once.

### 3. Examples

#### Example 1

- **Input:** nums = [9,2,6,1], s = "0101"

- **Output:** 15

- **Explanation:** 

- Initially, indices 1 and 3 contain tokens.

- Move the token from index 3 to index 2.

- Move the token from index 1 to index 0.

- The covered indices are `[0, 2]`, so the total value is $\text{nums}[0] + \text{nums}[2] = 9 + 6 = 15$.

#### Example 2

- **Input:** nums = [5,1,4], s = "001"

- **Output:** 4

- **Explanation:** 

- Initially, only index 2 contains a token.

- It is optimal to leave the token at index 2.

- The covered index is `[2]`, so the total value is $\text{nums}[2] = 4$.

#### Example 3

- **Input:** nums = [9,3,5], s = "011"

- **Output:** 14

- **Explanation:** 

- Initially, indices 1 and 2 contain tokens.

- Move the token from index 1 to index 0.

- The covered indices are `[0, 2]`, so the total value is $\text{nums}[0] + \text{nums}[2] = 9 + 5 = 14$.

### 4. Constraints

- $1 \le n = \text{nums.length} = \text{s.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $s[i]$ is either `'0'` or `'1'`
