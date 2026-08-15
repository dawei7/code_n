### 1. Description

You are given an integer array `nums`. Your task is to remove **all elements** from the array by performing one of the following operations at each step until `nums` is empty:

- Choose any two elements from the first three elements of `nums` and remove them. The cost of this operation is the **maximum** of the two elements removed.

- If fewer than three elements remain in `nums`, remove all the remaining elements in a single operation. The cost of this operation is the **maximum** of the remaining elements.

Return the **minimum** cost required to remove all the elements.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [6,2,8,4]

- **Output:** 12

- **Explanation:** Initially, `nums = [6, 2, 8, 4]`.

- In the first operation, remove $\text{nums}[0] = 6$ and $\text{nums}[2] = 8$ with a cost of $max(6, 8) = 8$. Now, `nums = [2, 4]`.

- In the second operation, remove the remaining elements with a cost of $max(2, 4) = 4$.

The cost to remove all elements is $8 + 4 = 12$. This is the minimum cost to remove all elements in `nums`. Hence, the output is 12.

#### Example 2

- **Input:** nums = [2,1,3,3]

- **Output:** 5

- **Explanation:** Initially, `nums = [2, 1, 3, 3]`.

- In the first operation, remove $\text{nums}[0] = 2$ and $\text{nums}[1] = 1$ with a cost of $max(2, 1) = 2$. Now, `nums = [3, 3]`.

- In the second operation remove the remaining elements with a cost of $max(3, 3) = 3$.

The cost to remove all elements is $2 + 3 = 5$. This is the minimum cost to remove all elements in `nums`. Hence, the output is 5.

### 4. Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 10^{6}$
