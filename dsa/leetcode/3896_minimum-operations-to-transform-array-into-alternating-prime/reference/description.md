### 1. Description

You are given an integer array `nums`.

An array is considered **alternating prime** if:

- Elements at **even** indices (0-based) are **prime** numbers.

- Elements at **odd** indices are **non-prime** numbers.

In one operation, you may **increment** any element by 1.

Return the **minimum** number of operations required to transform `nums` into an **alternating prime** array.

A **prime** number is a natural number greater than 1 with only two factors, 1 and itself.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty integer array to transform by incrementing individual elements.

Index parity is zero-based. Let $N=\texttt{nums.length}$ and let $M=\max(\texttt{nums})$.

**Return value**

Return the minimum number of unit increments required so every even-indexed value is prime and every odd-indexed value is non-prime.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,4]

- **Output:** 3

- **Explanation:** 

- The element at index 0 must be prime. Increment $\text{nums}[0] = 1$ to 2, using 1 operation.

- The element at index 1 must be non-prime. Increment $\text{nums}[1] = 2$ to 4, using 2 operations.

- The element at index 2 is already prime.

- The element at index 3 is already non-prime.

Total operations = $1 + 2 = 3$.

#### Example 2

- **Input:** nums = [5,6,7,8]

- **Output:** 0

- **Explanation:** 

- The elements at indices 0 and 2 are already prime.

- The elements at indices 1 and 3 are already non-prime.

No operations are needed.

#### Example 3

- **Input:** nums = [4,4]

- **Output:** 1

- **Explanation:** 

- The element at index 0 must be prime. Increment $\text{nums}[0] = 4$ to 5, using 1 operation.

- The element at index 1 is already non-prime.

Total operations = 1.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$
