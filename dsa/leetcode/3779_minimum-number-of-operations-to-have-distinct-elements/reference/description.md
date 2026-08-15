### 1. Description

You are given an integer array `nums`.

In one operation, you remove the **first three elements** of the current array. If there are fewer than three elements remaining, **all** remaining elements are removed.

Repeat this operation until the array is empty or contains no duplicate values.

Return an integer denoting the number of operations required.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty integer array.

Let $N=\lvert\texttt{nums}\rvert$. Each operation discards one prefix of length $\min(3,\text{current length})$; it never removes elements from another position or changes the relative order of survivors.

**Return value**

Return the minimum—and, because the operation is fixed, uniquely determined—number of prefix-removal operations needed until the remaining suffix is empty or has pairwise-distinct values.

### 3. Examples

#### Example 1

- **Input:** nums = [3,8,3,6,5,8]

- **Output:** 1

- **Explanation:** In the first operation, we remove the first three elements. The remaining elements `[6, 5, 8]` are all distinct, so we stop. Only one operation is needed.

#### Example 2

- **Input:** nums = [2,2]

- **Output:** 1

- **Explanation:** After one operation, the array becomes empty, which meets the stopping condition.

#### Example 3

- **Input:** nums = [4,3,5,1,2]

- **Output:** 0

- **Explanation:** All elements in the array are distinct, therefore no operations are needed.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$
