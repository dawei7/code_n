### 1. Description

Given an array of integers `nums`, you are allowed to perform the following operation any number of times:

- Remove a **strictly increasing** subsequence from the array.

Your task is to find the **minimum** number of operations required to make the array **empty**.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** nums = [5,3,1,4,2]

- **Output:** 3

- **Explanation:** We remove subsequences `[1, 2]`, `[3, 4]`, `[5]`.

#### Example 2

- **Input:** nums = [1,2,3,4,5]

- **Output:** 1

#### Example 3

- **Input:** nums = [5,4,3,2,1]

- **Output:** 5

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$
